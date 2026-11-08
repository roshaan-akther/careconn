from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.data.repositories import VolunteerRepo

volunteer_bp = Blueprint("volunteers", __name__)

@volunteer_bp.route("/profile", methods=["GET","POST"])
@login_required
def profile():
    if current_user.role != "volunteer":
        flash("Volunteers only", "warning")
        return redirect(url_for("requests.dashboard"))
    vp = VolunteerRepo.profile(current_user.id)
    if request.method == "POST":
        VolunteerRepo.update_profile(current_user.id,
            request.form.get("skills",""), request.form.get("availability","anytime"),
            int(request.form.get("radius_km", 10)))
        flash("Profile updated", "success")
        return redirect(url_for("volunteers.profile"))
    return render_template("volunteer_profile.html", vp=vp)
