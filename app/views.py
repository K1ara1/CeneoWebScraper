from app import app
from flask import render_template

@app.route("/")
@app.route("/<name>")
def index(name="World"):
    return render_template("index.html")

@app.route("/extract")
def extract():
    render_template("extract.html")

@app.route("/products")
def extract():
    render_template("products.html")

@app.route("/author")
def extract():
    render_template("author.html")

@app.route("/product/<product_id>")
def extract(product_id):
    render_template("product.html",product_id=product_id)