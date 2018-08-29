from flask import Flask, render_template
import cv2
from datetime import datetime
app = Flask(__name__)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['Last-Modified'] = datetime.now()
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/render_thresh/<value1>/<value2>')
def render_thresh(value1, value2):
    gray = cv2.imread("static/images/tetris_blocks_gray.png")
    thresh = cv2.threshold(gray, float(value1), float(value2), cv2.THRESH_BINARY_INV)[1]
    new_image = "static/images/tetris_blocks_thresh.png"
    cv2.imwrite(new_image, thresh)
    return render_template("thresh.html", new_image=new_image)


@app.route('/render_thresh_black/<value1>/<value2>')
def render_thresh_black(value1, value2):
    gray = cv2.imread("static/images/tetris_blocks_gray.png")
    thresh = cv2.threshold(gray, float(value1), float(value2), cv2.THRESH_BINARY_INV)[1]
    new_image = "static/images/tetris_blocks_thresh.png"
    cv2.imwrite(new_image, thresh)
    return render_template("thresh.html", new_image=new_image)


if __name__ == '__main__':
    image = cv2.imread("static/images/tetris_blocks.png")

    # convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("static/images/tetris_blocks_gray.png", gray)
    app.run()