import http.cookiejar
import urllib.request, urllib.parse

BASE_URI = 'http://fallenlondon.storynexus.com'

class Browser:
    def __init__(self):
        self.jar = http.cookiejar.CookieJar()
        self.client = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.jar))

    def get(self, page, query):
        uri = BASE_URI + page
        data = urllib.parse.urlencode(query)
        with self.client.open(uri + '?' + data) as page:
            if page.getcode() != 200:
                raise Exception('GET failed: {0} {1}'.format(uri, query))
            return page.read().decode('utf-8')

    def post(self, page, query):
        uri = BASE_URI + page
        data = urllib.parse.urlencode(query).encode('utf-8')
        with self.client.open(uri, data) as page:
            if page.getcode() != 200:
                raise Exception('POST failed: {0} {1}'.format(uri, query))
            return page.read().decode('utf-8')


