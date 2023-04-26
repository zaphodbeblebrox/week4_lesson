from flask import Flask, render_template
# localhost:5000

app = Flask(__name__)

@app.route("/play")
def play():
    return render_template("index.html",
                            num_boxes = 3,
                            box_color = "aqua")

@app.route("/play/<number>")
def play_more(number):
    return render_template("index.html",
                            num_boxes = int(number),
                            box_color = "aqua")

@app.route("/play/<number>/<color>")
def play_extra(number, color):
    return render_template("index.html",
                            num_boxes = int(number),
                            box_color = color)

if __name__ == "__main__":
    app.run(debug=True)