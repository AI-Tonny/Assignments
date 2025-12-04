from flask import Flask, request, jsonify
from pydantic import ValidationError

from db.db import product_db, Product
from schemas.product import (
    ProductCreate,
    ProductChange,
    ProductResponse,
    ProductOneResponse,
    ProductsResponse,
    ProductCreatedResponse,
    ProductChangedResponse,
    ProductDeletedResponse
)

app = Flask(__name__)
app.secret_key = "our-super-secret-key"

@app.route("/")
def root():
    return jsonify({
        "status": 200,
        "success": True,
        "message": "The server is working"
    })

@app.route("/api/health")
def health():
    return jsonify({
        "status": 200,
        "success": True,
        "message": "The server is healthy"
    })

@app.route("/api/create-product/", methods=['POST'])
def create_product():
    try:
        product_to_create = ProductCreate(**request.json)
        created_product = Product(
            id=len(product_db),
            name=product_to_create.name,
            price=product_to_create.price,
            quantity=product_to_create.quantity
        )

        product_db.append(created_product)

        return jsonify(
            ProductCreatedResponse(
            status=201,
            success=True,
            data=ProductResponse(
                name=created_product.name,
                price=created_product.price,
                quantity=created_product.quantity
            )
        ).dict()), 201
    except ValidationError as e:
        return jsonify({
            "status": 400,
            "success": False,
            "errors": e.errors()
        }), 400

@app.route("/api/get-products/", methods=['GET'])
def get_products():
    try:
        return jsonify(
            ProductsResponse(
            status=200,
            success=True,
            data=[ProductResponse(
                name=product.name,
                price=product.price,
                quantity=product.quantity) for product in product_db]
        ).dict()), 200
    except ValidationError as e:
        return jsonify({
            "status": 400,
            "success": False,
            "errors": e.errors()
        }), 400

@app.route("/api/get-product/<int:product_id>", methods=['GET'])
def get_product(product_id):
    try:
        wanted_product_to_get = next((product for product in product_db if product.id == product_id), None)

        if wanted_product_to_get is None:
            return jsonify({
                "status": 404,
                "success": False,
                "message": "Product not found",
                "data": None
            }), 404

        return jsonify(
            ProductOneResponse(
            status=200,
            success=True,
            data=ProductResponse(
                name=wanted_product_to_get.name,
                price=wanted_product_to_get.price,
                quantity=wanted_product_to_get.quantity
            )
        ).dict()), 200
    except ValidationError as e:
        return jsonify({
            "status": 400,
            "success": False,
            "errors": e.errors()
        }), 400

@app.route("/api/change-product/<int:product_id>", methods=['PUT'])
def change_product(product_id):
    try:
        product_with_new_data = ProductChange(**request.json)

        product_to_change_id = next((product.id for product in product_db if product.id == product_id), None)

        if product_to_change_id is None:
            return jsonify({
                "status": 404,
                "success": False,
                "message": "Product not found",
                "data": None
            }), 404

        product_to_change = product_db[product_to_change_id]
        product_to_change.name = product_with_new_data.name
        product_to_change.price = product_with_new_data.price
        product_to_change.quantity = product_with_new_data.quantity

        return jsonify(
            ProductChangedResponse(
            status=200,
            success=True,
            data=ProductResponse(
                name=product_to_change.name,
                price=product_to_change.price,
                quantity=product_to_change.quantity
            )
        ).dict()), 200
    except ValidationError as e:
        return jsonify({
            "status": 400,
            "success": False,
            "errors": e.errors()
        }), 400

@app.route("/api/delete-product/<int:product_id>", methods=['DELETE'])
def delete_product(product_id):
    try:
        product_to_delete_id = next((product.id for product in product_db if product.id == product_id), None)

        if product_to_delete_id is None:
            return jsonify({
                "status": 404,
                "success": False,
                "message": "Product not found",
                "data": None
            }), 404

        del product_db[product_to_delete_id]

        return jsonify(
            ProductDeletedResponse(
            status=200,
            success=True
        ).dict()), 200
    except ValidationError as e:
        return jsonify({
            "status": 400,
            "success": False,
            "errors": e.errors()
        }), 400

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)