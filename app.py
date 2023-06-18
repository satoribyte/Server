import subprocess
from http.server import HTTPServer, BaseHTTPRequestHandler

class PHPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        php_output = subprocess.check_output(['php', 'web/index.php'])
        self.wfile.write(php_output)

server_address = ('', 4646)

httpd = HTTPServer(server_address, PHPHandler)
ngrok_process = subprocess.Popen(['ngrok', 'http', '4646'])

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.shutdown()
    ngrok_process.terminate()
