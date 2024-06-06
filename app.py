from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scrapyuser:scrapy_password@localhost/books'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "Books API"})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    price_excl_tax = db.Column(db.Float, nullable=False)
    price_incl_tax = db.Column(db.Float, nullable=False)
    tax = db.Column(db.Float, nullable=False)
    availability = db.Column(db.Integer, nullable=False)
    num_reviews = db.Column(db.Integer, nullable=False)
    stars = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    product_type = db.Column(db.String(255), nullable=False)
    upc = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)


    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}


@app.route('/')
def landing_page():
    return render_template('index.html')

# Create
@app.route('/books', methods=['POST'])
def create_book():
    data = request.json
    new_book = Book(**data)
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.id), 201

# Read all
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.as_dict() for book in books])

# Read one
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify(book.as_dict())

# Update
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.json
    book = Book.query.get_or_404(id)
    for key, value in data.items():
        setattr(book, key, value)
    db.session.commit()
    return jsonify(book.as_dict())

# Delete
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
