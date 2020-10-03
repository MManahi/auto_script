# import required modules
import os
import sys
import pandas as pd
from bs4 import BeautifulSoup
from random import choice, randint
import csv

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
HTML_data = soup.find_all("table")[3].find_all("tr")[0:]
pairwise_list = []
similarity_files = []
for element in HTML_data:
    sub_data = []
    for sub_element in element:
        try:
            sub_data.append(sub_element.get_text())
        except:
            continue

    del sub_data[1]
    # print(sub_data)
    if len(sub_data) > 2:
        # print(sub_data)
        for i in range(1, len(sub_data)):
            # print(sub_data[0], sub_data[i])
            source_code_a = sub_data[0]
            source_code_b = sub_data[i].split('(')
            similarity = source_code_b[1].replace('%)', '')
            data.append([source_code_a, source_code_b[0], 1])
            similarity_files.append(sub_data[0])
            similarity_files.append(source_code_b[0])
            # print(sub_data[0], source_code_b[0])

    else:
        source_code_a = sub_data[0]
        source_code_b = sub_data[1].split('(')
        similarity = source_code_b[1].replace('%)', '')
        data.append([source_code_a, source_code_b[0], 1])
        # print(sub_data[0], source_code_b[0])
        similarity_files.append(sub_data[0])
        similarity_files.append(source_code_b[0])

similarity_files = list(dict.fromkeys(similarity_files))

all_files = []
dissimilarity_files = []
for i in range(0, 499):
    file_name = 'ps20-' + str(i) + '.cpp'
    all_files.append(file_name)

dissimilarity_files = [x for x in all_files if (x not in similarity_files)]

# print(len(all_files), all_files)
# print(len(similarity_files), similarity_files)
# print(len(dissimilarity_files), dissimilarity_files)
data_dis = []
for a in dissimilarity_files:
        b = randint(0, len(dissimilarity_files) - 1)
        if a != dissimilarity_files[b]:
            # print(a, dissimilarity_files[b], 0)
            data_dis.append([a, dissimilarity_files[b], 0])

all_data = data + data_dis

# store the data into dataframe
dataFrame = pd.DataFrame(data=all_data)

# convert the dataframe into csv
dataFrame.to_csv('result.csv', index=False)
