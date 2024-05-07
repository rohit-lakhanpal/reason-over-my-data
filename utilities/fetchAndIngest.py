import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md, MarkdownConverter
from urllib.parse import urljoin
import hashlib
from datetime import datetime
import os
from llama_index.llms.azure_openai import AzureOpenAI
from llama_index.embeddings.azure_openai import AzureOpenAIEmbedding
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from llama_index.vector_stores.azureaisearch import AzureAISearchVectorStore
from llama_index.vector_stores.azureaisearch import (
    IndexManagement,
    MetadataIndexFieldType,
)
from llama_index.core import (    
    StorageContext,
    VectorStoreIndex,
)
from llama_index.core.settings import Settings
from llama_index.core import Document


def get_search_index(index_name):
    credential = AzureKeyCredential(os.getenv('AI_SEARCH_SERVICE_API_KEY'))
    index_client = SearchIndexClient(
        endpoint=os.getenv('AI_SEARCH_SERVICE_ENDPOINT'),
        credential=credential,
    )
    filterable_metadata_fields = {
            "title": ("title", MetadataIndexFieldType.STRING),
            "url": ("url", MetadataIndexFieldType.STRING),
            "hash": ("hash", MetadataIndexFieldType.STRING),
            "lastModified": ("lastModified", MetadataIndexFieldType.STRING),
            #"created": ("lastModified", MetadataIndexFieldType.STRING),
        }

    vector_store = AzureAISearchVectorStore(
        search_or_index_client=index_client,
        filterable_metadata_field_keys=filterable_metadata_fields,
        index_name=index_name,
        index_management=IndexManagement.CREATE_IF_NOT_EXISTS,
        id_field_key="id",
        chunk_field_key="text",
        embedding_field_key="embedding",
        embedding_dimensionality=1536,
        metadata_string_field_key="metadata",
        doc_id_field_key="doc_id",
        language_analyzer="en.lucene",
        vector_algorithm_type="exhaustiveKnn",
    )
    
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    models = get_aoai()
    Settings.llm = models['llm']
    Settings.embed_model = models['embed_model']
    
    return VectorStoreIndex.from_documents(
        [],
        storage_context=storage_context,
    )

def generate_llama_document(document):
    return Document(
                text=document["md"],
                doc_id=document['id'],
                # extra_info=document['url'],
                metadata={
                    "title": document['metadata']['title'],                 
                    "url": document['url'],
                    "hash": document['hash'],
                    "lastModified": document['metadata']['source-last-modified'],
                    # "created": document['created'], 
                }    
            )

def configure_search_and_store(document, index_name):
    try:
        credential = AzureKeyCredential(os.getenv('AI_SEARCH_SERVICE_API_KEY'))

        # Use index client to demonstrate creating an index
        index_client = SearchIndexClient(
            endpoint=os.getenv('AI_SEARCH_SERVICE_ENDPOINT'),
            credential=credential,
        )

        # Use search client to demonstration using existing index
        search_client = SearchClient(
            endpoint=os.getenv('AI_SEARCH_SERVICE_ENDPOINT'),
            index_name=index_name,
            credential=credential,
        )

        filterable_metadata_fields = {
            "title": ("title", MetadataIndexFieldType.STRING),
            "url": ("url", MetadataIndexFieldType.STRING),
            "hash": ("hash", MetadataIndexFieldType.STRING),
            "lastModified": ("lastModified", MetadataIndexFieldType.STRING),
            #"created": ("lastModified", MetadataIndexFieldType.STRING),
        }

        vector_store = AzureAISearchVectorStore(
            search_or_index_client=index_client,
            filterable_metadata_field_keys=filterable_metadata_fields,
            index_name=index_name,
            index_management=IndexManagement.CREATE_IF_NOT_EXISTS,
            id_field_key="id",
            chunk_field_key="text",
            embedding_field_key="embedding",
            embedding_dimensionality=1536,
            metadata_string_field_key="metadata",
            doc_id_field_key="doc_id",
            language_analyzer="en.lucene",
            vector_algorithm_type="exhaustiveKnn",
        )

        storage_context = StorageContext.from_defaults(vector_store=vector_store)

        models = get_aoai()
        Settings.llm = models['llm']
        Settings.embed_model = models['embed_model']

        return VectorStoreIndex.from_documents(
            [Document(
                text=document["md"],
                metadata={
                    "title": document['metadata']['title'],                 
                    "url": document['url'],
                    "hash": document['hash'],
                    "lastModified": document['metadata']['source-last-modified'],
                    "created": document['created'], 
                }    
            )], storage_context=storage_context
        )
            
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_aoai():
    llm = AzureOpenAI(
        model=os.getenv('AOAI_LLM_MODEL'),
        deployment_name=os.getenv('AOAI_LLM_DEPLOYMENT_NAME'),
        api_key=os.getenv('AOAI_API_KEY'),
        azure_endpoint=os.getenv('AOAI_ENDPOINT'),
        api_version=os.getenv('AOAI_API_VERSION'),
    )

    embed_model = AzureOpenAIEmbedding(
        model=os.getenv('AOAI_EMBEDDING_MODEL'),
        deployment_name=os.getenv('AOAI_EMBEDDING_DEPLOYMENT_NAME'),
        api_key=os.getenv('AOAI_API_KEY'),
        azure_endpoint=os.getenv('AOAI_ENDPOINT'),
        api_version=os.getenv('AOAI_API_VERSION')
    )

    return {
        'llm': llm,
        'embed_model': embed_model
    }

def get_md5_hash(string):
    return hashlib.md5(string.encode()).hexdigest()

class CustomImageBlockConverter(MarkdownConverter):
    def convert_img(self, el, text, convert_as_inline):
        alt_text = el.get('alt', '')
        src = el.get('src', '')
        return f"![{alt_text}]({src})"

def convert_html_to_markdown(html_content):
    try:
        return md(html_content, custom_block_converters=[CustomImageBlockConverter])
    except Exception as e:
        print(f"Error converting HTML to Markdown: {e}")
        return None

def fetch_url_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

def is_html_content(response):
    content_type = response.headers.get('Content-Type', '')
    if 'text/html' not in content_type:
        print(f"Invalid content type: {content_type}")
        return False
    return True

def extract_and_convert_html(response, base_url):
    try:
        soup = BeautifulSoup(response.text, 'html.parser')

        links_to = []
        images = []
        
        # Process <a>, <link>, and <script> tags to extract links
        for tag in soup.find_all(['a', 'link', 'script']):
            if tag.get('href'):
                full_url = urljoin(base_url, tag['href'])
                links_to.append(full_url)
                tag['href'] = full_url

        # Process <img> tags to extract image URLs
        for tag in soup.find_all('img'):
            if tag.get('src'):
                full_url = urljoin(base_url, tag['src'])
                images.append(full_url)
                tag['src'] = full_url

        # Extract metadata (title and meta tags)
        metadata = {
            'title': soup.title.string if soup.title else None,
            'description': None,
        }

        # Find description from meta tags
        for meta_tag in soup.find_all('meta'):
            if 'name' in meta_tag.attrs and 'content' in meta_tag.attrs:
                metadata[meta_tag['name']] = meta_tag['content']
            elif 'property' in meta_tag.attrs and 'content' in meta_tag.attrs:
                metadata[meta_tag['property']] = meta_tag['content']

        return {
            'content': str(soup),
            'metadata': metadata or None,  # Return None if metadata is empty
            'links': links_to,
            'images': images
        }
    except Exception as e:
        print(f"Error processing HTML content: {e}")
        return None

def fetch_document(url):
    response = fetch_url_content(url)
    if not response or not is_html_content(response):
        return None

    html_content = extract_and_convert_html(response, url)
    
    if html_content is None:
        return None
    
    if 'content' not in html_content or html_content['content'] is None:
        return None
    if 'metadata' not in html_content or html_content['metadata'] is None:
        return None

    metadata = html_content['metadata'] or None
    links = html_content['links'] or None
    images = html_content['images'] or None

    id = get_md5_hash(url)

    #current_date = datetime.now()

    return {
        'id': id,        
        'url': url,
        'html': html_content['content'],
        'md': convert_html_to_markdown(html_content['content']),        
        'metadata': metadata,
        'links': links,
        'images': images,
        # 'created': current_date.isoformat(),
        'hash': get_md5_hash(html_content['content'])
    }

def fetch_and_ingest_url_approach_001(url, index_name):
    # validate index_name is not null
    # validate index_name is not null
    if index_name is None:
        raise ValueError("Index name cannot be null")

    # step 1: fetch and convert
    document = fetch_document(url)

    # step 2: enrichments
    # None here

    # step 3: configure search and store
    return configure_search_and_store(document, index_name)