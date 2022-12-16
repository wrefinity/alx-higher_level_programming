#!/usr/bin/python3
"""Take GitHub credentials (username and password) as arguments
and uses the GitHub API to display users id"""

if __name__ == '__main__':
    import sys
    from requests import get
    from requests.auth import HTTPBasicAuth

    url = "https://api.github.com/user"
    response = get(
        url, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    res_dict = response.json()
    print(res_dict.get('id'))
