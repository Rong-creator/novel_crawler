import csv
import __settings__

def write_rows(filename,row_Data):
    with open(filename, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in row_Data:
            filewriter.writerow(row)

def read_csv(filename):
    result = []
    with open( filename, 'r') as f:
        reader = csv.reader(f)
        # read file row by row
        for row in reader:
            result.append(row)
    return result

def test_website_csv_data():
    # root, url_base ,search_box_css, search_button_css , search_result_css
    cssOfInput =  '#keyword'
    cssOfsearch = '#wrapper > div.header > div.search > span > input'
    css_first_search = 'body > div.result-list > div:nth-child(1) > div.result-game-item-detail > h3 > a > span'
    root_website = 'https://www.biquge.com.cn/'
    search_base = 'https://www.biquge.com.cn/book/'

    one = [root_website, search_base, cssOfInput, cssOfsearch, css_first_search]
    filename = __settings__.novel_website_csv
    write_rows(filename,[one])


def main():
    test_website_csv_data()




if __name__ == "__main__":
    main()
    





