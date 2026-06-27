from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 899.99, "category": "electronics"},
    {"id": 2, "name": "Book", "price": 14.99, "category": "books"},
    {"id": 3, "name": "Desk", "price": 199.99, "category": "furniture"},
]

@app.route("/")
def home():
    return jsonify({"message": "welcome message"})


@app.route("/products")
def get_products():
    category = request.args.get("category")

    if category:
        filtered = [
            p for p in products
            if p["category"].lower() == category.lower()
        ]
        return jsonify(filtered)

    return jsonify(products)


@app.route("/products/<int:id>")
def get_product_by_id(id):
    for product in products:
        if product["id"] == id:
            return jsonify(product)

    return jsonify({"error": "Product not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)