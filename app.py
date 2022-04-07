from flask import Flask, request
from ast import literal_eval
from numpy import array2string
from pixel_coordinate_grid import calculate_coordinate_grid

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome! API documentation here: "  # TODO: add GitHub link


@app.route("/coordinate-grid", methods=['POST'])
def return_coordinate_grid():
    image_dimensions, corners = literal_eval(request.form['image_dimensions']), \
                                literal_eval(request.form['corners'])
    try:
        coordinate_grid = calculate_coordinate_grid(image_dimensions, corners)
    except ValueError:
        return "Invalid input, both image dimensions must be greater than zero"
    return array2string(coordinate_grid, separator=', ')
