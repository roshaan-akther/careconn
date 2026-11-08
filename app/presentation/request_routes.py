from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.data.repositories import RequestRepo, NotificationRepo
from app.services.services import RequestService, MatchingService
from app.data.repositories import VolunteerRepo

request_bp = Blueprint("requests", __name__)
ms = MatchingService("balanced")

@request_bp.route("/")
@login_required
def dashboard():
    if current_user.role == "seeker":
        reqs = RequestRepo.by_seeker(current_user.id)
    elif current_user.role == "volunteer":
        reqs = RequestRepo.by_volunteer(current_user.id)
        open_reqs = RequestRepo.all_open()
    else:
        reqs = RequestRepo.all_requests()
        open_reqs = []
    unread = NotificationRepo.unread_count(current_user.id)
    return render_template("dashboard.html", reqs=reqs, open_reqs=open_reqs if current_user.role=="volunteer" else [],
                          unread=unread)

@request_bp.route("/requests")
@login_required
def list_requests():
    reqs = RequestRepo.all_open()
    return render_template("requests_list.html", reqs=reqs)

@request_bp.route("/requests/new", methods=["GET","POST"])
@login_required
def new_request():
    if current_user.role != "seeker":
        flash("Only seekers can post requests", "warning")
        return redirect(url_for("requests.dashboard"))
    if request.method == "POST":
        r = RequestService.create(
            current_user.id, request.form.get("title"), request.form.get("description"),
            request.form.get("category"), request.form.get("urgency"), request.form.get("location") or current_user.location)
        # auto-match
        match = ms.find(r)
        suggested = match[0].id if match else None
        flash("Request created. Suggested volunteer assigned by strategy.", "success")
        return redirect(url_for("requests.detail", rid=r.id))
    return render_template("request_form.html")

@request_bp.route("/requests/<int:rid>")
@login_required
def detail(rid):
    r = RequestRepo.get(rid)
    if not r:
        flash("Not found", "danger")
        return redirect(url_for("requests.dashboard"))
    match = None
    if r.status == "open":
        match = ms.find(r)
    return render_template("request_detail.html", r=r, match=match)

@request_bp.route("/requests/<int:rid>/accept", methods=["POST"])
@login_required
def accept(rid):
    volunteer_id = int(request.form.get("volunteer_id", current_user.id))
    RequestService.accept(rid, volunteer_id)
    flash("Accepted", "success")
    return redirect(url_for("requests.detail", rid=rid))

@request_bp.route("/requests/<int:rid>/start", methods=["POST"])
@login_required
def start(rid):
    RequestService.start(rid)
    flash("Started", "success")
    return redirect(url_for("requests.detail", rid=rid))

@request_bp.route("/requests/<int:rid>/complete", methods=["POST"])
@login_required
def complete(rid):
    RequestService.complete(rid)
    flash("Completed", "success")
    return redirect(url_for("requests.detail", rid=rid))

@request_bp.route("/requests/<int:rid>/rate", methods=["POST"])
@login_required
def rate(rid):
    score = int(request.form.get("score", 5))
    comment = request.form.get("comment", "")
    RequestService.rate(rid, current_user.id, score, comment)
    flash("Thanks for rating!", "success")
    return redirect(url_for("requests.detail", rid=rid))

@request_bp.route("/strategy", methods=["POST"])
@login_required
def set_strategy():
    ms.set_strategy(request.form.get("strategy", "balanced"))
    flash(f"Strategy set to {request.form.get('strategy')}", "success")
    return redirect(url_for("requests.dashboard"))

@request_bp.route("/notifications")
@login_required
def notifications():
    ns = NotificationRepo.for_user(current_user.id)
    return render_template("notifications.html", notifications=ns)
