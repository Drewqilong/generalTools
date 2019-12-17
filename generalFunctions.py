# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:46:10 2019

@author: Jerry
"""
import pandas as pd

def exportCSV(data):
    submit = pd.DataFrame(data)
    submit.to_csv('submission.csv',index=False)
    
def generatePassword(length):
    import secrets
    import string
    alphabet = string.ascii_letters + string.digits + '!@#$%^&*()'
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

print(generatePassword(15))