from flask import Blueprint, render_template, request, jsonify

main = Blueprint("main", __name__)

@main.get("/")
def index():
    return render_template("index.html")

@main.post("/api/analyze")
def analyze():
    # Prototype response. Replace this layer with Qualcomm AI Hub / ONNX
    # inference after selecting and benchmarking compatible models.
    data = request.get_json(silent=True) or {}
    business = data.get("business", "Your Business")
    return jsonify({
        "business": business,
        "status": "prototype",
        "insights": [
            "Define a clear primary audience.",
            "Strengthen headline hierarchy in creatives.",
            "Use one prominent call-to-action.",
            "Keep visual styling consistent with the brand profile."
        ]
    })

if __name__ == "__main__":
    from . import create_app
    create_app().run(debug=True)
