###
# Sample configuration /usr/local/etc/nginx/nginx.conf
# events {
#     worker_connections  1024;
# }
#
# http {
#     upstream backend { # Weights are adjusted to demonstrate Least Connections
#         server 127.0.0.1:5001 weight=1; # Default weight is 1 if not specified
#         server 127.0.0.1:5002 weight=1;
#         server 127.0.0.1:5003 weight=1;
#     }
#
#     server {
#         listen 80;
#         location / {
#             proxy_pass http://backend;
#         }
#     }
#
#     include servers/*;
# }
###

from flask import Flask

app = Flask(__name__)
counter = 0  # Global counter to track number of requests

@app.route('/', methods=['POST'])
def increment_counter():
    global counter
    counter += 1
    return f"Server has processed {counter} requests!"

if __name__ == "__main__":
    app.run(port=5001)  # Adjust the port for different instances