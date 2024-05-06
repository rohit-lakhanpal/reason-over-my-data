import xml.etree.ElementTree as ET
import requests

# This function fetches the sitemap from a given URL
def fetch_sitemap(url):
    # If the url ends with /, then strip it
    if url.endswith('/'):
        url = url[:-1]

    # If the url does not end with /sitemap.xml, append it
    if not url.endswith('/sitemap.xml'):
        url = f'{url}/sitemap.xml'
    
    try:
        response = requests.get(f'{url}')
        response.raise_for_status()  # Will raise an HTTPError for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to fetch sitemap from {url}. Error message: {str(e)}")
        return None


# Try to fetch the sitemap from the given URL, if it exists, then the url is valid.
# Throw a custom exception if the URL is invalid. (Message: Invalid URL: {url}. Please provide a valid URL that contains a sitemap.xml file.)
def is_url_valid(url):    
    if not url:
        raise Exception("Invalid URL: You did not provide a URL. Please provide a valid URL that contains a sitemap.xml file.")

    try:
        response = fetch_sitemap(url)
        if response is None:
            raise Exception(f"Invalid URL: {url}. Please provide a valid URL that contains a sitemap.xml file.")
    except Exception as e:
        raise Exception(f"Invalid URL: {url}. Please provide a valid URL that contains a sitemap.xml file.")
    
    return True

# This function parses the sitemap content and returns a list of URLs 
def parse_sitemap(sitemap_content):
    namespace = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    
    try:
        root = ET.fromstring(sitemap_content)
    except ET.ParseError:
        print("Error: Unable to parse the sitemap content.")
        return []
    
    # If it's a sitemap index, recursively parse contained sitemaps
    if root.tag == f"{{{namespace['sitemap']}}}sitemapindex":
        sitemap_urls = [elem.text for elem in root.findall('.//sitemap:loc', namespace)]
        all_urls = []
        for sitemap_url in sitemap_urls:
            try:
                sitemap_content = fetch_sitemap(sitemap_url)
            except Exception as e:
                print(f"Error: Unable to fetch sitemap from {sitemap_url}. Error message: {str(e)}")
                continue

            if sitemap_content is not None:
                all_urls.extend(parse_sitemap(sitemap_content))
        return all_urls
    else:
        # It's a standard sitemap
        return [elem.text for elem in root.findall('.//sitemap:loc', namespace)]
    
# Filter the URLs to only include those that are allowed
def filter_urls(urls, allowed_paths):
    # If no allowed paths are provided, return all URLs
    if not allowed_paths:
        return urls
    
    return [url for url in urls if any([path in url for path in allowed_paths])]