import sys
import http.server
import socketserver

PORT = 8000


class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        http.server.SimpleHTTPRequestHandler.end_headers(self)


def server(port):
    httpd = socketserver.TCPServer(('', port), HTTPRequestHandler)
    return httpd


if __name__ == "__main__":
    port = PORT
    httpd = server(port)
    try:
        print("Serving at localhost:" + str(port))
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down http server")
        httpd.shutdown()
        sys.exit()
