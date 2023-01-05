from app import db

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    books = db.relationship("Book",secondary="book_genre",back_populates="genres")

    def to_dict(self):
        genre_dict = {
            "id": self.id,
            "name": self.name
        }
        if self.books:
            book_titles = [book.title for book in self.books]
            genre_dict["books"] = book_titles

        return genre_dict

    @classmethod
    def from_dict(cls, genre_data):
        return cls(
            name = genre_data["name"],
        )