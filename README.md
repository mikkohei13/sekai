# Sekai

A simple web app for storing fictional character data: names, descriptions, features, lore, images, etc. To be expanded later into a worldbuilding and story database.

## Architecture

Core Stack

- Database: PostgreSQL (Stores character data, lore, image paths, and handles native Finnish full-text search).

- ORM: SQLAlchemy (Maps Python objects to Postgres tables and executes complex queries).

- Admin UI: Flask-Admin (Automatically generates a CRUD interface from your SQLAlchemy models with zero frontend coding required).

- Backend & Templating: Flask & Jinja2 (Handles business logic, serves HTML pages, and manages routing).

- Interactivity: HTMX (Handles dynamic frontend behavior like live search).

Run locally with Docker Compose:

db service: Runs the official PostgreSQL image. You will mount a persistent Docker volume here to ensure your character data survives container restarts.

web service: Runs your Flask application. It connects to the db service using SQLAlchemy. You will also mount a second persistent Docker volume to your Flask app's upload directory (e.g., /app/static/uploads) so your character image files are permanently stored on your host machine.


