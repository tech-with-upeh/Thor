import socket
from user_agents import parse
import datetime
import pytz

class Thor:
    def __init__(self, ip, port, path):
        self.ip = ip
        self.port = port
        self.path= path
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((ip, port))
        self.url = {}
        self.url_args = {}
    
    def route(self, route, method=[]):
        def inner(func):
            def inner_f(*args):
                self.url[route] = func
                self.url_args[route] = str(*args)
                return func
            self.url[route] = inner_f
            return inner_f
        return inner
        
        
    def handle_request(self, conn, addr, req):
        req_data = req.decode('utf-8').splitlines()
        hreq = req_data[0]
        del req_data[0]
        method = hreq.split()[0]
        req_loc = hreq.split()[1]
        status_code = 200
        headers = f'HTTP/1.0 200 OK\nDate: {str(datetime.datetime.now(pytz.timezone("UTC")))[:-13]}\nServer: Thor/1.0.0 \nContent-Type: text/html; charset=utf-8'
        if req_loc in self.url:
            self.url[req_loc]()
            if self.url_args[req_loc]:
                print(self.url[req_loc](self.url_args[req_loc]))
                resp = f'\n\n{self.url[req_loc](self.url_args[req_loc])}'
            else:
                print(self.url[req_loc]())
                resp = f'\n\n{self.url[req_loc]()}'
            status_code = 200
        else:
            resp = '\n\nError Page not found'
            status_code = 404
        response = headers + '\nContent-Length: ' +str(len(resp[2::].encode())) + resp
        conn.sendall(response.encode())
        print(f'{method} {req_loc} {status_code}')
        conn.close()

    def run(self):
        self.sock.listen()
        print(f"[RUNNING: Thor Server on {self.ip}:{self.port} ]")
        while True:
            conn, addr = self.sock.accept()
            try:
                req = conn.recv(1024)
                self.handle_request(conn, addr[0], req)
            except:
                conn.close()
        self.sock.close()

   
