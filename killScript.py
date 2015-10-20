__author__ = 'bcox, roconnor'

import urllib2
import json
import sys
from collections import defaultdict

baseUrl = 'https://api.groupme.com/v3/'
access_token = '?token=KZZMpZlBXr8b1Td0QTsHGLo7aIbPRWojZRHONX5L'
members = defaultdict(list)

def main(args):
    global group_name
    try:
        group_name = str(args[1])
        get_groups = urllib2.Request(baseUrl+'groups'+access_token, headers={'Content-type': 'application/json'})
        get_groups_resp = urllib2.urlopen(get_groups)
        old_group_id = getOldGroupId(json.load(get_groups_resp))
        get_members = urllib2.Request(baseUrl+'groups/'+old_group_id+access_token, headers={'Content-type': 'application/json'})
        get_members_resp = urllib2.urlopen(get_members)
        getMembers(json.load(get_members_resp))
        destroy = urllib2.Request(baseUrl+'groups/'+old_group_id+'/destroy'+access_token, data="", headers={'Content-type': 'application/json'})
        data = {
              "name": group_name,
              "share": True,
              "image_url": "http://i.groupme.com/123456789"
            }
        create = urllib2.Request(baseUrl+'groups'+access_token, data = json.dumps(data), headers={'Content-type': 'application/json'})
        destroy_resp = urllib2.urlopen(destroy)
        create_resp = urllib2.urlopen(create)
        id = getNewGroupId(json.load(create_resp))
        invite = urllib2.Request(baseUrl+'groups/'+id+'/members/add'+access_token, data=json.dumps(members), headers={'Content-type': 'application/json'})
        invite_resp = urllib2.urlopen(invite)

    except TypeError:
        print "Check your spelling, Julian"

def getOldGroupId(get_groups_resp):
    for x in get_groups_resp['response']:
        if x['name'] == group_name:
            return x['id']

def getMembers(get_members_resp):
    for x in get_members_resp['response']['members']:
        person = defaultdict(list)
        person['nickname'] = x['nickname']
        person['user_id'] = x['user_id']
        members['members'].append(person)

def getNewGroupId(create_resp):
    return create_resp['response']['id']

if __name__ == '__main__':
    main(sys.argv)

