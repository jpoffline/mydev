'''
Simple chatroom

Reference
https://docs.python.org/2/library/threading.html
http://blog.oddbit.com/2013/11/23/long-polling-with-ja/
http://zulko.github.io/blog/2013/09/19/a-basic-example-of-threads-synchronization-in-python/
http://www.laurentluce.com/posts/python-threads-synchronization-locks-rlocks-semaphores-conditions-events-and-queues/
'''

import time
import threading
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
from ajax import *
message = None

class Chat_server(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        body = self.rfile.read(length)
        path = self.path
        print 'PATH: ', path
        if path.startswith('/'):
            path = path[1:]
        res = self.perform_operation(path, body)
        print path, ' RES: ', res, ' BODY ', body 
        if res:
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(res)
        else:
            self.send_response(404)

    def do_GET(self):
        path = self.path
        if path.startswith('/'):
            path = path[1:]
        res = get_html(path)
        if res:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(res)
        else:
            self.send_response(404)

    def perform_operation(self, oper, body):
        if oper=='poll':
            return message.wait(body)
        elif oper=='post':
            return message.post(body)





class Message():
    def __init__(self):
        self.data = ''
        self.time = 0
        self.event = threading.Event()
        self.lock = threading.Lock()
        self.event.clear()

    def wait(self, last_mess=''):
        
        if message.data != last_mess and time.time()-message.time < 60:
            # resend the previous message if it is within 1 min
            return message.data
        self.event.wait()
        return message.data

    def post(self, data):
        with self.lock:
            self.data = data
            self.time = time.time()
            self.event.set()
            self.event.clear()
        return 'ok'


ThreadingMixIn.daemon_threads = True
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""


def start_server(handler, host, port):
    global message
    message = Message()

    httpd = ThreadedHTTPServer((host, port), handler)
    print 'Serving at http://%s:%s' % (host, port)
    try:
        httpd.serve_forever()
    finally:
        httpd.server_close()


if __name__ == '__main__':
    start_server(Chat_server, 'localhost', 8000)