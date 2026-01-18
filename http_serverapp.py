import http.server
from prometheus_client import start_http_server
class HandleRequests(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = """
        <html>
            <head>
                <title>First Python Application</title>
            </head>
            <body style="color:#333; margin-top:30px;">
                <center>
                    <h2>Welcome to our first Python application.</h2>
                </center>
            </body>
        </html>
        """

        self.wfile.write(html.encode("utf-8"))

if __name__ == "__main__":
    start_http_server(8001)
    server = http.server.HTTPServer(('3.113.242.39', 8000), HandleRequests)
    server.serve_forever()