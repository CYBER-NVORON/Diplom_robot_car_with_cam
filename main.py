from flask import Flask, Response, render_template, redirect, url_for, request, jsonify
import time, random
from camera_opencv import Camera
import socket

app = Flask(__name__)

def left():
    print("Turn left")

def right():
    print("Turn right")

def straight():
    print("Turn straight")

def back():
    print("Turn back")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        if request.form.get('left') == 'left':
            left()
        if request.form.get('right') == 'right':
            right()
        if request.form.get('straight') == 'straight':
            straight()
        if request.form.get('back') == 'back':
            back()
    
    return render_template('index.html')


def gen(camera):
    """Видео стриминг генератор"""
    yield b'--frame\r\n'
    while True:
        frame = camera.get_frame()
        yield b'Content-Type: image/jpeg\n\n' + frame + b' --frame'


@app.route('/video_feed')
def video_feed():
    """Маршрут потоковой передачи видео"""
    return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True, host=socket.gethostbyname(socket.gethostname()))