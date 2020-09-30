from flask import Flask, render_template, redirect, request

import os
from glob import glob
import re
import random

image_extensions = ["jpg", "png"]
src_dir = os.path.dirname(os.path.abspath(__file__))
dataset_dir = src_dir + "/static/dataset/target"
output_dir = src_dir + "/static/dataset/annotations"

get_basename = lambda p: re.sub('\..*?$','', p.replace(dataset_dir,'').replace(output_dir, ''))

app = Flask(__name__)

print(sum([glob(dataset_dir + "/**/*." + ext, recursive=True) for ext in image_extensions], []))

# index.html
@app.route("/")
def index():
    title = "Top"

    output_paths = set([get_basename(p) for p in glob(output_dir + "/**/*.txt", recursive=True)])
    image_paths = sorted(sum([glob(dataset_dir + "/**/*." + ext, recursive=True) for ext in image_extensions], []))
    image_paths = [{'link': '/edit?image_path='+p[4:], 'name': p} for p in image_paths if get_basename(p) not in output_paths]

    if request.args.get('rand'):
      return redirect(random.choice(image_paths)["link"])
    if request.args.get('next'):
      return redirect(image_paths[0]["link"])

    # index.html をレンダリングする
    return render_template(
        "index.html",
        image_paths=image_paths[:100]
    )


# edit.html
@app.route("/edit")
def edit():
    title = "Edit"
    image_path = request.args.get('image_path')

    return render_template(
        "edit.html",
        image_path=image_path
    )

# register attributes
@app.route("/register", methods=["post"])
def register():
    try:
        output_path = "/app" + request.json["output_path"]
        data = request.json["data"]
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, mode='w') as f:
          f.write('\n'.join(data))
          os.chmod(output_path, 0o777)
        return 'success'
    except Exception as e:
        print(e)
        return str(e), 500

if __name__ == "__main__":
    app.debug = True  # デバッグモード有効化
    app.run(host="0.0.0.0", port=80, threaded=True)  # どこからでもアクセス可能に

