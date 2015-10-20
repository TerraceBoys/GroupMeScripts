__author__ = 'bcox, roconnor'

import urllib2
import json
from collections import defaultdict

baseUrl = 'https://api.groupme.com/v3/'
groupId = '17306682'

access_token = '?token=KZZMpZlBXr8b1Td0QTsHGLo7aIbPRWojZRHONX5L'
#members = list()

def main():
    get = urllib2.Request(baseUrl+'groups/'+groupId+access_token, headers={'Content-type': 'application/json'})
    get_resp = urllib2.urlopen(get)
    #getMembers(json.load(get_resp))
    members = getMembers2(json.load(get_resp))
    print members
    #destroy = urllib2.Request(baseUrl+'groups/'+groupId+'/destroy'+access_token, data="", headers={'Content-type': 'application/json'})
    data = {
          "name": "TestingRebornAgain",
          "share": True,
          "image_url": "http://i.groupme.com/123456789"
        }
    create = urllib2.Request(baseUrl+'groups'+access_token, data = json.dumps(data), headers={'Content-type': 'application/json'})

    #destroy_resp = urllib2.urlopen(destroy)
    create_resp = urllib2.urlopen(create)

    id = getNewGroupId(json.load(create_resp))

    #print members
    #member_data = json.dumps(dict(members))
    invite_url = baseUrl+'groups/'+id+'/members/add'+access_token
    print invite_url
    print json.dumps(members[0])
    invite = urllib2.Request(baseUrl+'groups/'+id+'/members/add'+access_token, data=json.dumps(members[0]), headers={'Content-type': 'application/json'})

    invite_resp = urllib2.urlopen(invite)



def getMembers(get_resp):
    for x in get_resp['response']['members']:
        person = (x['nickname'], x['user_id'])
        members.append(person)
    for z in members:
        print z

def getMembers2(get_resp):
    return get_resp['response']['members']

def getNewGroupId(create_resp):
    return create_resp['response']['id']

main()

