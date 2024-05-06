import os
import re
from uuid import uuid4
from datetime import datetime
from azure.data.tables import TableServiceClient, TableEntity


def get_base_64(url):
    if not url:
        return None    
    return url.encode("utf-8").hex()

def clean_url(url):
    if not url:
        return None    
    # From the URL, remove all parameters and fragments
    url = url.split('?')[0].split('#')[0]
    # Remove trailing slashes
    if url.endswith('/'):
        url = url[:-1]
    return url

def get_domain_from_url(url):
    if not url:
        return None    
    # Extract the domain from the URL
    domain = url.split('//')[-1].split('/')[0]
    return domain

def replace_special_chars(url):
    # Replace all non-alphanumeric characters (excluding underscores) with underscores
    return re.sub(r'[^a-zA-Z0-9_]', '_', url)

def generate_keys_from_url(url):
    if not url:
        return None
    # clean the URL
    url = clean_url(url)
    # get the domain from the URL
    domain = get_domain_from_url(url)
    # replace all special characters in the domain with underscores


    return {        
        "PartitionKey": replace_special_chars(domain),
        "RowKey": get_base_64(url),
        "Url": url,
        "Domain": domain
    }

def generate_entity_from_url(url):
    keys = generate_keys_from_url(url)
    current_time = datetime.now()
    if not keys:
        return None
    return {
        "PartitionKey": keys["PartitionKey"],
        "RowKey": keys["RowKey"],
        "Url": keys["Url"],
        "Domain": keys["Domain"],
        "Created": current_time,
        "Updated": current_time,
        "Deleted": False
    }

def get_table_client():
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    if not connection_string:
        raise Exception("Connection error: The connection string is empty. Please check the value of 'AZURE_STORAGE_CONNECTION_STRING' in the .env file.")
    
    try:
        table_service = TableServiceClient.from_connection_string(conn_str=connection_string)
        table_name = "inventory"
        return table_service.create_table_if_not_exists(table_name)
    except Exception as e:
        raise Exception(f"Connection error: Unable to connect to Azure Storage. Error message: {str(e)}")

def create_inventory_from_urls(urls):
    if not urls or not isinstance(urls, list):
        return None
    responses = []
    table_client = get_table_client()

    for url in urls:
        try:
            entity = generate_entity_from_url(url)
            if entity:                
                table_client.upsert_entity(entity=TableEntity(entity))
                print(f"Success: Inventory created for {url} with partition key: {entity['PartitionKey']} and row key: {entity['RowKey']}.")
                responses.append({
                    "url": url,
                    "partition_key": entity["PartitionKey"],
                    "row_key": entity["RowKey"],
                    "status": "Success"                
                })
        except Exception as e:
            print(f"Error: Unable to create inventory for {url}. Error message: {str(e)}")
            responses.append({
                "url": url,
                "status": "Error",
                "message": str(e)
            })
            continue
    return responses

def delete_inventory_table():
    try:
        table_client = get_table_client()
        table_client.delete_table()
        print("Success: Inventory table deleted.")
    except Exception as e:
        print(f"Error: Unable to delete inventory table. Error message: {str(e)}")

def get_inventory_table_count():
    try:
        table_client = get_table_client()
        entities = table_client.list_entities()
        row_count = sum(1 for _ in entities)
        return row_count
    except Exception as e:
        print(f"Error: Unable to get inventory table count. Error message: {str(e)}")
        return None
    
def get_inventory_entities_by_page(page_size, page_number):
    try:
        table_client = get_table_client()
        entities = table_client.list_entities(results_per_page=page_size)
        
        # Skip to the desired page
        skipped_pages = (page_number - 1) * page_size
        result_page = []
        
        for i, entity in enumerate(entities):
            if i < skipped_pages:
                continue
            result_page.append(entity)
            if len(result_page) == page_size:
                break
        
        return result_page
    except Exception as e:
        print(f"Error: Unable to get inventory entities. Error message: {str(e)}")
        return None