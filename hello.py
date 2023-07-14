# import fire

# def hello(name="World"):
#   return "Hello %s!" % name

# if __name__ == '__main__':
#   fire.Fire(hello)

import http.server
import socketserver

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'''
            <html>
            <head>
                <title>My Custom Server</title>
            </head>
            <body>
                <h1>Welcome to My Custom Server!</h1>
                <p>This is a simple HTTP server.</p>
            </body>
            </html>
        ''')

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("Server started on port", PORT)
    httpd.serve_forever()
