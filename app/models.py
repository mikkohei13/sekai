import enum
from datetime import datetime, timezone

from app import db


class Sex(enum.Enum):
    male = "male"
    female = "female"
    other = "other"


class Character(db.Model):
    __tablename__ = "characters"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    sex = db.Column(db.Enum(Sex, name="sex_enum"), nullable=False)
    image_path = db.Column(db.String(500), nullable=True)
    created_at = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )

    def __repr__(self) -> str:
        return f"<Character {self.name!r}>"
