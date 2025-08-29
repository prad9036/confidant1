from flask import Blueprint, jsonify, request
import markdown

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/render-markdown", methods=["POST"])
def render_markdown():
    markdown_text = request.form.get("markdown", "")
    html = markdown.markdown(markdown_text)
    return jsonify(html=html)

