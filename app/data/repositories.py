from app import db
from app.domain.models import User, VolunteerProfile, HelpRequest, Rating, Notification

class UserRepo:
    @staticmethod
    def get_by_id(uid):
        return User.query.get(uid)
    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()
    @staticmethod
    def create(name, email, password, role="seeker", location=""):
        u = User(name=name, email=email, role=role, location=location)
        u.set_password(password)
        db.session.add(u)
        db.session.commit()
        if role == "volunteer":
            vp = VolunteerProfile(user_id=u.id)
            db.session.add(vp)
            db.session.commit()
        return u
    @staticmethod
    def all_users():
        return User.query.all()
    @staticmethod
    def volunteers():
        return User.query.filter_by(role="volunteer").all()

class RequestRepo:
    @staticmethod
    def create(seeker_id, title, description, category, urgency, location):
        r = HelpRequest(seeker_id=seeker_id, title=title, description=description,
                        category=category, urgency=urgency, location=location)
        db.session.add(r)
        db.session.commit()
        return r
    @staticmethod
    def get(rid):
        return HelpRequest.query.get(rid)
    @staticmethod
    def all_open():
        return HelpRequest.query.filter_by(status="open").order_by(HelpRequest.created_at.desc()).all()
    @staticmethod
    def all_requests():
        return HelpRequest.query.order_by(HelpRequest.created_at.desc()).all()
    @staticmethod
    def by_seeker(uid):
        return HelpRequest.query.filter_by(seeker_id=uid).order_by(HelpRequest.created_at.desc()).all()
    @staticmethod
    def by_volunteer(uid):
        return HelpRequest.query.filter_by(assigned_volunteer_id=uid).order_by(HelpRequest.created_at.desc()).all()
    @staticmethod
    def update_status(rid, status, volunteer_id=None):
        r = HelpRequest.query.get(rid)
        if r:
            r.status = status
            if volunteer_id is not None:
                r.assigned_volunteer_id = volunteer_id
            db.session.commit()
        return r

class VolunteerRepo:
    @staticmethod
    def profile(uid):
        return VolunteerProfile.query.get(uid)
    @staticmethod
    def update_profile(uid, skills, availability, radius_km):
        vp = VolunteerProfile.query.get(uid)
        if not vp:
            vp = VolunteerProfile(user_id=uid)
            db.session.add(vp)
        vp.skills = skills
        vp.availability = availability
        vp.radius_km = radius_km
        db.session.commit()
        return vp
    @staticmethod
    def all_with_profiles():
        vols = User.query.filter_by(role="volunteer").all()
        out = []
        for v in vols:
            vp = v.volunteer_profile
            if vp is None:
                vp = VolunteerProfile(user_id=v.id)
                db.session.add(vp)
                db.session.commit()
            out.append((v, vp))
        return out
    @staticmethod
    def update_rating(uid, score):
        vp = VolunteerProfile.query.get(uid)
        if vp:
            vp.rating_count += 1
            vp.rating_avg = ((vp.rating_avg * (vp.rating_count-1)) + score) / vp.rating_count
            db.session.commit()

class RatingRepo:
    @staticmethod
    def create(request_id, volunteer_id, seeker_id, score, comment):
        rt = Rating(request_id=request_id, volunteer_id=volunteer_id,
                    seeker_id=seeker_id, score=score, comment=comment)
        db.session.add(rt)
        db.session.commit()
        return rt

class NotificationRepo:
    @staticmethod
    def create(user_id, message):
        n = Notification(user_id=user_id, message=message)
        db.session.add(n)
        db.session.commit()
        return n
    @staticmethod
    def for_user(uid):
        return Notification.query.filter_by(user_id=uid).order_by(Notification.created_at.desc()).limit(20).all()
    @staticmethod
    def mark_read(nid):
        n = Notification.query.get(nid)
        if n:
            n.read = True
            db.session.commit()
        return n
    @staticmethod
    def unread_count(uid):
        return Notification.query.filter_by(user_id=uid, read=False).count()
    @staticmethod
    def mark_all_read(uid):
        Notification.query.filter_by(user_id=uid, read=False).update({"read": True})
        db.session.commit()
