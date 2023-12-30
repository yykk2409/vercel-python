from flask import Flask, request, render_template, redirect
from flask_cors import CORS
from yt_dlp import YoutubeDL
import demucs.separate
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/sss', methods=["POST"])
def sss():
    url = request.form["url"]
    print(url)
    ydl_opts = {'format': 'bestaudio', 'outtmpl': 'sound.mp3'}
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    audio_data = info['url']
    options = [audio_data, "-n", "htdemucs", "--two-stems", "vocals", "--mp3"]
    demucs.separate.main(options)
    return render_template('main.html')
