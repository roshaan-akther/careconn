from abc import ABC, abstractmethod
import math

class MatchingStrategy(ABC):
    @abstractmethod
    def match(self, request, volunteers):
        """Return a single (user, profile) tuple or None."""
        pass

def _distance(a, b):
    # simple string-based pseudo-distance: 0 if same location else 1
    return 0 if (a or "").lower() == (b or "").lower() else 1

class NearestStrategy(MatchingStrategy):
    def match(self, request, volunteers):
        if not volunteers:
            return None
        scored = sorted(volunteers, key=lambda vp: _distance(request.location, vp[0].location))
        return scored[0]

class SkillMatchStrategy(MatchingStrategy):
    def match(self, request, volunteers):
        if not volunteers:
            return None
        cat = (request.category or "").lower()
        def score(vp):
            skills = [s.strip().lower() for s in (vp[1].skills or "").split(",") if s.strip()]
            return (0 if cat in skills else 1, -vp[1].rating_avg)
        return sorted(volunteers, key=score)[0]

class AvailabilityStrategy(MatchingStrategy):
    def match(self, request, volunteers):
        if not volunteers:
            return None
        # prefer "anytime" then earliest-ish availability string sort
        def key(vp):
            avail = (vp[1].availability or "").lower()
            return (0 if avail == "anytime" else 1, avail)
        return sorted(volunteers, key=key)[0]

class BalancedStrategy(MatchingStrategy):
    def match(self, request, volunteers):
        if not volunteers:
            return None
        def score(vp):
            dist = _distance(request.location, vp[0].location)
            cat = (request.category or "").lower()
            skills = [s.strip().lower() for s in (vp[1].skills or "").split(",") if s.strip()]
            skill_pen = 0 if cat in skills else 1
            avail_pen = 0 if (vp[1].availability or "").lower() == "anytime" else 1
            rating_pen = -vp[1].rating_avg
            return dist + skill_pen + avail_pen + rating_pen
        return sorted(volunteers, key=score)[0]
