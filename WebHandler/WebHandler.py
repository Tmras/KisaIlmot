import requests
from bs4 import BeautifulSoup

from DocHandler.DataObject import DataObjectFencing


def get_site_content(url):

    # open URL
    resp = requests.get(url)
    # Check that response is ok
    if resp.status_code != 200:
        return ""

    return resp.text

def find_site_content(site_html, element, type):
    content_list = []
    html = BeautifulSoup(site_html, features="html.parser")
    if type == "fencing":

        # Go through the pages html content and put relevant items in list
        main_elem = html.find_all('div', class_=element.element.split(" "))
        for e in main_elem:
            try:
                date = e.find('span', class_=element.subelements[0]).text
                contest = e.find('a', class_=element.subelements[1]).text

                content_list.append(DataObjectFencing(date, contest))
            except:
                print(f"{e}")

    return content_list


