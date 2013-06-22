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
    return post(page, data)

def get(uri, query):
    data = urllib.parse.urlencode(query)
    uri = uri + '?' + data
    with client.open(uri) as page:
        if page.getcode() != 200:
            raise Exception('Request failed: {0} {1}'.format(uri, query))
        return page.read().decode('utf-8')

def post(page, query):
    uri = BASE_URI + page
    data = urllib.parse.urlencode(query).encode('utf-8')
    with client.open(uri, data) as page:
        if page.getcode() != 200:
            raise Exception('Request failed: {0} {1}'.format(uri, query))
        return page.read().decode('utf-8')

print('Entering the Neath')
post('/Auth/EmailLogin', {'emailAddress': _settings.AUTH_USER, 'password': _settings.AUTH_PASS})