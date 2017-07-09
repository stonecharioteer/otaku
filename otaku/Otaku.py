#!/bin/env python
"""
Otaku Base code.

===

This script provides all the routes for the base application.
"""
import os
import sys
import tarfile

from flask import (Flask, url_for,
                Response, render_template,
                jsonify)

app = Flask(__name__)

@app.route("/")
def serve_index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, threaded=True, host='0.0.0.0')

