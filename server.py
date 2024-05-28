from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import numpy as np
import cv2
import base64
from utils.process_video import color_image

app = Flask(__name__)
app.debug = True
CORS(app)


@app.route('/')
def index():
    return render_template('video_capture.html')


@app.route('/process_frame', methods=['POST'])
def process_frame():
    try:
        data = request.get_json()
        img_data = base64.b64decode(data['frame'])
        nparr = np.frombuffer(img_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        colored_image = color_image(img)

        _, buffer = cv2.imencode('.jpg', colored_image)
        encoded_colored_image = base64.b64encode(buffer).decode('utf-8')

        return jsonify({'color_image': encoded_colored_image})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
