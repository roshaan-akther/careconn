from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.services.services import AuthService

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        u, err = AuthService.register(
            request.form.get("name"), request.form.get("email"),
            request.form.get("password"), request.form.get("role","seeker"),
            request.form.get("location",""))
        if err:
            flash(err, "danger")
            return redirect(url_for("auth.register"))
        flash("Registered. Please log in.", "success")
        return redirect(url_for("auth.login"))
    return render_template("register.html")

@auth_bp.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        u = AuthService.authenticate(request.form.get("email"), request.form.get("password"))
        if u:
            login_user(u)
            return redirect(url_for("requests.dashboard"))
        flash("Invalid credentials", "danger")
    return render_template("login.html")

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
