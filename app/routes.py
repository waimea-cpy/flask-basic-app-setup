from flask import Blueprint, render_template, request, redirect
from app.db import connect_db


# Allow these routes to be used in the main app
main = Blueprint("main", __name__)


# HOME PAGE ---------------------------------------------------
@main.get("/")
def index():
    # Get all the things from the DB
    query = "SELECT * FROM things"
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query)
    things = cursor.fetchall()
    conn.close()

    # Show the page with the DB data
    return render_template("pages/home.jinja", things=things)


# ADD THING (from form) ---------------------------------------------------
@main.post("/add")
def add():
    # Get the data from the form
    name = request.form["name"]

    # Add the thing to the DB
    query = "INSERT INTO things (name) VALUES (?)"
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query, (name,))
    conn.commit()
    conn.close()

    # Go back to the home page
    return redirect("/")


# DELETE THING ---------------------------------------------------
@main.get("/delete/<int:itemId>")
def delete(itemId):
    # Delete the thing from the DB
    query = "DELETE FROM things WHERE id=?"
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query, (itemId,))
    conn.commit()
    conn.close()

    # Go back to the home page
    return redirect("/")


# ABOUT PAGE ---------------------------------------------------
@main.get("/about/")
def about():
    return render_template("pages/about.jinja")
