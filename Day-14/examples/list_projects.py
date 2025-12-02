# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth            //To authenticate jira account & we are using request.auth package
import json                                        //as we are using json 

url = "https://veeramallaabhishek.atlassian.net/rest/api/3/project"

API_TOKEN=""                                                     //api token>>jira>>profile>>manage account>>security>>create API

auth = HTTPBasicAuth("", API_TOKEN)                            //give email of jira account

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)               //to convert into dictionary we use json.loads

name = output[0]["name"]

print(name)
