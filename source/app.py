from flask import Flask, render_template, abort
import os
import json
import requests

# Start the app
app = Flask(__name__)

# Catch all requests
@app.route('/', defaults={'path': None})
@app.route('/<path:path>')
def catch_all(path):
    path = '/{}/'.format(path) if path is not None else '/'
    response = requests.get('http://169.254.169.254{}'.format(path))

    return render_template(
        'index.html',
        path=path,
        links=[
            link.rstrip('/')
            for link in  response.text.split('\n')
        ]
    )

if __name__ == "__main__":
    app.run()
