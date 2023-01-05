from app import db

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    books = db.relationship("Book",secondary="book_genre",back_populates="genres")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

    @classmethod
    def from_dict(cls, genre_data):
        return cls(
            name = genre_data["name"],
        )