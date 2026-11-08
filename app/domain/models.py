from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="seeker")  # seeker/volunteer/admin
    location = db.Column(db.String(120), default="")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, pw):
        self.password_hash = generate_password_hash(pw)

    def check_password(self, pw):
        return check_password_hash(self.password_hash, pw)

    @property
    def is_admin(self):
        return self.role == "admin"

class VolunteerProfile(db.Model):
    __tablename__ = "volunteer_profiles"
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    skills = db.Column(db.String(255), default="")
    availability = db.Column(db.String(100), default="anytime")
    radius_km = db.Column(db.Integer, default=10)
    rating_avg = db.Column(db.Float, default=0.0)
    rating_count = db.Column(db.Integer, default=0)
    user = db.relationship("User", backref=db.backref("volunteer_profile", uselist=False))

class HelpRequest(db.Model):
    __tablename__ = "help_requests"
    id = db.Column(db.Integer, primary_key=True)
    seeker_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, default="")
    category = db.Column(db.String(50), default="general")
    urgency = db.Column(db.String(20), default="normal")
    location = db.Column(db.String(120), default="")
    status = db.Column(db.String(20), default="open")  # open/assigned/in_progress/completed
    assigned_volunteer_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    seeker = db.relationship("User", foreign_keys=[seeker_id], backref="requests_made")
    volunteer = db.relationship("User", foreign_keys=[assigned_volunteer_id])

class Rating(db.Model):
    __tablename__ = "ratings"
    id = db.Column(db.Integer, primary_key=True)
    request_id = db.Column(db.Integer, db.ForeignKey("help_requests.id"), nullable=False)
    volunteer_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    seeker_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, default="")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Notification(db.Model):
    __tablename__ = "notifications"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    message = db.Column(db.String(255), nullable=False)
    read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
