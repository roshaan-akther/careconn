from flask import Blueprint, render_template

learn_bp = Blueprint("learn", __name__)

@learn_bp.route("/learn")
def learn():
    return render_template("learn.html")
