from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait




def get_novel_ID(novel_name, cssOfInput,cssOfsearch,css_first_search,root_website):
	novel_url = ""
	driver = webdriver.Firefox()
	driver.get(root_website)
	elem = driver.find_element_by_css_selector(cssOfInput)
	elem.clear()
	elem.send_keys(novel_name)
	# click search
	driver.find_element_by_css_selector(cssOfsearch).click()
	assert "No results found." not in driver.page_source

	
	driver.find_element_by_css_selector(css_first_search).click()
	assert "No results found." not in driver.page_source

	window_after = driver.window_handles[1]

	driver.switch_to.window(window_after)
	
	novel_url = driver.current_url
	driver.quit()

	return novel_url

def main():
	cssOfInput =  "#keyword"
	cssOfsearch = "#wrapper > div.header > div.search > span > input"
	css_first_search = "body > div.result-list > div:nth-child(1) > div.result-game-item-detail > h3 > a > span"
	root_website = "https://www.biquge.com.cn/"
	novel_name = "a"

	url = get_novel_ID(novel_name,cssOfInput,cssOfsearch,css_first_search ,root_website)
	print(url)




if __name__ == "__main__":
    main()
	

