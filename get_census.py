# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 15:40:46 2022

@author: qzhu
"""

import requests,csv

year='2020'
dsource='dec' # the survey i.e. decennial census, acs, etc
dseries='pl' # a dataset within the survey
cols='NAME,P1_001N' # census variables - total population
state='06' #'44' # ansi fips codes for states; use asterisk * for all states
place= '*' #'19180,54640,59000,74300' # ansi fips codes cities / towns; use asterisk * for all places
county = '*'
outfile='census_pop2020.csv'
# keyfile='census_key.txt'

# with open(keyfile) as key:
# 	api_key=key.read().strip()
api_key = 'e76b3223547faa2bf0198c7abd52dd572f4da9bd'

base_url = f'https://api.census.gov/data/{year}/{dsource}/{dseries}'

# for sub-geography within larger geography - geographies must nest
# data_url = f'{base_url}?get={cols}&for=place:{place}&in=state:{state}&key={api_key}'
data_url = f'{base_url}?get={cols}&for=county:{county}&in=state:{state}&key={api_key}'

response=requests.get(data_url)