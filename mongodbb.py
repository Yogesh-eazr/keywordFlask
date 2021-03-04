import pymongo
from flask import Flask, jsonify, request

conn = pymongo.MongoClient('localhost', 27017)
db = conn['KEYWORDS']
t = db.keyword_list

app = Flask(__name__)

# @app.route("/keyword", methods = ['POST'])
# def postkeyword():
#     data = re quest.get_json()
#     category = data["category"]
#     # collection.find({},{category:"one"}).pretty();
#     table = t.find()
#     key_list = []
#     for i in table:
#         key_list.append(i[f'{category}'])
#     return jsonify({"list": key_list})

#### updating a mongodb using flask

newkey_list = []

@app.route("/keywordupdate", methods = ['POST'])
def mongoupdate():
    data = request.get_json()
    add_data = data["add_keyword"]
    table_1 = t.find()
    for i in table_1:
        db_data = i['one']
        for j in db_data:
            newkey_list.append(j)
    for i in add_data:
        newkey_list.append(i)
    t.update_one({"_id": "60409f0ee2d665843ceac7a9"}, {'$set': {"one": newkey_list}})
    return jsonify({"new keys list ": newkey_list})


@app.route("/keyword", methods = ['GET'])
def postkeyword():
    table = t.find()
    key_list = []
    for i in table:
        key_list.append(i['one'])
    return jsonify({"list": key_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=8080)

import openpyxl
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
# df = pd.read_excel('Header_2021_Jan_F2_og.xlsx',header = 1)
# print(df.head())
#
# a = df['Purpose of the header']
# b = df['Header']
#
# dictt = {}
# count = 0
#
# for k,v in zip(b,a):
#     dictt[k]=v
#     count += 1
#     print(count)

from bson.json_util import dumps

import json

# with open('data_newest.json', 'w') as fp:
#     json.dump(dictt, fp)
#
# conn = pymongo.MongoClient('localhost',27017)
# db = conn['mydata']

# keyword_list = ['CR', 'CREDIT', 'DEBIT']
# keyword_dict = {}
#
# # for i in range(len(keyword_list)):
# keyword_dict['one'] = keyword_list
#
# print(keyword_dict)
#
# # below code creates a table
# collection = db['keyword_list']

# for i in range(len(keyword_list)):
# collection.insert(keyword_dict)
# collection.insert_one(dumps({"keyword": keyword_list[i]}))

# collection.insert(dictt)
