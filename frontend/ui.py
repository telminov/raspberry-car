# coding: utf-8
import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("0.0.0.0", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()