from app.strategies.matching_strategy import NearestStrategy, SkillMatchStrategy, AvailabilityStrategy, BalancedStrategy

def make_volunteers():
    class U: pass
    class P: pass
    # build tuples (user, profile) via simple objects
    class User:
        def __init__(self, name, location): self.name=name; self.location=location
    class Prof:
        def __init__(self, skills, availability, rating): self.skills=skills; self.availability=availability; self.rating_avg=rating; self.rating_count=1
    v1=(User("Bob","Downtown"),Prof("groceries,driving","weekends",4.0))
    v2=(User("Carol","Uptown"),Prof("tech,forms","anytime",4.5))
    return [v1,v2]

class Req:
    def __init__(self): self.category="groceries"; self.location="Downtown"; self.title="t"

def test_nearest():
    vs=make_volunteers()
    r=NearestStrategy().match(Req(), vs)
    assert r[0].name=="Bob"

def test_skill():
    vs=make_volunteers()
    r=SkillMatchStrategy().match(Req(), vs)
    assert r[0].name=="Bob"

def test_availability():
    vs=make_volunteers()
    r=AvailabilityStrategy().match(Req(), vs)
    assert r[0].name=="Carol"

def test_balanced():
    vs=make_volunteers()
    r=BalancedStrategy().match(Req(), vs)
    assert r is not None

def test_empty():
    assert NearestStrategy().match(Req(), []) is None
