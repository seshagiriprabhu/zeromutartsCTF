import urllib.error
import urllib.request

# set up authentication info
auth_handler = urllib.request.HTTPBasicAuthHandler()
auth_handler.add_password(realm=None,
        uri=r'http://zeromutarts.de/',
        user='blob',
        passwd='april121991?')
opener =  urllib.request.build_opener(auth_handler)
urllib.request.install_opener(opener)
try:
    res = opener.open(r'http://zeromutarts.de/task/noise')
    nodes = res.read()
except urllib.error.HTTPError as e:
    print(e.headers['www-authenticate'])
