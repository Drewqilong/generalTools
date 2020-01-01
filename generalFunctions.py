# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:46:10 2019

@author: Jerry
"""
import pandas as pd
from pymongo import MongoClient

#def exportCSV(data):
#    submit = pd.DataFrame(data)
#    submit.to_csv('submission.csv',index=False)
    
def generatePassword(length):
    import secrets
    import string
    alphabet = string.ascii_letters + string.digits + '!@#$%^&*()'
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

def exportExcel(goods_table):
    import exportexcel
    if len(goods_table) > 1:  
        exportexcel.write_excel(goods_table, 'demo.xls')
        print('download data success!')
    
def exportCSV(data,filename,filePath='',mode='w',header=True):
    l_file = filename
    from os import path,makedirs
    if filePath:
        if not path.exists(filePath):
            makedirs(filePath)
        l_file = path.join(filePath,filename)
    df_data = pd.DataFrame(data)
    df_data.to_csv(l_file,index=False, encoding='utf-8-sig',mode=mode,header=header)
    
def combineCSV(path):
    import pandas as pd
#data = pd.read_csv('breweries_Companines.csv')
#print(data.iloc[491])

    import os
    import glob
    
    
    os.chdir(path)
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    
    print(glob.glob('*.{}'.format(extension)))
    
    #all_filenames = ['breweries'+i+'.csv' for i in constant.states.keys()]
    #combine all files in the list
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ], sort=False)
    #export to csv
    '''encoding = ‘utf-8-sig’ is added to overcome the issue when exporting ‘Non-English’ languages.'''
    combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
    
'''Request url'''    
def get_html(url):
    import requests
    '''
    封装请求
    '''
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36',
        'cookie':
        '__cfduid=d95896e149fb4dc7048bb7dc3fc30f9861576607394; xf_user=1284121%2C96e54c148af23da29089bba8910561a8c89b6a90; xf_session=511de6204544d8a81648fcd3e16460cd',
        'authority': 
        'www.beeradvocate.com'
#        'ContentType':
#        'text/html; charset=utf-8',
#        'Accept-Encoding':
#        'gzip, deflate, br',
#        'Accept-Language':
#        'zh-CN,zh;q=0.9,en;q=0.8',
#        'Connection':
#        'keep-alive',
    }
    try:
        session_requests = requests.session()
        htmlcontet = session_requests.get(url, headers=headers, timeout=30)
        htmlcontet.raise_for_status()
        htmlcontet.encoding = 'utf-8'
        return htmlcontet.text
    except:
        return " Request Failure "
    
def insertMongo(data,database,collection):
    
    client = MongoClient()
    db = client[database]
    collection = db[collection]
    collection.insert_many(data)

def removeMongo(query,database,collection):
    client = MongoClient()
    db = client[database]
    collection = db[collection]
    if not query:
        collection.delete_many({})

if __name__ == "__main__":  
    print(generatePassword(15))