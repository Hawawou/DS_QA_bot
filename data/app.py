import json
import requests
from bs4 import BeautifulSoup

reddit_url = "https://www.reddit.com/r/datascience/"
response = requests.get(reddit_url)
soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('div', class_='_1poyrkZ7g36PawDueRza-J')