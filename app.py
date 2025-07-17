from flask import Flask, render_template, request, Response
from pytube import YouTube

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            return Response(
                stream.stream_to_buffer(),
                mimetype='video/mp4',
                headers={"Content-Disposition": f"attachment;filename={yt.title}.mp4"}
            )
        except Exception as e:
            return render_template('index.html', error=str(e))
    return render_template('index.html')

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
