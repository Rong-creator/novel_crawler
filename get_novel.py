import requests as req
import __settings__ 


def get_page(url):
	resp = req.get(url)
	return resp.text


def main():
	print(get_page(__settings__.novel_website))
    

if __name__ == "__main__":
    main()



