import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from langdetect import detect

def is_from_docs_google(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc == 'docs.google.com'
def is_external_link(link, domain):
    parsed_link = urlparse(link)
    return parsed_link.netloc != domain

def count_external_links(url, html):
    soup = BeautifulSoup(html, 'html.parser')
    domain = urlparse(url).netloc
    external_links_count = 0

    for anchor_tag in soup.find_all('a', href=True):
        link = anchor_tag['href']
        if is_external_link(link, domain):
            external_links_count += 1

    return external_links_count

def phrase(html):
    soup = BeautifulSoup(html, 'html.parser')
    specific_element = soup.find(lambda tag: tag.name and "privacy policy" in tag.get_text().lower())

    if specific_element is None:
        specific_element = soup.find(lambda tag: tag.name and "privacy statement" in tag.get_text().lower())
        if specific_element is None:
            return ''
    # Get all the div elements up to the level where "private policy" is found
    parents_up_level = list(specific_element.find_parents())

    # Reverse the list to maintain the original order
    parents_up_level.reverse()

    privacy_policy=''
    for div in parents_up_level:
        privacy_policy+=div.text
    return privacy_policy

def detect_language(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Get the text content from the webpage
    text = soup.get_text()
    # Detect the language of the text
    language = detect(text)
    return language

def count_words(text):
    words = text.split()
    return len(words)
def examine(text):
    return count_words(text)>100


def get_privacy_text(url):


    if url==None:
        raise ValueError("Webpage Missing")

    if is_from_docs_google(url):
        return 0

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    headers = {'User-Agent': user_agent}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return ValueError("Webpage Unaccessible")

    if detect_language(response.text)!='en':
        return ValueError("Language Unsupported")

    privacy_text=phrase(response.text)
    if privacy_text=='':
        return ValueError("No Privacy Information Identified")

    return privacy_text
