from flask import Flask, Response, render_template, redirect, url_for, request, jsonify
import time, random
from pi_camera import Camera
import socket

app = Flask(__name__)

@app.route('/<FUNCTION>')
def command(FUNCTION=None):
    exec(FUNCTION.replace("<br>", "\n"))
    return ""

def left():
    print("Turn left")

def right():
    print("Turn right")

def back():
    print("Turn back")

def forward():
    print("Turn straight")

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

def videostreaming_generator():
    """Видео стриминг генератор"""
    yield b'--frame\r\n'
    while True:
        yield b'Content-Type: image/jpeg\n\n' + Camera().get_frame() + b' --frame'


@app.route('/video_feed')
def video_feed():
    """Маршрут потоковой передачи видео"""
    return Response(videostreaming_generator(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True, host=socket.gethostbyname(socket.gethostname()))