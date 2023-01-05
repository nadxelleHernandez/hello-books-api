from app import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable = False)
    books = db.relationship("Book", back_populates="author")

    def to_dict(self):
        book_dict = {
            "id": self.id,
            "name": self.name
        }
        book_dict["books"] = [book.title for book in self.books]
        return book_dict

    @classmethod
    def from_dict(cls, author_data):
        return cls(
            name = author_data["name"],
        )