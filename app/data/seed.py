from app import db
from app.domain.models import User, VolunteerProfile, HelpRequest
from app.data.repositories import UserRepo, VolunteerRepo, RequestRepo

SL_LOCATIONS = ["Colombo", "Gampaha", "Kandy", "Galle", "Jaffna", "Matara", "Negombo", "Kurunegala"]

def seed_if_empty():
    if User.query.count() > 0:
        return
    admin = UserRepo.create("Admin", "admin@care.com", "admin123", role="admin", location="Colombo")

    seekers = [
        ("Nimal Perera", "nimal@care.com", "pass123", "Colombo"),
        ("Kamala Silva", "kamala@care.com", "pass123", "Gampaha"),
        ("Sunil Fernando", "sunil@care.com", "pass123", "Kandy"),
        ("Priya Raj", "priya@care.com", "pass123", "Jaffna"),
    ]
    for name, email, pw, loc in seekers:
        UserRepo.create(name, email, pw, role="seeker", location=loc)

    vols = [
        ("Rohan Jayasinghe", "rohan@care.com", "pass123", "Colombo", "groceries,driving,forms", "weekends"),
        ("Dilani Wickramasinghe", "dilani@care.com", "pass123", "Gampaha", "tech,forms", "evenings"),
        ("Kasun Bandara", "kasun@care.com", "pass123", "Kandy", "driving,repairs", "anytime"),
        ("Tharushi De Silva", "tharushi@care.com", "pass123", "Galle", "groceries,companionship", "weekdays"),
        ("Arjun Kumar", "arjun@care.com", "pass123", "Jaffna", "tech,driving", "anytime"),
    ]
    for name, email, pw, loc, skills, avail in vols:
        u = UserRepo.create(name, email, pw, role="volunteer", location=loc)
        VolunteerRepo.update_profile(u.id, skills, avail, 15)

    # seed requests
    seeker_users = [u for u in User.query.filter_by(role="seeker").all()]
    sample_reqs = [
        ("Need groceries picked up", "Elderly, need weekly groceries from supermarket", "groceries", "normal", "Colombo"),
        ("Help filling scholarship form", "Need assistance with online application", "forms", "high", "Kandy"),
        ("Broken tap repair", "Kitchen tap leaking, need a hand", "repairs", "normal", "Gampaha"),
        ("Lonely, would love a chat", "Isolated senior, looking for companionship", "companionship", "low", "Galle"),
        ("Laptop not working", "Need help fixing slow laptop", "tech", "normal", "Jaffna"),
    ]
    for i, (t, d, c, u, loc) in enumerate(sample_reqs):
        s = seeker_users[i % len(seeker_users)]
        RequestRepo.create(s.id, t, d, c, u, loc)
