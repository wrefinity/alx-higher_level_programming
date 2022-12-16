#!/usr/bin/python3
"""A script that  request a  URL and
displays the value of the variable X-Request-Id
in the response header"""

if __name__ == '__main__':
    import sys
    import requests
    try:
        response = requests.get(sys.argv[1])
        print(response.headers.get('X-Request-Id'))
    except Exception:
        pass
