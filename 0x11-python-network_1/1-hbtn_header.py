#!/usr/bin/python3
"""A script that takes in a URL, sends a request and display the value
in the X-Request-Id variable found in the header"""

if __name__ == '__main__':
    import sys
    from  urllib.request import urlopen
    url = sys.argv[1]
    with urlopen(url) as res:
        url_res = res.info()
        print(url_res['X-Request-Id'])
