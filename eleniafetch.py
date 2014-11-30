#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
LOGIN_URL="https://minunsivuni.elenia.fi/main/default.asp"

class EleniaFetch:
    auth = None
    def __init__(user, password):
        auth = self.login(user, password)
        
    def login(self, user, password):
    """
    Returns authorization cookie
    """
    pass
    
    #def getImgUrl(
    
if __name__ = '__main__':
    elenia = EleniaFetch()