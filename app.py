"""Web interface for the password strength checker."""

from flask import Flask, render_template, request

from src.password_checker import evaluate_password

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    """Show the form and, after sending it, the result."""
    level = None
    reasons = []
    error = None

    if request.method == "POST":
        password = request.form["password"]
        try:
            level, reasons = evaluate_password(password)
        except ValueError as e:
            error = str(e)

    return render_template("index.html", level=level, reasons=reasons, error=error)


if __name__ == "__main__":
    app.run(debug=True)