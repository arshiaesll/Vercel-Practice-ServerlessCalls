from http.server import BaseHTTPRequestHandler
import json

def hello_world():
    return "Hello, World!"

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # Create a response object
        response = {
            "message": hello_world(),
            "status": "success",
            "endpoint": "/api/test.py"
        }
        
        # Convert to JSON and send
        self.wfile.write(json.dumps(response).encode('utf-8'))
    
    def do_POST(self):
        # Get the size of data
        content_length = int(self.headers['Content-Length'])
        
        # Get the data
        post_data = self.rfile.read(content_length)
        
        # Parse the data
        try:
            data = json.loads(post_data.decode('utf-8'))
            name = data.get('name', 'World')
            
            # Create a response
            response = {
                "message": f"Hello, {name}!",
                "status": "success",
                "method": "POST",
                "received_data": data
            }
            
            # Send a success response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))
            
        except json.JSONDecodeError:
            # Send an error response
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_response = {
                "message": "Invalid JSON data",
                "status": "error"
            }
            self.wfile.write(json.dumps(error_response).encode('utf-8'))

# This is only used when running locally
if __name__ == "__main__":
    print(hello_world())
