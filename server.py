from fastapi import FastAPI
from fastapi.responses import StreamingResponse, HTMLResponse
import subprocess

app = FastAPI()

# Twój VB-Cable device name
DEVICE_NAME = r"audio=@device_cm_{t-id-nazwa-urządzenie }"

def ffmpeg_stream():
    """Stream audio z urządzenia VB-Cable przez ffmpeg"""
    ffmpeg = subprocess.Popen(
        [
            "ffmpeg",
            "-f", "dshow",
            "-i", DEVICE_NAME,
            "-c:a", "libmp3lame",
            "-b:a", "128k",
            "-f", "mp3",
            "-"
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL
    )
    try:
        while True:
            data = ffmpeg.stdout.read(4096)
            if not data:
                break
            yield data
    finally:
        try:
            ffmpeg.kill()
        except:
            pass

@app.get("/audio")
def live_audio():
    return StreamingResponse(ffmpeg_stream(), media_type="audio/mpeg")

@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <!doctype html>
    <html>
      <head>
        <meta charset="utf-8">
        <title>Live Audio + Kick Chat</title>
        <style>
          body { font-family: Arial, sans-serif; background: #0b0b0b; color: #eee; margin: 0; padding: 10px; }
          h1 { color: #6ee7b7; font-size: 1.1em; margin-bottom: 6px; }

          .row { display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 10px; }
          
          .card { 
            background: #111; 
            padding: 8px; 
            border-radius: 8px; 
            box-shadow: 0 4px 10px rgba(0,0,0,0.5); 
            flex: 1; 
            min-width: 200px; 
            height: 120px;   /* audio card */
          }
          
          .wide { 
            background: #111; 
            padding: 8px; 
            border-radius: 8px; 
            box-shadow: 0 4px 10px rgba(0,0,0,0.5); 
            flex: 1; 
            min-width: 300px; 
            height: 500px;   /* chat cards */
          }
          
          .wide iframe { 
            width: 100%; 
            height: 100%; 
            border: none; 
            border-radius: 6px; 
          }
          
          audio { width: 100%; margin-top: 6px; }
        </style>
      </head>
      <body>
        <!-- Pierwszy rząd: audio -->
        <div class="row">
          <div class="card">
            <h1>🎧 Live Audio</h1>
            <audio controls autoplay src="/audio"></audio>
          </div>
        </div>

        <!-- Drugi rząd: chaty obok siebie -->
        <div class="row">
          <div class="wide">
            <h1>📺 Kick Chat</h1> 
            <iframe src="https://socialstream.ninja/dock.html?session="></iframe>
          </div>
          <div class="wide">
            <h1>💬 Kick Chat tylko do alertów</h1>
            <iframe src="https://kick.com/popout/700rafalski/chat"></iframe>
          </div>
        </div>
      </body>
    </html>
    """
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
