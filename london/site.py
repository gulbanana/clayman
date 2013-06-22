import http.cookiejar
import urllib.request, urllib.parse
import _settings

BASE_URI = 'http://fallenlondon.storynexus.com'

jar = http.cookiejar.CookieJar()
client = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))

def command(page, data):
    #uri = BASE_URI + page
    #inner = urllib.parse.urlencode(data)
    #get('/Gap/Load', {'content': page + '?' + inner})
    post(page, data)

def get(uri, query):
    data = urllib.parse.urlencode(query)
    uri = uri + '?' + data
    print(uri)
    page = client.open(uri)
    if page.getcode() != 200:
        raise Exception('Request failed')

def post(page, query):
    uri = BASE_URI + page
    print(uri)
    data = urllib.parse.urlencode(query).encode('utf-8')
    page = client.open(uri, data)
    if page.getcode() != 200:
        raise Exception('Request failed')

print('Entering the Neath')
post('/Auth/EmailLogin', {'emailAddress': _settings.AUTH_USER, 'password': _settings.AUTH_PASS})