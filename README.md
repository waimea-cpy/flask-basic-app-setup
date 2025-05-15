# A Basic Flask App with SQLite Database

This is template for a simple [Flask](https://flask.palletsprojects.com) application with a [SQLite](https://www.sqlite.org) database to store and provide data. The app uses [Jinja2](https://jinja.palletsprojects.com/templates/) templating for structuring pages and data, and [PicoCSS](https://picocss.com/) for styling.

## Project Structure

- **app** folder
    - **db** folder
        - **data.db** - The SQLite database
        - **schema.sql** - Defines the database structure
    - **static** folder - Files to be served as-is
        - **css** folder
            - **styles.css** - A user stylesheet
        - **images** folder
            - **icon.svg** - Site favicon
            - *other example images*
    - **templates** folder
        - **pages** folder
            - **base.jinja** - The base template for all pages
            - *other templates for specific pages*
    - **\_\_init__.py** - App launcher code
    - **db.py** - Functions for database setup and access
    - **routes.py** - Functions to handle URL routes

- **requirements.txt** - Defines the Pyth0n modules needed

## Project Setup and Deployment

See [SETUP.md](SETUP.md) for details of how to install and run the app locally for development, and how to deploy the app to [Render](https://render.com/) for hosting.

## Demo Site

A demo of this site is hosted [here]()

