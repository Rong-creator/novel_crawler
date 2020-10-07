import requests as req
from bs4 import BeautifulSoup
import __settings__ 
import re


def get_page(url):
	resp = req.get(url)
	return resp.text

def grab_content(page,selector):
	soup = BeautifulSoup(page, 'html.parser')
	elements = soup.select(selector)
	return elements

def remove_all_tags(content):
	pattern = re.compile(r'\s|<.*?>',re.S)
	result = pattern.sub('', content)
	return result

def main():
	page = get_page("https://www.biquge.com.cn/book/31833/489624.html")
	selector = "#content"
	content = grab_content(page,selector)
	print(remove_all_tags(str(content)))
    

if __name__ == "__main__":
    main()



