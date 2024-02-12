import requests
from bs4 import BeautifulSoup
import pandas as pd



domains = ['dealer.com', 'dealers.getmyauto.com' , 'www.w3.org' , 'automanager.com'  , "autofunds.com"]


def load_data(data):
    url_list = []
    for row in range(len(data.iloc[:, 0])):
        item = [data.iloc[row, 2], data.index[data[2] == data.iloc[row, 2]].tolist()[0]]
        url_list.append(item)
        print('links collected')
    return url_list


def get_website_provider():
    data = pd.read_excel('Irvine-CA.xlsx')
    url_list = load_data(data)
    data['website_provider'] = None
    for url in url_list:

        try:
            response = requests.get(url[0])
            if response.status_code == 200:
                for domain in domains:
                    if domain in response.text:
                        data.at[url[1], -1] = domain
            else:
                return "Error: Status Code {}".format(response.status_code)
        except Exception as e:
            return "Error: {}".format(str(e))


load_data()
