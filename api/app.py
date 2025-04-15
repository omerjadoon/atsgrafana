import logging
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Logging config
logging.basicConfig(
    level=logging.INFO,  # You can use DEBUG for more detail
    format='%(asctime)s %(levelname)s: %(message)s',
)

logger = logging.getLogger(__name__)

# Static metric
metrics.info('app_info', 'Application info', version='1.0.0')

@app.route('/')
def hello():
    logger.info("Hello endpoint was hit")
    return 'Hello World!'

@app.route('/api/data')
@metrics.counter('api_data_requests', 'Number of calls to data endpoint')
def data():
    logger.info("Data endpoint was called")
    return {'data': 'some data'}

if __name__ == '__main__':
    logger.info("Starting Flask app...")
    app.run(host='0.0.0.0', port=5000)
