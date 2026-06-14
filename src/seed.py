from models import db, User, Planet, People, Favorite
from app import app

with app.app_context():
    # Limpia la base antes de insertar
    db.drop_all()
    db.create_all()

    # Usuarios
    user1 = User(email="luke@jedi.com", password="1234", is_active=True)
    user2 = User(email="leia@rebel.com", password="1234", is_active=True)

    # Planetas
    tatooine = Planet(name="Tatooine", climate="arid", diameter="10465")
    alderaan = Planet(name="Alderaan", climate="temperate", diameter="12500")

    # Personajes
    luke = People(name="Luke Skywalker", gender="male", height="172")
    leia = People(name="Leia Organa", gender="female", height="150")

    # Favoritos iniciales
    fav1 = Favorite(user=user1, planet=tatooine)
    fav2 = Favorite(user=user1, people=luke)
    fav3 = Favorite(user=user2, planet=alderaan)

    # Guardar en DB
    db.session.add_all([user1, user2, tatooine, alderaan, luke, leia, fav1, fav2, fav3])
    db.session.commit()

    print("✅ Datos iniciales insertados correctamente")
