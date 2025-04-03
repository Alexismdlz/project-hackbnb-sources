from database.init import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Booking(db.Model):
    __tablename__ = 'bookings'

    id: Mapped[int] = mapped_column(primary_key=True)
    reference: Mapped[str] = mapped_column(index=True)
    arrival_date: Mapped[str] = mapped_column()
    departure_date: Mapped[str] = mapped_column()
    guests_count: Mapped[int] = mapped_column()
    total_price: Mapped[float] = mapped_column()
    checkout_confirmation_secret: Mapped[str] = mapped_column()
    stripe_checkout_session_id: Mapped[str] = mapped_column(index=True)
    is_paid: Mapped[bool] = mapped_column()
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"), index=True)
    room: Mapped["Room"] = relationship('Room', back_populates="bookings")

    def __repr__(self):
        return f'<Booking {self.id!r}>'
    
    def to_dict(self):
        output = {
            "id": self.id,
            "reference": self.reference,
            "is_paid": self.is_paid,
            "arrival_date": self.arrival_date,
            "departure_date": self.departure_date,
            "guests_count": self.guests_count,
            "total_price": self.total_price,
            "stripe_checkout_session_id": self.stripe_checkout_session_id,
        }

        if self.room:
            output["room"] = self.room.to_dict()

        return output
