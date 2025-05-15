#===========================================================
# Routing Functions
#===========================================================

from flask import Blueprint, render_template, request, redirect
from app.db import connect_db


# Allow these routes to be used in the main app
main = Blueprint("main", __name__)


#-----------------------------------------------------------
# Home page route - Show all the things, and new thing form
#-----------------------------------------------------------
@main.get("/")
def index():
    # Get all the things from the DB
    conn = connect_db()
    query = "SELECT * FROM things ORDER BY name ASC"
    records = conn.execute(query).fetchall()
    conn.close()

    # Show the page with the DB data
    return render_template("pages/home.jinja", things=records)


#-----------------------------------------------------------
# Route for adding a thing, using data posted from a form
#-----------------------------------------------------------
@main.post("/add")
def add():
    # Get the data from the form
    name  = request.form["name"]
    price = request.form["price"]

    # Add the thing to the DB
    conn = connect_db()
    query = "INSERT INTO things (name, price) VALUES (?, ?)"
    conn.execute(query, (name, price))
    conn.commit()
    conn.close()

    # Go back to the home page
    return redirect("/")


#-----------------------------------------------------------
# Route for deleting a thing, Id given in the route
#-----------------------------------------------------------
@main.get("/delete/<int:itemId>")
def delete(itemId):
    # Delete the thing from the DB
    conn = connect_db()
    query = "DELETE FROM things WHERE id=?"
    conn.execute(query, (itemId,))
    conn.commit()
    conn.close()

    # Go back to the home page
    return redirect("/")


#-----------------------------------------------------------
# About page route
#-----------------------------------------------------------
@main.get("/about")
@main.get("/about/")
def about():
    return render_template("pages/about.jinja")


#-----------------------------------------------------------
# 404 Error page
#-----------------------------------------------------------
@main.errorhandler(404)
def notFound(e):
    return render_template("pages/404.jinja")
