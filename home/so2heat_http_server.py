import http.server
import ssl
import threading
import io
from PIL import Image

photoW = 10
photoH = 10
msg_queue = None


def initialize(data):
    global photoW, photoH, msg_queue
    photoW = data.get("photoW")
    photoH = data.get("photoH")
    msg_queue = data.get("msg_queue")


class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/v1/test':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            response = '{}'
            self.wfile.write(response.encode('utf-8'))
            # for header, value in self.headers.items():
            #   print(f"  {header}: {value}")
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == '/api/v1/update-status':
            content_type = self.headers.get('Content-Type', '')
            print(f"Incoming content type is {content_type}")

            if content_type == 'image/jpeg' or content_type == 'image/png':
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)

                image = Image.open(io.BytesIO(post_data))
                image = image.resize((photoW, photoH))
                msg_queue.put(("image", image));

            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.end_headers()
            response = '{"result":"status received"}'
            self.wfile.write(response.encode('utf-8'))


class StoppableHTTPServer:
    def __init__(self, host='localhost', port=8443, certfile='eebase_tech_2026_10_01.crt',
                 keyfile='eebase_tech_2026_10_01.key'):
        self.host = host
        self.port = port
        self.certfile = certfile
        self.keyfile = keyfile
        self.server = None
        self.thread = None

    def start(self):
        """Starting HTTPS server in another thread"""
        # Используем встроенный ThreadingHTTPServer (без SSL)
        handler = MyRequestHandler
        self.server = http.server.ThreadingHTTPServer((self.host, self.port), handler)

        # Добавляем SSL поверх существующего сервера
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(self.certfile, self.keyfile)
        self.server.socket = context.wrap_socket(self.server.socket, server_side=True)

        self.thread = threading.Thread(target=self.server.serve_forever)
        self.thread.daemon = True
        self.thread.start()
        print(f"HTTPS server started at https://{self.host}:{self.port}")

    def stop(self):
        """Stopping server"""
        if self.server:
            print("Stopping server...")
            self.server.shutdown()
            self.server.server_close()
            if self.thread:
                self.thread.join(timeout=5)
            print("Server stopped")

