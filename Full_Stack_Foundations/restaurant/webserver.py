from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi
import database_queries

class webserverHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		try:
			if self.path.endswith("/hello"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				output = ""
				output += "<html><body>"
				output += "Hello World!"
				output += "<form method = 'POST' enctype='multipart/form-data' action='/hello'><h2> What would you like me to say?</h2><input name='message' type='text'><input type='submit' value='Submit'></form>";
				output += "</body></html>"

				self.wfile.write(output);
				return

			if self.path.endswith("/restaurants"):
				output = "";
				output += "<html><body>"
				output += "<a href=/restaurants/new>Create a new Restaurant</a>"
				output += "</br></br>"
				output += database_queries.getHTMLContentWithRestaurantList(database_queries.getAllRestaurants())
				output += "</body></html>"

				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()
				self.wfile.write(output);
				return

			if self.path.endswith("/restaurants/new"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				output = ""
				output += "<html><body>"
				output += "<form method = 'POST' enctype='multipart/form-data' action='/restaurants/new'><h2>Make a new restaurant</h2><input name='name' type='text'><input type='submit' value='Create'></form>";
				output += "</body></html>"

				self.wfile.write(output);
				return

			if self.path.endswith("/edit"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				restaurant_id = self.path.split('/')[2];
				output = ""
				output += "<html><body>"
				output += "<form method = 'POST' enctype='multipart/form-data' action='/restaurants/%s/edit'><h2>Change the name of this restaurant</h2><input name='name' type='text'><input type='submit' value='Update'></form>" % (restaurant_id);
				output += "</body></html>"

				self.wfile.write(output);
				return

			if self.path.endswith("/delete"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				restaurant_id = self.path.split('/')[2];
				output = ""
				output += "<html><body>"
				output += "<form method = 'POST' enctype='multipart/form-data' action='/restaurants/%s/delete'><h2>Are you sure you want to delete this restaurant?</h2><input type='submit' value='Delete'></form>" % (restaurant_id);
				output += "</body></html>"

				self.wfile.write(output);
				return
		except:
			self.send_error(404, "File Not Found %s" % self.path);


	def do_POST(self):

		try:
			if self.path.endswith("/restaurants/new"):
				ctype, pdcit = cgi.parse_header(self.headers.getheader('content-type'))
				if ctype == 'multipart/form-data':
					fields = cgi.parse_multipart(self.rfile, pdcit);
					restaurant_name = fields.get('name');
					database_queries.addRestaurant(restaurant_name[0]);

				self.send_response(301);
				self.send_header('Content-type', 'text/html')
				self.send_header('Location', '/restaurants')
				self.end_headers()

			if self.path.endswith("/edit"):
				restaurant_id = self.path.split('/')[2];

				ctype, pdcit = cgi.parse_header(self.headers.getheader('content-type'))
				if ctype == 'multipart/form-data':
					fields = cgi.parse_multipart(self.rfile, pdcit);
					restaurant_name = fields.get('name');
					database_queries.updateRestaurantName(restaurant_id, restaurant_name[0]);

				self.send_response(301);
				self.send_header('Content-type', 'text/html')
				self.send_header('Location', '/restaurants')
				self.end_headers()
			
			if self.path.endswith("/delete"):
				restaurant_id = self.path.split('/')[2];
				print self.path
				database_queries.deleteRestaurant(restaurant_id);

				self.send_response(301);
				self.send_header('Content-type', 'text/html')
				self.send_header('Location', '/restaurants')
				self.end_headers()

		except:
			print "Error!"


def main():
	try:
		port = 8080
		server = HTTPServer(('', port), webserverHandler)
		print "Web server running on port %s" % port
		server.serve_forever()

	except KeyboardInterrupt:
		print "^C entered, stopping web server"
		server.socket.close()


if __name__ == '__main__':
	main();