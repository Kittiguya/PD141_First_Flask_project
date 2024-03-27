from app import db



class GamesModel(db.Model):
        __tablename__ = 'games'

        id = db.Column(db.Integer, primary_key = True)
        name = db.Column(db.String(50), nullable=False, unique=True)
        description = db.Column(db.String(150), nullable=False, unique=True)
        studio = db.Column(db.String(75))
        

        def save_games(self):
                db.session.add(self)
                db.session.commit()

        def delete_games(self):
                db.session.delete(self)
                db.session.commit()
        