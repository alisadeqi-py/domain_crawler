import requests
from bs4 import BeautifulSoup
import pandas as pd



domains = ['dealer.com', 'dealers.getmyauto.com' , 'www.w3.org' , 'automanager.com'  , "autofunds.com"]


def load_data(data):
    url_list = []
    for row in range(len(data.iloc[:, 0])):
        item = [data.iloc[row, 2], data.index[data[2] == data.iloc[row, 2]].tolist()[0]]
        url_list.append(item)
    return url_list


def get_website_provider():
    data = pd.read_excel('Irvine-CA.xlsx')
    url_list = load_data(data)
    data['website_provider'] = None
    for url, index in url_list:

        try:
            print(url, index)
            response = requests.get(url, verify=False)
            print(response.status_code)
            if response.status_code == 200:
                for domain in domains:
                    if domain in response.text:
                        data.at[index, -1] = domain
                        print(f'{domain} ,set')
            else:
                print("Error: Status Code {}".format(response.status_code))
        except Exception as e:
            print(f"Error:{e}")


get_website_provider()
