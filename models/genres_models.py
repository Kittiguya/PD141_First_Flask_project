from app import db



class GenresModel(db.Model):
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key = True)
    genre = db.Column(db.String(50), nullable=False, unique=True)


def save_genre(self):
        db.session.add(self)
        db.session.commit()

def delete_genre(self):
        db.session.delete(self)
        db.session.commit()