import os
from flask import *
import mlab
from mongoengine import *
from werkzeug.utils import secure_filename

app = Flask(__name__)
mlab.connect()

app.config["IMG_PATH"] = os.path.join(app.root_path, "images")
app.secret_key = "864YcC%$q=rKPVdU"

class Flower(Document):
    image = StringField()
    title = StringField()
    price = FloatField()

flower1 = Flower(
                image="https://s-media-cache-ak0.pinimg.com/originals/05/b9/9f/05b99f02503732d4b96e9c81a0e94019.jpg",
                 title="Pink",
                 price=30000
)

flower1.save()

image = "https://s-media-cache-ak0.pinimg.com/736x/39/6f/0a/396f0ad4ce00e0ccf1ffead17da426c1--purple-things-purple-stuff.jpg"
title = "violet rose"
price = 10000

@app.route('/')
def index():
    return render_template("index.html", flowers = Flower.objects())

                           # image="https://s-media-cache-ak0.pinimg.com/736x/39/6f/0a/396f0ad4ce00e0ccf1ffead17da426c1--purple-things-purple-stuff.jpg",
                           # title = "violet rose",
                           # price = 10000)
@app.route("/images/<image_name>")
def image(image_name):
    return send_from_directory(app.config["IMG_PATH"], image_name)

flowers = [

    {
        "image": "https://s-media-cache-ak0.pinimg.com/736x/39/6f/0a/396f0ad4ce00e0ccf1ffead17da426c1--purple-things-purple-stuff.jpg",
        "title": "violet rose",
        "price": 10000
    },
    {
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Yonina_Tulip.jpg/220px-Yonina_Tulip.jpg",
        "title": "Tulip",
        "price": 20000
    },
    {
        "image": "https://s-media-cache-ak0.pinimg.com/originals/05/b9/9f/05b99f02503732d4b96e9c81a0e94019.jpg",
        "title": "Pink",
        "price": 30000

    }
]



@app.route("/logout")
def logout():
    session["/logged_in"] = False
    return redirect(url_for("login"))

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        form = request.form
        username = form["username"]
        password = form["password"]

        if username == "admin" and password == "admin":
            # valid credentital
            session["logged_in"] = True
            return redirect(url_for("index"))
        else:
            return "Invalid credentitals"
            #invalid credentital

@app.route('/add-flower', methods = ["GET", "POST"])
def add_flower():
    if "logged_in" in session and session["logged_in"]:
        if request.method == "GET":
            return render_template("add_flower.html")
        elif request.method == "POST":#User submitted form
            # 1: Get data (title, image, price)

            form = request.form
            title = form["title"]
            # image = form["image"]
            price = form["price"]

            image = request.files["image"]

            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config["IMG_PATH"], filename))

            # 2: Save data into database
            new_flower = Flower(title = title,
                                image = "/images/{0}".format(filename),
                                price = price)
            new_flower.save()
            return redirect(url_for("index"))
    else:
        return redirect(url_for("login"))


@app.route("/users/<username>")
def usert(username):
    return "Hello, my name is " + username + ", welcome to my page <3"

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return "{0} + {1}  = {2}".format(a, b, a + b)



# @app.route('/tuna')
# def tuna():
#     return '<h2>Tuna is good</h2>'
#
# @app.route('/profile/<username>')
# def profile(username):
#     return "<h2>Hey there %s</h2>" % username
#
# @app.route('/post/<int:post_id>')
# def post(post_id):
#     return "<h2>Post ID %s</h2>" % post_id


if __name__ == '__main__':
    app.run()
