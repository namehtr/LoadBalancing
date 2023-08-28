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