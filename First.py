__author__ = 'shawnmehan'

import urllib2, json


key = ""

school=['cal%20poly','harvard%20university']
opedids=['00114300']
city = "Boston"
for item in school:
    url='https://api.data.gov/ed/collegescorecard/v1/schools?school.name='+item+'&api_key='+key
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    response2 = response.read()
    json_data=json.loads(response2)
    #print json_data
    for series in json_data['results']:
        unitid=str(series['ope6_id'])
        lines=unitid+"/n"
        output=open('api_test.txt','a')
        print(lines)
        output.write(lines)
        output.close()

for id in opedids:
    url='https://api.data.gov/ed/collegescorecard/v1/schools?school.ope8_id='+id+'&api_key='+key
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    response2 = response.read()
    json_data=json.loads(response2)
    for s in json_data['results']:
        print s