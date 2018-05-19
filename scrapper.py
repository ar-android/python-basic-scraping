import requests, json
from bs4 import BeautifulSoup

def get(url):
  request = requests.get(url)
  content = request.content
  return BeautifulSoup(content, "html.parser")

def post(url, params):
  data = json.dumps(params)
  request = requests.post(url, data)
  return BeautifulSoup(request.content, "html.parser")
