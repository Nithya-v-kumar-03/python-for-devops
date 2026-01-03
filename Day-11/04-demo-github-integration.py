# Program to demonstrate integration with GitHub to fetch the 
# details of Users who created Pull requests(Active) on Kubernetes Github repo.

import requests   #to handle API we use request

# URL to fetch pull requests from the GitHub API>>Pull requests>>pull request
url = f'https://api.github.com/repos/kubernetes/kubernetes/pulls'

# Make a GET request to fetch pull requests data from the GitHub API
response = requests.get(url)  # Add headers=headers inside get() for authentication

# Only if the response is successful
if response.status_code == 200:
    # Convert the JSON response to a dictionary
    pull_requests = response.json()

    # Create an empty dictionary to store PR creators and their counts
    pr_creators = {}

    # Iterate through each pull request and extract the creator's name
    for pull in pull_requests:
        creator = pull['user']['login']
        if creator in pr_creators:
            pr_creators[creator] += 1        #If the creator is already in pr_creators, increment their count; otherwise add them with count 1.
        else:
            pr_creators[creator] = 1

    # Display the dictionary of PR creators and their counts
    print("PR Creators and Counts:")
    for creator, count in pr_creators.items():
        print(f"{creator}: {count} PR(s)")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
----------------------------------------------------------------------------------------------
Line 1–2 (comments)
# Program to demonstrate integration with GitHub to fetch the 
# details of Users who created Pull requests(Active) on Kubernetes Github repo.


These are comments

Python ignores them

Used only for human understanding

🟢 Importing module
Line 4
import requests


Python loads the requests library into memory

This library allows Python to make HTTP requests (GET, POST, etc.)

Program continues

🟢 URL definition
Line 7
url = f'https://api.github.com/repos/kubernetes/kubernetes/pulls'


A string URL is created

This URL points to:

GitHub API

Kubernetes repository

Active pull requests

Stored in variable url

🟢 Sending HTTP request
Line 10
response = requests.get(url)


Python sends a GET request to GitHub’s server

GitHub processes the request

GitHub sends back a response

Response is stored in response

At this point:

No data is printed yet

response contains:

status code

headers

response body (JSON)

🟢 Checking response status
Line 13
if response.status_code == 200:


Python checks the HTTP status code

200 means request was successful

If True, execution enters the if block

(If it were not 200, Python would skip to the else block)

🟢 Converting response data
Line 15
pull_requests = response.json()


GitHub sends data in JSON format

.json() converts JSON → Python data structure

pull_requests becomes a list of dictionaries

Each dictionary represents one pull request

🟢 Creating empty dictionary
Line 18
pr_creators = {}


Creates an empty dictionary

This will store:

{
  "username": number_of_PRs
}

🟢 Looping through pull requests
Line 21
for pull in pull_requests:


Loop starts

pull represents one pull request at a time

Loop repeats for each PR in the list

🟢 Extracting PR creator
Line 22
creator = pull['user']['login']


pull is a dictionary

pull['user'] → dictionary of user info

pull['user']['login'] → GitHub username

Username is stored in creator

Example:

creator = "alice123"

🟢 Counting pull requests
Line 23
if creator in pr_creators:


Python checks:

Is this username already in the dictionary?

Line 24 (if True)
pr_creators[creator] += 1


Username already exists

Increase PR count by 1

Line 26 (if False)
else:
    pr_creators[creator] = 1


Username does not exist

Add it to dictionary with count 1

🟢 Loop continues

Steps 21–26 repeat for every pull request

Dictionary fills up like:

{
  "alice123": 3,
  "bob_dev": 1,
  "charlie99": 2
}

🟢 Printing results
Line 29
print("PR Creators and Counts:")


Prints a heading

Line 30
for creator, count in pr_creators.items():


Loop through dictionary

Each iteration gives:

creator → username

count → number of PRs

Line 31
print(f"{creator}: {count} PR(s)")


Prints each user and their PR count

Example output:

alice123: 3 PR(s)
bob_dev: 1 PR(s)

🟢 If request failed
Line 33–34
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")


Runs only if status code is NOT 200

Prints error message with HTTP status code

Example:

Failed to fetch data. Status code: 403
