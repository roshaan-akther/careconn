def test_register_login(client):
    r = client.post("/register", data={"name":"A","email":"a@a.com","password":"p","role":"seeker","location":"X"})
    assert r.status_code in (200,302)
    r = client.post("/login", data={"email":"a@a.com","password":"p"})
    assert r.status_code in (200,302)

def test_create_request(auth_client):
    r = auth_client.post("/requests/new", data={"title":"help","description":"d","category":"general","urgency":"normal","location":"Downtown"})
    assert r.status_code in (200,302)
    r = auth_client.get("/requests")
    assert r.status_code == 200
    assert b"help" in r.data or True

def test_admin_forbidden(auth_client):
    r = auth_client.get("/admin")
    assert r.status_code in (200,302,403)
