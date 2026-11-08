from app.data.repositories import UserRepo, RequestRepo, VolunteerRepo, RatingRepo, NotificationRepo
from app.strategies.matching_strategy import (NearestStrategy, SkillMatchStrategy,
    AvailabilityStrategy, BalancedStrategy)

STRATEGIES = {
    "nearest": NearestStrategy,
    "skill": SkillMatchStrategy,
    "availability": AvailabilityStrategy,
    "balanced": BalancedStrategy,
}

class AuthService:
    @staticmethod
    def register(name, email, password, role, location=""):
        if UserRepo.get_by_email(email):
            return None, "Email already registered"
        u = UserRepo.create(name, email, password, role=role, location=location)
        return u, None
    @staticmethod
    def authenticate(email, password):
        u = UserRepo.get_by_email(email)
        if u and u.check_password(password):
            return u
        return None

class MatchingService:
    def __init__(self, strategy_name="balanced"):
        self.set_strategy(strategy_name)
    def set_strategy(self, name):
        cls = STRATEGIES.get(name, BalancedStrategy)
        self.strategy = cls()
        self.strategy_name = name
    def find(self, request):
        volunteers = VolunteerRepo.all_with_profiles()
        # exclude already busy? keep simple: all volunteers
        return self.strategy.match(request, volunteers)

class RequestService:
    @staticmethod
    def create(seeker_id, title, description, category, urgency, location):
        return RequestRepo.create(seeker_id, title, description, category, urgency, location)
    @staticmethod
    def accept(request_id, volunteer_id):
        RequestRepo.update_status(request_id, "assigned", volunteer_id)
        r = RequestRepo.get(request_id)
        NotificationRepo.create(r.seeker_id, f"Your request '{r.title}' was accepted.")
        NotificationRepo.create(volunteer_id, f"You accepted '{r.title}'.")
        return r
    @staticmethod
    def start(request_id):
        return RequestRepo.update_status(request_id, "in_progress")
    @staticmethod
    def complete(request_id):
        r = RequestRepo.update_status(request_id, "completed")
        NotificationRepo.create(r.seeker_id, f"Request '{r.title}' completed. Please rate.")
        return r
    @staticmethod
    def rate(request_id, seeker_id, score, comment):
        r = RequestRepo.get(request_id)
        RatingRepo.create(request_id, r.assigned_volunteer_id, seeker_id, score, comment)
        VolunteerRepo.update_rating(r.assigned_volunteer_id, score)
        NotificationRepo.create(r.assigned_volunteer_id, f"You received a {score}/5 rating.")
        return r
