#coding=utf-8
import http.client
import urllib
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from 检测 import process_data


def start_server(host, dg):
    class Resquest(BaseHTTPRequestHandler):
        def do_GET(self):
            data={"Method:":self.command,
                  "Path:":self.path}
            print(data)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        # 使用post请求方法
        def do_POST(self):
            length = int(self.headers['Content-Length'])
            post_data = urllib.parse.parse_qs(self.rfile.read(length).decode('utf-8'))
            # You now have a dictionary of the post data
            data = {"Method:": self.command,
                    "Path:": self.path,
                    "Post Data":post_data}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps("received").encode())
            process_data(data["Post Data"], dg)
        def do_HEAD(self):
            data = {"Method:": self.command,
                    "Path:": self.path,
                    "Header Content-type": self.headers.get('Content-type')}
            print(data)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            self.wfile.write(json.dumps(data).encode())
        def do_PUT(self):
            data = {"Method:": self.command,
                    "Path:": self.path,
                    "Header Content-type": self.headers.get('Content-type')}
            print(data)
            path = self.path
            content_length = int(self.headers.get('content-length'))
            content = self.rfile.read(content_length)
            #safe_mkdir(os.path.dirname(path))
            with open("D:/code/pyhttp/put_datas.txt", 'ab') as outfile:
                outfile.write(content)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()


if __name__ == '__main__':
    start_server()
    print("start server success...")
