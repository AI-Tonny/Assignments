from flask import jsonify
from app import create_app

app = create_app()

@app.route("/")
def root():
    return jsonify({
        "status": 200,
        "success": True,
        "message": "API is working"
    })

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)