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


def get_manga_images_list(p=None):
    # Returns a list of images.
    from glob import glob
    from os.path import join, normpath
    if p is None:
        p = normpath("/home/vinay/Manga/naruto/Naruto 1")
    if os.path.isdir(p):
        imgs = []
        for possible_ext in ["*.png","*.jpg","*.jpeg"]:
            imgs += glob(join(p,possible_ext))
            imgs += glob(join(p, possible_ext.upper()))
        return imgs
    else:
        raise Exception("Uh-oh! Folder {} doesn't exist!".format(p))

app = Flask(__name__, template_folder="../templates")

@app.route("/")
def serve_index():
    return render_template("index.html", slides=get_manga_images_list())

if __name__ == "__main__":
    app.run(debug=True, threaded=True, host='0.0.0.0')

