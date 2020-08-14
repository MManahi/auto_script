# import required modules
import os
import sys
import pandas as pd
from bs4 import BeautifulSoup
import random

# define absolute path
path = 'data/index.html'

# initialize empty data list
data = []

# get the header data
list_header = []
soup = BeautifulSoup(open(path), 'html.parser')
header = soup.find_all("table")[3].find("tr")

for items in header:
    try:
        list_header.append(items.get_text())
    except:
        continue

# get the html data
HTML_data = soup.find_all("table")[3].find_all("tr")[1:]
pairwise_list = []
for element in HTML_data:
    sub_data = []
    for sub_element in element:
        try:
            sub_data.append(sub_element.get_text())
        except:
            continue

    del sub_data[1]
    #print(sub_data)
    if len(sub_data) > 2:
        #print(sub_data)
        for i in range(1, len(sub_data)):
            #print(sub_data[0], sub_data[i])
            score = sub_data[i].split('(')
            similarity = score[1].replace('%)', '')
            data.append([sub_data[0], score[0], 1])

    else:
        score = sub_data[1].split('(')
        similarity = score[1].replace('%)', '')
        data.append([sub_data[0], score[0], 1])
    #data.append(sub_data)
#print(data)
for i in range(0, 199):
    # for exculsion_data in sub_data:
    # var = exculsion_data.split('-')[1].split('.')[0]
    # exclusion.append(var)
    # random_num = random.randint(0,499)
    # print(random_num)
    inclusion = []
    inclusion_a = 'ps20-' + str(random.randint(0, 499)) + '.cpp'
    inclusion_b = 'ps20-' + str(random.randint(0, 499)) + '.cpp'
    if inclusion not in data:
        inclusion = inclusion.append([inclusion_a, inclusion_b, 0])
    all_data = [data, inclusion]
# store the data into dataframe
dataFrame = pd.DataFrame(data=all_data)

# convert the dataframe into csv
dataFrame.to_csv('result.csv', index= False)