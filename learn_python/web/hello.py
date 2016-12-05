signin = '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

def application(environ, start_response):
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    print method, path
    if method == 'POST' and path == '/signin':
        print "111"
    start_response('200 OK', [('Content-Type', 'text/html')])
    return signin
