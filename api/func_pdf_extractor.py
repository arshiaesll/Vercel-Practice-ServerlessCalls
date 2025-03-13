from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200);
        self.send_header('Content-type', 'text/html')

        self.end_headers()
        # AI GENERATED
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>PDF Extractor API</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #f5f5f5;
                }
                .container {
                    background-color: white;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }
                h1 {
                    color: #333;
                }
                p {
                    color: #666;
                    line-height: 1.6;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>PDF Extractor API</h1>
                <p>This endpoint provides PDF text extraction functionality.</p>
                <p>To use this API, send a POST request with your PDF file.</p>
                <p>Current endpoint: <code>/api/func_pdf_extractor.py</code></p>
            </div>
        </body>
        </html>
        """
        # END AI        
        self.wfile.write(html_content.encode('utf-8'))


    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        content_type = self.headers.get('Content-Type', "")

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        result = {"name" : "Arshia"}
        response = json.dumps(result)

        self.wfile.write(response.encode("utf-8"))
        print(content_type)