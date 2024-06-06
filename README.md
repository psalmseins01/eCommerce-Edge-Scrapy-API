# eCommerce Edge Scrapy API

## Introduction
This project provides an API for managing book data, which can be scraped from an e-commerce site. It includes CRUD operations for book items and Swagger documentation for the endpoints.

## Project Structure

project/
app.py
models.py
templates/
index.html
static/
css/
js/
requirements.txt



- `app.py`: Main entry point for the Flask application, defining routes and configuring the app.
- `models.py`: Database models using SQLAlchemy.
- `templates/`: Directory for HTML templates.
  - `index.html`: Landing page describing the project.
- `static/`: Directory for static files like CSS and JS.
- `requirements.txt`: List of Python dependencies.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/psalmseins01/eCommerce-Edge-Scrapy-API.git
    cd eCommerce-Edge-Scrapy-API
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

5. Run the application:
    ```bash
    flask run
    ```

## Usage

### API Endpoints

#### Book Items
- `POST /books` - Create a new book record
- `GET /books` - Retrieve all book records
- `GET /books/<int:id>` - Retrieve a book record by ID
- `PUT /books/<int:id>` - Update a book record by ID
- `DELETE /books/<int:id>` - Delete a book record by ID

### Swagger Documentation
Swagger UI is available at `/swagger` for interactive API documentation.

## Landing Page
The landing page describing the project is available at the root URL (`/`).

## Running Tests
Run the unit tests with:
```bash
python -m unittest discover tests

## Setup
### Prerequisites
- Python 3.8+
- MySQL
- Installation

git clone https://github.com/psalmseins01/eCommerce-Edge-Scrapy-API.git
cd eCommerce-Edge-Scrapy-API

