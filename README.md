# Django Contact Agenda Project

This is a web application project for a contact agenda developed with Django.

## Hosted Site

Access the application at [Agenda](https://agendaotaviossousa.pythonanywhere.com)

## Features

- User registration
- User login and logout
- Contact CRUD (create, read, update, and delete)
- Contact search
- Contact pagination
- Upload images for contacts

## Project Structure

- `base_static/`: Global static files (CSS, JS, images)
- `base_templates/`: Global HTML templates
- `contact/`: Main application with specific models, views, forms, and templates
- `core/`: Project settings and URLs
- `media/`: Directory for file uploads
- `static/`: Directory for collected static files
- `utils/`: Utility scripts

## Utility Scripts

- `utils/create_contacts.py`: Creates random contacts for testing