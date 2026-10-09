from app.models import Hero

def test_create_hero(client):
    r = client.post("/api/v1/heroes", json={"name": "Deadpond", "secret_name": "Dive Wilson"})
    assert r.status_code == 201
    assert r.json()["status"] == "active"
    assert "secret_name" not in r.json()

def test_update_hero_partial(session, client):
    hero = Hero(name="Tony", secret_name="Iron Man", age=45)
    session.add(hero)
    session.commit()
    r = client.patch(f"/api/v1/heroes/{hero.id}", json={"status": "retired"})
    assert r.json()["age"] == 45 and r.json()["status"] == "retired"

def test_hero_unknown_team(client):
    r = client.post("/api/v1/heroes", json={"name": "A", "secret_name": "a", "team_id": 999})
    assert r.status_code == 400