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
#    pdb.set_trace()
    print(glob.glob('*.{}'.format(extension)))
    
    #all_filenames = ['breweries'+i+'.csv' for i in constant.states.keys()]
    #combine all files in the list
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ], sort=False)
#    combined_csv.drop(['Link'], axis=1,inplace=True)
#    export to csv
    '''encoding = ‘utf-8-sig’ is added to overcome the issue when exporting ‘Non-English’ languages.'''
    combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
    

'''Request url'''    
def get_general_html(url,cookie=None, returnJson=None):
    import requests
#    import browsercookie
#    import browser_cookie3
    from requests.auth import HTTPBasicAuth
    
    '''
    封装请求
    '''
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Cache-Control': 'no-cache',
        "Pragma": "no-cache",
#        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36',
#        'Referer': 'https://www.ratebeer.com/',
#        'Sec-Fetch-Dest': 'document',
#        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#        'cookie':'__cfduid=d2360bf242830ca67ffd6f63b24470e0e1584457916; OptanonAlertBoxClosed=2020-03-17T15:46:33.375Z; OptanonConsent=isIABGlobal=false&datestamp=Tue+Mar+17+2020+10%3A46%3A33+GMT-0500+(%E5%8C%97%E7%BE%8E%E4%B8%AD%E9%83%A8%E5%A4%8F%E4%BB%A4%E6%97%B6%E9%97%B4)&version=5.7.0&landingPath=NotLandingPage&groups=1%3A1%2C2%3A1%2C3%3A1%2C4%3A1%2C0_223362%3A1%2C0_223376%3A1%2C0_223377%3A1%2C0_223375%3A1%2C0_223352%3A1%2C0_223353%3A1%2C0_223351%3A1%2C0_223360%3A1%2C0_223361%3A1%2C0_223358%3A1%2C0_223359%3A1%2C0_223356%3A1%2C0_223357%3A1%2C0_223354%3A1%2C0_223355%3A1&AwaitingReconsent=false',
#        '__cfduid=d95896e149fb4dc7048bb7dc3fc30f9861576607394; xf_user=1284121%2C96e54c148af23da29089bba8910561a8c89b6a90; xf_session=511de6204544d8a81648fcd3e16460cd',
#        'authority': 
#        'www.beeradvocate.com'
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
#        cookie_obj = requests.cookies.create_cookie(domain='www.ratebeer.com',name='COOKIE_NAME',value='the cookie works')
#        session_requests.cookies.set_cookie(cookie_obj)
#        cookies = browser_cookie3.firefox(domain_name='.ratebeer.com')
#        cookie = {'version':'0', name='_gid', value='GA1.2.1596360130.1584462568', port=None, port_specified=False, domain='.ratebeer.com', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=0, expires=1584548968, discard=False, comment=None, comment_url=None, rest={}, rfc2109=False}
#        htmlcontet = session_requests.get(url, cookies = cookies, headers=headers,  timeout=30)   # auth = HTTPBasicAuth('Jerryzzz','URduI79Ck%iqDcx'),
        htmlcontent = session_requests.get(url, headers=headers,  timeout=30)
        if returnJson == True:
            return htmlcontent.json()
        else:
            htmlcontent.raise_for_status()
            htmlcontent.encoding = 'utf-8'
            return htmlcontent.text
    except Exception as e:
        print(str(e))
        return " Request Failure "
    
'''Request url, only for beeradvocate with session ID'''    
def get_html(url):
    import requests
    '''
    封装请求
    '''
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36',
        'cookie':
#        '__cfduid=d95896e149fb4dc7048bb7dc3fc30f9861576607394; xf_user=1284121%2C96e54c148af23da29089bba8910561a8c89b6a90; xf_session=511de6204544d8a81648fcd3e16460cd',
#        '_ga=GA1.3.307185451.1578070313; __gads=ID=c5edf6e044c40358:T=1578070314:S=ALNI_Maj2RSpH9A4RzlGRPmwtlgjrMH6Ew; __cfduid=dea7dbaa16d5a0df3a931fa0f266a20d71582845290; _gid=GA1.3.270839865.1583531993; AdvallyUserLocation=US,TX; hideRatings=N; xf_session=af65a8b3e651b61467ee202d0a4e60a1',
        '_ga=GA1.3.838867706.1577533683; __cfduid=d76e511076637f9ef002bd80d6c7fd21e1582548059; hideRatings=N; xf_user=1284121%2C96e54c148af23da29089bba8910561a8c89b6a90; xf_session=5f3a590654e7e6f4e056fc89cbb515e6',
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

def tranferMongo():
    from pymongo import MongoClient
    client = MongoClient("mongodb+srv://dbuser:8fO56qa3wBdNYtsk@cluster0-bhgly.mongodb.net/rateBeer?retryWrites=true&w=majority")
    db = client.rateBeer
    collection = db['beers']
    data = collection.find()
    client_local = MongoClient()
    db_local = client_local.rateBeer
    coll_local = db_local['beers']
    coll_local.insert(data)

if __name__ == "__main__":  
    print(generatePassword(15))