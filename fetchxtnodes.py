#!/usr/bin/python

import urllib2
import json

url = "https://getaddr.bitnodes.io/api/v1/snapshots/latest/"

data = urllib2.urlopen(url).read()
data = json.loads(data)['nodes']

for node  in data.items():
    if ("Bitcoin XT" in node[1][1]) and ("[" not in node[0]):
        print node[0].split(":")[0]
