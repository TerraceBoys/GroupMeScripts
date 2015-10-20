__author__ = 'bcox'

import urllib2
import json

baseUrl = 'https://api.groupme.com/v3/'
access_token = '?token=KZZMpZlBXr8b1Td0QTsHGLo7aIbPRWojZRHONX5L'

def main():
    req = urllib2.Request(baseUrl+'groups/17217125'+access_token, headers={'Content-type': 'application/json'})
    r = urllib2.urlopen(req)
    getMembers(json.load(r))

def getMembers(json):
    print json
    for x in range(len(json['response']['members'])):
        print json['response']['members'][x]

main()

