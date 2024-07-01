from app import db



class GenresModel(db.Model):
    __tablename__ = 'genre'

    
    genre = db.Column(db.String(50), primary_key=True)


    def save_genre(self):
        db.session.add(self)    
        db.session.commit()    
        
    def delete_genre(self):
        db.session.delete(self)
        db.session.commit()



