#!/bin/env python
"""
Otaku Base code.

===

This script provides all the routes for the base application.
"""
import os
import shutil
#import tarfile

from flask import (Flask, render_template, url_for)


def get_manga_images_list(p=None):
    # Returns a list of images.
    from glob import glob
    from os.path import join, normpath, basename, dirname
    if p is None:
        p = normpath("/home/vinay/Manga/naruto/Naruto 1")
        #Copy the folder into the tmp folder
        from distutils.dir_util import copy_tree
        new_folder_path = os.path.join("static","tmp",basename(dirname(p)),basename(p))
        if os.path.exists(new_folder_path):
            shutil.rmtree(new_folder_path)
        os.makedirs(new_folder_path)
        copy_tree(p, new_folder_path)
        p = new_folder_path
    if os.path.isdir(p):
        imgs = []
        for possible_ext in ["*.png","*.jpg","*.jpeg"]:
            imgs += glob(join(p,possible_ext))
            imgs += glob(join(p, possible_ext.upper()))
        img_ps = []
        for i in sorted(imgs):
            base = i.split("/")[0]
            f = join(*i.split("/")[1:])
            url = url_for(base, filename=f)
            img_ps += [url]
        return img_ps
    else:
        raise Exception("Uh-oh! Folder {} doesn't exist!".format(p))

app = Flask(__name__)

@app.route("/")
def serve_index():
    return render_template("index.html", slides_list=get_manga_images_list())

if __name__ == "__main__":
    app.run(debug=True, port=8080, threaded=True, host='0.0.0.0')

