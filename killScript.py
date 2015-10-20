__author__ = 'bcox, roconnor'

import urllib2
import json

baseUrl = 'https://api.groupme.com/v3/'
access_token = '?token=KZZMpZlBXr8b1Td0QTsHGLo7aIbPRWojZRHONX5L'

def main():

    req = urllib2.Request('baseUrl'+'groups/'+access_token, data="", headers={'Content-type': 'application/json'})
    r = urllib2.urlopen(req)
    print r

main()

