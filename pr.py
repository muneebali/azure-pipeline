import requests
import os

class Message():
    '''Instance of a message
    Source: https://stackoverflow.com/a/60049855
    '''

    def __init__(self):
        SYSTEM_COLLECTIONURI = os.getenv('SYSTEM_COLLECTIONURI')
        SYSTEM_PULLREQUEST_PULLREQUESTID = os.getenv('SYSTEM_PULLREQUEST_PULLREQUESTID')
        SYSTEM_TEAMPROJECT = os.getenv('SYSTEM_TEAMPROJECT')
        BUILD_REPOSITORY_ID = os.getenv('BUILD_REPOSITORY_ID')
        self.url = f"{SYSTEM_COLLECTIONURI}{SYSTEM_TEAMPROJECT}/_apis/git/repositories/" \
                   f"{BUILD_REPOSITORY_ID}/pullRequests/{SYSTEM_PULLREQUEST_PULLREQUESTID}" \
                   "/threads?api-version=6.0"
        self.headers = {
            "content-type": "application/json",
            "Authorization": f"BEARER {os.getenv('SYSTEM_ACCESSTOKEN')}"
        }

    def add(self, comment: str) -> bool:
        ''' Add a message to Azure DevOps Pull Request'''
        data = {
            "comments": [
                {
                    "parentCommentId": 0,
                    "content": comment,
                    "commentType": 1
                }
            ],
            "status": 1
        }

        print(f"URL: {self.url}")
        print(f"headers: {self.headers}")
        r = requests.post(url=self.url, json=data, headers=self.headers)
        if r.status_code == 200:
            return True
        else:
            return False
