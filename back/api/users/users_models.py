from typing import List
from database.init import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import Mapped, mapped_column, relationship

class User(db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str] = mapped_column()
    rooms: Mapped[List["Room"]] = relationship(back_populates="host_user")

    def __repr__(self):
        return f'<User {self.email!r}>'
    
    def to_dict(self):
        # Version publique (affichée comme hôte sur les logements) : pas d'e-mail
        return {
            "id": self.id,
            "name": self.name,
        }

    def to_private_dict(self):
        # Seulement pour l'utilisateur lui-même (/users/me)
        return {
            **self.to_dict(),
            "email": self.email,
        }

    def set_password(self, clear_password: str):
        # Avant : md5 sans sel, cassable en quelques secondes avec une rainbow table.
        # generate_password_hash utilise scrypt avec un sel aléatoire par utilisateur.
        self.password_hash = generate_password_hash(clear_password)

    def is_valid_password(self, clear_password: str) -> bool:
        # Comparaison en temps constant, le sel et l'algo sont lus dans le hash stocké
        return check_password_hash(self.password_hash, clear_password)
