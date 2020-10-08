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

# remove all html tags then get pure novel content
def remove_all_tags(content):
	pattern = re.compile(r'\s|<.*?>',re.S)
	result = pattern.sub('', content)
	return result

def rel_or_abs_path(path):
	if "www." not in path:
		return True
	return False


# get all link to each chapters in novel's main page
def get_all_chapter_link(page, selector):
	href_list = []
	all_link = grab_content(page,selector)
	base = ''
	if len(all_link) == 0 :
		print("There is no chapter")
		return
	if rel_or_abs_path(all_link[0].get('href')):
		base = __settings__.root
	for i in all_link:
		link = i.get('href')
		link = base + link
		href_list.append(link)

	return href_list




def main():
	page = get_page("https://www.biquge.com.cn/book/31833/489624.html")
	page2 = get_page("https://www.biquge.com.cn/book/31833/")
	selector = "#content"
	selector2 = "#list > dl > dd > a"
	all_link = get_all_chapter_link(page2,selector2)
	for i in all_link:
		print(i)
	
    

if __name__ == "__main__":
    main()



