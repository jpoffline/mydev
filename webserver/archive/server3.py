#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep
import cgi
import htmlGenerator as html
import serverHelp as srv


PORT_NUMBER = 8080



#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		if self.path == "/":
			self.path = "index_example.html"

		try:
			#Check the file extension required and
			#set the right mime type

			sendReply = False
			if self.path.endswith(".html"):
				mimetype = 'text/html'
				sendReply = True
			if self.path.endswith(".jpg"):
				mimetype = 'image/jpg'
				sendReply = True
			if self.path.endswith(".gif"):
				mimetype = 'image/gif'
				sendReply = True
			if self.path.endswith(".js"):
				mimetype='application/javascript'
				sendReply = True
			if self.path.endswith(".css"):
				mimetype='text/css'
				sendReply = True

			if sendReply == True:
				#Open the static file requested and send it
				f = open(curdir + sep + self.path) 
				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()
				self.wfile.write(html.page_form())#f.read())
				f.close()
			return

		except IOError:
			self.send_error(404, 'File Not Found: %s' % self.path)

	def gen_form(self):
		form = cgi.FieldStorage(
			fp      = self.rfile, 
			headers = self.headers,
			environ = {
				'REQUEST_METHOD' : 'POST',
				'CONTENT_TYPE'   : self.headers['Content-Type']
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
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
	