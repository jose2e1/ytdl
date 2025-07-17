from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/download', methods=["POST"])
def download():
    try:
        url = request.form.get("url")
        yt = YouTube(url)

        title = yt.title
        thumbnail = yt.thumbnail_url
        streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
        audio = yt.streams.filter(only_audio=True).first()

        return render_template("result.html", title=title, thumbnail=thumbnail, streams=streams, audio=audio, url=url)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
