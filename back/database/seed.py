from .init import db
from api.rooms.rooms_models import Room
from api.users.users_models import User


def seed_database():
    # Do not seed database if data already exists
    if User.query.count() > 0 or Room.query.count() > 0:
      return

    db.session.add(User(
        id=1,
        name="John Doe",
        email="john@doe.com",
        password_hash="XX",
    ))

    db.session.add(Room(
        id=1,
        title="Nature, Spa & bien-être au Châtaignier",
        city="Hersin-Coupigny, France",
        price=170,
        picture="room-1.jpg",
        category="swimming-pool",
        description="<p>Spa idéal pour se détendre !</p>",
        host_user_id=1,
    ))

    db.session.add(Room(
        id=2,
        title="Loft lumineux en centre-ville",
        city="Lille, France",
        price=95,
        picture="room-2.jpg",
        category="swimming-pool",
        description="<p>Loft moderne, idéal pour les courts séjours. <em>Proche des transports</em>.</p>",
        host_user_id=1,
    ))

    db.session.add(Room(
        id=3,
        title="Chalet cosy avec vue montagne",
        city="Chamonix, France",
        price=220,
        picture="room-3.jpg",
        category="ski",
        description="<p>Chalet chaleureux, cheminée, et accès direct aux sentiers.</p>",
        host_user_id=1,
    ))

    db.session.add(Room(
        id=4,
        title="Appartement plage & coucher de soleil",
        city="Nice, France",
        price=150,
        picture="room-4.jpg",
        category="seaside",
        description="<p>Balcon face à la mer — parfait pour se détendre au soleil.</p>",
        host_user_id=1,
    ))

    db.session.add(Room(
        id=5,
        title="Villa Provençale avec piscine privée",
        city="Aix-en-Provence, France",
        price=320,
        picture="room-5.jpg",
        category="swimming-pool",
        description="<p>Grande villa, jardin arboré, piscine et cuisine extérieure.</p>",
        host_user_id=1,
    ))

    db.session.add(Room(
        id=6,
        title="Studio design près des musées",
        city="Paris, France",
        price=120,
        picture="room-6.jpg",
        category="city",
        description="<p>Studio compact et stylé, parfait pour découvrir la ville.</p>",
        host_user_id=1,
    ))

    db.session.add(Room(
        id=7,
        title="Maison de campagne & calme absolu",
        city="Saint-Rémy-de-Provence, France",
        price=135,
        picture="room-7.jpg",
        category="hut",
        description="<p>Retraite paisible, jardins et sentiers à proximité.</p>",
        host_user_id=1,
    ))

    db.session.add(Room(
        id=8,
        title="Nid romantique pour escapade en duo",
        city="Colmar, France",
        price=110,
        picture="room-8.jpg",
        category="hut",
        description="<p>Intime et charmant, idéal pour les couples.</p>",
        host_user_id=1,
    ))

    db.session.add(Room(
        id=9,
        title="Appartement ski-in / ski-out",
        city="Val-d'Isère, France",
        price=260,
        picture="room-9.jpg",
        category="ski",
        description="<p>Accès direct aux pistes, local à skis et sauna.</p>",
        host_user_id=1,
    ))

    db.session.add(Room(
        id=10,
        title="Grand loft industriel & espace coworking",
        city="Lyon, France",
        price=140,
        picture="room-10.jpg",
        category="loft",
        description="<p>Loft spacieux avec coin travail, fibre haut débit.</p>",
        host_user_id=1,
    ))

    db.session.commit()
