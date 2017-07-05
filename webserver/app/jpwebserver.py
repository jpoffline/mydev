""" jp webserver """
#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep
import cgi
import lib.htmlgenerator as html
import lib.serverhelp as srv
from app.app import page_index

PORT_NUMBER = 8080

# This class will handles any incoming request from
# the browser


class myHandler(BaseHTTPRequestHandler):
    """ myHandler """
    # Handler for the GET requests
    def do_GET(self):
        """ do_GET """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(page_index())

        return

    def gen_form(self):
        """ gen_form """
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={
                'REQUEST_METHOD': 'POST',
                'CONTENT_TYPE': self.headers['Content-Type']
            }
        )
        return form

    # Handler for the POST requests
    def do_POST(self):
        """ do_POST """
        recd = self.path.split('?')
        form = self.gen_form()
        self.send_response(200)
        self.end_headers()
        keys = recd[1].split('&')
        values = []
        for key in keys:
            values.append(srv.read_form(form, key))

        send_type = recd[0]

        self.wfile.write(
            html.get_response_page(
                srv.gen_response_string(
                    send_type,
                    keys,
                    values
                )
            )
        )
        return


try:

    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ', PORT_NUMBER
    server.serve_forever()

except KeyboardInterrupt:
    print '* kill command received; shutting down the web server'
    server.socket.close()
