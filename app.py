from flask import Flask, Response
from prometheus_client import start_http_server, Counter, generate_latest
import matplotlib

matplotlib.use('Agg')
app = Flask(__name__)
c = Counter('my_successes', 'Description of counter')
@app.route('/', methods=['POST'])
def increment_counter():
    c.inc()  # Increment the counter
    return "Processed requests!"

@app.route('/metrics', methods=['GET'])
def metrics():
    return Response(generate_latest(), content_type='text/plain')

if __name__ == '__main__':
    start_http_server(5001)  # Start up the server to expose the metrics.
    app.run(host='0.0.0.0', port=5001)
