#search the terms related to views

import urllib
import urllib.request
import json
url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&"
searchterm = 'Golden Gate'
helpterm = 'San Francisco'
query = searchterm + helpterm
query = urllib.parse.urlencode( {'q' : query } )
response = urllib.request.urlopen (url + query ).read()
print(response)
data = json.loads ( response.decode() )
results = data [ 'responseData' ] [ 'results' ]
print("data")
for result in results:
    title = result['title']
    url = result['url']
    print ( title + '; ' + url )