""" jp webserver """
#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep
import cgi
import htmlGenerator as html
import serverHelp as srv


PORT_NUMBER = 8080

# This class will handles any incoming request from
# the browser


class myHandler(BaseHTTPRequestHandler):

    # Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html.page_index())

        return

    def gen_form(self):
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
