from thor import Thor

host = "0.0.0.0"
port = 80
thor = Thor(host, port, '/htdocs')

@thor.route('/')
def home():
    return 'WeB SeRvEr Is LiVe....'

thor.run()