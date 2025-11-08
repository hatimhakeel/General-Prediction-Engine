"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
from services.tsforecastservice import sales_forecasts_trainer, sales_forecasts

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
def hello():
    """Renders a sample page."""
    return "Hello World!"

@app.route('/sales_forecast/<customerid>/<int:predictinterval>')
def sales_forecast(customerid, predictinterval):
    """Returns a dict"""

    result = sales_forecasts(customerid, predictinterval)
@app.route('/sales_forecast/train/<customerid>')
def sales_forecast_train(customerid):
    
    result = sales_forecasts_trainer(customerid)
    return result


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    PORT = 8870
    '''try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555'''
    app.run(HOST, PORT)
