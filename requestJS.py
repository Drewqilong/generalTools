# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:01:41 2020

@author: Jerry
"""

url="https://www.ratebeer.com/brewers/avondale-brewing-company/12890/"

#import asyncio
#if asyncio.get_event_loop().is_running(): # Only patch if needed (i.e. running in Notebook, Spyder, etc)
#    import nest_asyncio
#    nest_asyncio.apply()
#
#from requests_html import HTMLSession
#session = HTMLSession()
#r = session.get('https://pythonclock.org')
#r.html.render()


import asyncio
if asyncio.get_event_loop().is_running(): # Only patch if needed (i.e. running in Notebook, Spyder, etc)
    import nest_asyncio
    nest_asyncio.apply()
    
from requests_html import HTMLSession,AsyncHTMLSession

#asession = AsyncHTMLSession()
#
#async def get_pyclock():
#    
#    r = await asession.get('https://pythonclock.org/')
#    await r.html.arender()
#    return r
#
#results = asession.run(get_pyclock)

asession = AsyncHTMLSession()

async def get_pyclock():
    r = await asession.get('https://pythonclock.org/')
    await r.html.arender()
    return r
resp= asession.run(get_pyclock)

#r = session.get(url)
#
#r.html.render()  # this call executes the js in the page

#async def get_results():
#    r = await asession.get('http://python-requests.org')
#    return r
##
#a = asession.run(get_results)
#print(a[0].html.search('Python 2 will retire in only {months} months!'))

#import requests_html
#with requests_html.HTMLSession() as session:
#    r = session.get('https://www.ratebeer.com/brewers/')
#    js = r.html.render()
#    item = js.find('.MarketInfo_market-num_1lAXs',first=True).text
#    print(item)