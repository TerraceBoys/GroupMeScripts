__author__ = 'bcox'

import urllib
import json

baseUrl = 'https://api.groupme.com/v3/'
access_token = '?token=KZZMpZlBXr8b1Td0QTsHGLo7aIbPRWojZRHONX5L'

def main():
    resp = urllib.urlopen(baseUrl+'groups/'+access_token)
    resp.a
    resp_data = json.loads(resp.read().decode())
    print resp_data

main()

