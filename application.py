from flask import Flask, render_template, url_for, redirect, Response

from lib.streams import HlsStream

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bin/create-stream')
def create_stream():
    try:
        hls_stream = HlsStream()
    except:
        # except a db error
        return url_for(index)
    hls_stream.initialize()
    return redirect(url_for('live', key=hls_stream.key))

@app.route('/live/<key>')
def live(key):
    # hands off to nginx
    return Response('', status=500)