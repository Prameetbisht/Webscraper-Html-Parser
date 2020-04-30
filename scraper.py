import os
# from selenium import webdriver
# import os
from bs4 import BeautifulSoup
# import openpyxl
import pandas as pd
import csv

# from selenium.webdriver.common.keys import Keys
# import time
# from pprint import pprint
# from selenium.common.exceptions import NoSuchElementException
# import parser
person = {}
dir = "C:\\Users\\pbisht\\PycharmProjects\\Prameet\\local_sys_venv\\zagat (scrap)\\html_downloaded_pages\\"


def directory_file_fetch(dir):
    data_reataurant_name = []
    data_address = []
    data_rating = []

    for filename in os.listdir(dir):
        if filename.endswith(".html"):
            # print(dir+filename) cross verify the ress link
            with open(dir + filename, "r", encoding='utf-8') as f:
                contents = f.read()
                soup = BeautifulSoup(contents, features='lxml')
                res_name = soup.find(class_='h1-calibre zgt-place-sheet-title')
                rest_name_clean = str(res_name).split('title">')[1].split('</h1>')[0].replace('\n', '').strip()
                # data_reataurant_name.append()
                # print((format(res_name.text)) + ",")
                data_reataurant_name.append(rest_name_clean)
                res_add = soup.find(class_='zgt-business-detail-text flex')
                address_clean = str(res_add).split('flex="">')[1].split('</span>')[0]
                # data_address.append(address_clean)
                # print(address_clean)

                # exit()
                # print((format(res_add.text)) + ",")
                data_address.append(address_clean)

                try:
                    rating = soup.find('div', attrs={'class': 'zgt-place-sheet-zagat-ratings'})
                    rating_clean = float(str(str(rating).split('<div class="zgt-place-sheet-zagat-rating-value h1-calibre">')[1].split('</div>')[0]).strip())
                except:
                    rating_clean=0
                # print(rating_clean)
                # exit()
                # try:
                #     zagat_rating = float(str(soup_internal.find('div', attrs={'class': 'zgt-place-sheet-zagat-ratings'}).text).strip())
                # except:
                #     zagat_rating = 2
                data_rating.append(rating_clean)

    return data_reataurant_name, data_address, data_rating


rest_name, address, rating = directory_file_fetch(dir)

# print(len(rating), len(rest_name), len(address))
# exit()

# ls_data = {'name': rest_name, 'address': address, 'rating': rating}

ls_data = dict()

ls_data['name'] = rest_name
ls_data['address'] = address
ls_data['rating'] = rating

df = pd.DataFrame(ls_data)

df.to_csv('data_zagat.csv', index=False)




# df.columns = ['name', 'address', 'rating']

df.to_csv('zagat_name.csv', index=False)

print(df)
