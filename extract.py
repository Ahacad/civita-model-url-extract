import requests 
from bs4 import BeautifulSoup
from tqdm import tqdm
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("filename", help="File containing urls to extract model urls from")
parser.add_argument("savefile", help="File to be written to with extracted model urls")
args = parser.parse_args()

def extract_model_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    a_tags = soup.find_all("a", {"class": "mantine-UnstyledButton-root mantine-Button-root mantine-1movwzg"})
    
    return f"https://civitai.com{a_tags[0]['href']}"


with open(args.filename) as f:
    urls = f.readlines()

processed_urls = []
for url in tqdm(urls):
    processed_urls.append(extract_model_url(url.strip()))

with open(f"{args.savefile}.txt", "w") as f:
    for url in processed_urls:
        f.write(f"{url}\n")
