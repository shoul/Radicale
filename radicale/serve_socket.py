

def serve_socket(environ, start_response):

    start_response('200 OK', [('Content-Type', 'text/html')])
    return ('''<html>
<head>
<title>Hello World!</title>
</head>
<body>
<h1>Hello world!</h1>
</body>
2
Apache, FastCGI and Python
</html>''')