import os

from flask import Flask, render_template, jsonify

from woordje.root.views import blueprint


app = Flask(__name__)


@app.route('/getdir')
def get_dir():
    dircont,fcont = [], []
    for f in os.listdir('.'):
        if os.path.isdir(f):
            dircont.append({"name": f, "dir": True})
        else:
            fcont.append({"name": f, "dir": False})
    for _list in [dircont, fcont]:
        sorted(_list,key=lambda x: x['name'])
    dircont.extend(fcont)
    return jsonify({"data": dircont})

def main():
    app.register_blueprint(blueprint)
    app.secret_key = "somewhere a village is missing its idiot"
    app.run(debug=True)

if __name__ == '__main__':
    main()
