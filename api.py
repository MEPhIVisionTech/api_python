from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename
import os
 
app = Flask(__name__)
#app.config["SECRET_KEY"] = "fff"


upload = '/home/itech/Desktop/Project/neuroNetworking/flask/static/Image'
 
app.config['UPLOAD'] = upload
 

@app.route('/api/post/image', methods=['POST'])
def file_upload():
    print("cock")
    f = request.files['file']
    filename = secure_filename(f.filename)
    f.save(os.path.join(app.config['UPLOAD'], filename))
    return send_from_directory(app.config['UPLOAD'], filename)

@app.route("/")
def index():
    return render_template('render.html')

@app.route("/<file>")
def file(file):
    print("aboba",file)
    return send_from_directory(app.config['UPLOAD'], file)
 
if __name__ == '__main__':
    app.run(debug=True, port=8089, host="0.0.0.0")