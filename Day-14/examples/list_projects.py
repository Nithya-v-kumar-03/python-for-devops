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
                                           //response.text is an attribute of that object. It returns the body of the HTTP response as a Unicode string (i.e. human-readable text). 
GeeksforGeeks
+1
name = output[0]["name"]

print(name)
---------------------------------------------------------------------------------
    import requests
from requests.auth import HTTPBasicAuth            # To authenticate Jira account — we are using requests.auth package
import json                                         # To work with JSON (parse response, etc.)
import requests — loads the Python Requests library, which makes it easy to send HTTP requests (GET, POST, etc.).

from requests.auth import HTTPBasicAuth — imports the class HTTPBasicAuth, used to send HTTP Basic Authentication credentials with your request. Basic auth is a simple authentication method where username (or email) + password (or API token) are encoded and sent in the Authorization header. 
docs.python-requests.org
+2
Delft Stack
+2

import json — imports Python’s built-in json module to work with JSON data (for example, converting JSON strings into Python dictionaries via json.loads, or converting dict → JSON string via json.dumps).

python
Copy code
url = "https://veeramallaabhishek.atlassian.net/rest/api/3/project"
This defines the endpoint URL of the JIRA REST API you want to call. Here you're using the API to get information about projects in the JIRA instance. The suffix /rest/api/3/project is part of JIRA Cloud’s REST API. 
Atlassian Support
+1

python
Copy code
API_TOKEN = ""    # api token >> Jira >> profile >> manage account >> security >> create API
This line is supposed to store your API token — a string generated from your Atlassian (JIRA) account. For JIRA Cloud, you typically don’t use a plain password; instead you generate an API token for authentication. The token replaces the “password” in Basic Auth. 
Atlassian Support
+1

You need to put your actual token (inside the quotes) for authentication to work.

python
Copy code
auth = HTTPBasicAuth("", API_TOKEN)  # give email of JIRA account
This creates an HTTP Basic Auth object: HTTPBasicAuth(username_or_email, password_or_token). In the case of JIRA Cloud, username_or_email is typically your Atlassian account email, and password_or_token is the API token. When you pass this auth object to Requests, it adds the correct Authorization: Basic ... header to your HTTP request. 
docs.python-requests.org
+2
NewTum API Test
+2

Important: you must supply your email (or Atlassian account identifier) — not leave it empty — otherwise authentication will fail.

python
Copy code
headers = {
  "Accept": "application/json"
}
This defines HTTP headers to send with your request. "Accept": "application/json" tells the server "I expect JSON in response". Since JIRA’s API returns JSON, this is appropriate and helps ensure you get JSON-formatted response.

python
Copy code
response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)
This sends an HTTP GET request to the specified url, with the given headers and auth.

Because you provided auth=auth, the request will include the Basic Authentication credentials (email + API token) in the Authorization header — so the JIRA server can verify you have permission to access projects. 
docs.python-requests.org
+1

The result is stored in response, a Response object from Requests. This object contains HTTP status code (response.status_code), response body (response.text or .json()), headers, etc.

python
Copy code
output = json.loads(response.text)  # to convert into dictionary we use json.loads
After getting the response, response.text returns the body content as a string. Since the JIRA API returns JSON, response.text should be a JSON-formatted string (if the request succeeded and the server returned JSON).

json.loads(...) parses that JSON string and returns an equivalent Python object — typically a dict (if the JSON was an object) or a list (if JSON was an array). From now on you can treat output like a normal Python dict/list.

Note: Alternatively, you could use response.json() (Requests offers it) — it does the same thing (parse JSON) but is a bit more convenient and handles edge cases.

python
Copy code
name = output[0]["name"]
print(name)
This tries to retrieve the "name" field from the first element of output. Implicitly, this means output is assumed to be a list (array) of projects, where each project is a dict with a "name" key.

output[0] — first project in the returned list.

["name"] — the “name” field of that project.

Then print(name) — prints the project name to standard output.

If the API returns multiple projects, this will only print the first one.
