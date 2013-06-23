import http.cookiejar
import urllib.request, urllib.parse
import _settings

BASE_URI = 'http://fallenlondon.storynexus.com'

jar = http.cookiejar.CookieJar()
client = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))

def get(page, query):
    uri = BASE_URI + page
    data = urllib.parse.urlencode(query)
    with client.open(uri + '?' + data) as page:
        if page.getcode() != 200:
            raise Exception('GET failed: {0} {1}'.format(uri, query))
        return page.read().decode('utf-8')

def post(page, query):
    uri = BASE_URI + page
    data = urllib.parse.urlencode(query).encode('utf-8')
    with client.open(uri, data) as page:
        if page.getcode() != 200:
            raise Exception('POST failed: {0} {1}'.format(uri, query))
        return page.read().decode('utf-8')


post('/Auth/EmailLogin', {'emailAddress': _settings.AUTH_USER, 'password': _settings.AUTH_PASS})
print('Entered the Neath.')