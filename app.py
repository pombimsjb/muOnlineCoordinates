from flask import Flask, render_template, request
from variables import image_files, image_coordinates, event_list

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", image_files=image_files, event_list=event_list)


@app.route("/view_image/<image>", methods=["GET"])
def view_image(image):
    coordinates = image_coordinates.get(image, {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250})
    return render_template("view_image.html", image=image, coordinates=coordinates)


@app.route("/add_event", methods=["POST"])
def add_event():
    event_name = request.form["event-name"]
    event_time = request.form["event-time"]
    event_list.append({"name": event_name, "time": event_time})
    return render_template("index.html", image_files=image_files, event_list=event_list)


if __name__ == "__main__":
    app.run(debug=True)
