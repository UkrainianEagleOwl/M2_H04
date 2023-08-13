from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread
import urllib.parse
import mimetypes
import pathlib
import socket
import json
from datetime import datetime

BASE_DIR = pathlib.Path()

class CommonServer(BaseHTTPRequestHandler):
    def do_POST(self):
        data = self.rfile.read(int(self.headers["Content-Length"]))
        self.sed_data_via_socket(data.decode())
        self.send_response(200)
        self.send_header('Location', '/message')
        self.end_headers()

    def do_GET(self):
        return self.router()

    def send_html_file(self, filename, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open(filename, "rb") as fd:
            self.wfile.write(fd.read())

    def send_static(self, file):
        self.send_response(200)
        mt = mimetypes.guess_type(self.path)
        if mt:
            self.send_header("Content-type", mt[0])
        else:
            self.send_header("Content-type", "text/plain")
        self.end_headers()
        with open(file, "rb") as fd:  # ./assets/js/app.js
            self.wfile.write(fd.read())

    def router(self):
        pr_url = urllib.parse.urlparse(self.path)

        match pr_url.path:
            case "/":
                self.send_html_file("index.html")
            case "/message":
                self.send_html_file("message.html")
            case _:
                file = BASE_DIR.joinpath(pr_url.path[1:])
                if file.exists():
                    self.send_static(file)
                else:
                    self.send_html_file("error.html", 404)
                    
    def sed_data_via_socket(self, message):
        host = socket.gethostname()
        port = 5000

        client_socket = socket.socket()
        client_socket.connect((host, port))
        
        print(message)
        self.save_data_to_json(message)
        client_socket.close()
        self.send_html_file("message_succesfull.html")
        # while message.lower():
        #     client_socket.send(message.encode())
        #     data = client_socket.recv(1024).decode()
        #     print(f'received message: {data}')

        
        
    def save_data_to_json(self, data):
        data_parse = urllib.parse.unquote_plus(data)
        data_parse = {key: value for key, value in [el.split('=') for el in data_parse.split('&')]}
        save_message = {str(datetime.now()): data_parse}
        try:
            with open(BASE_DIR.joinpath('storage/data.json'), 'r') as fd:
                data_json = json.load(fd)
            data_json.update(save_message)
        except:
            data_json = save_message
        with open(BASE_DIR.joinpath('storage/data.json'), 'a', encoding='utf-8') as fd:
            json.dump(data_json, fd, ensure_ascii=False)

          
def server_socket():
    print('Socket start listening.')
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print(f'Connection from {address}')
    while True:
        data = conn.recv(100).decode()

        if not data:
            break
        print(f'received message: {data}')
    conn.close()   
    
def check_and_create_directories():
    storage_directory = BASE_DIR.joinpath('storage')
    data_file = BASE_DIR.joinpath('storage/data.json')

    if not storage_directory.is_dir():
        storage_directory.mkdir(parents=True)

    if not data_file.is_file():
        with open('storage/data.json', 'w', encoding='utf-8') as fd:
            json.dump({}, fd, ensure_ascii=False)



def run(server_class=HTTPServer, handler_class=CommonServer):
    check_and_create_directories()
    server_address = ("", 3000)
    http = server_class(server_address, handler_class)
    try:
        print("Start running")
        s_ser = Thread(target = server_socket)
        s_ser.start()
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()


if __name__ == "__main__":
    run()
