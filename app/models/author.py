from app import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable = False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

    @classmethod
    def from_dict(cls, author_data):
        return cls(
            name = author_data["name"],
        )