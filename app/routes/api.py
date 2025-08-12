from flask import Blueprint, request, jsonify
import markdown

api_bp = Blueprint("api", __name__, url_prefix="/api")

@api_bp.route("/markdown", methods=["POST"])
def render_markdown():
    md = request.form.get("markdown", "")
    html = markdown.markdown(md)
    return jsonify({"html": html})
