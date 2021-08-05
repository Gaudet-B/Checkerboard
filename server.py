from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def default():
    return render_template("index.html", boxes_x=8, boxes_y=8, color_1="red", color_2="black")

@app.route('/<int:boxes_y>')
def change_y(boxes_y):
    return render_template("index.html", boxes_x=8, boxes_y=boxes_y, color_1="red", color_2="black")

@app.route('/<int:boxes_x>/<int:boxes_y>')
def change_x_and_y(boxes_x, boxes_y):
    return render_template("index.html", boxes_x=boxes_x, boxes_y=boxes_y, color_1="red", color_2="black")

@app.route('/<int:boxes_x>/<int:boxes_y>/<string:color_1>/<string:color_2>')
def change_x_y_and_color(boxes_x, boxes_y, color_1, color_2):
    return render_template("index.html", boxes_x=boxes_x, boxes_y=boxes_y, color_1=color_1, color_2=color_2)

if __name__=="__main__":
    app.run(debug=True)