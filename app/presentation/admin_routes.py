from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.data.repositories import UserRepo, RequestRepo

admin_bp = Blueprint("admin", __name__)

def admin_only():
    return current_user.is_authenticated and current_user.is_admin

@admin_bp.route("/admin")
@login_required
def admin_dashboard():
    if not admin_only():
        flash("Admin only", "danger")
        return redirect(url_for("requests.dashboard"))
    users = UserRepo.all_users()
    reqs = RequestRepo.all_requests()
    return render_template("admin.html", users=users, reqs=reqs)
