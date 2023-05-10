from webapp import db 

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False)
    about = db.Column(db.Text)
    
    def __init__(self, name, about):
        self.name = name
        self.about = about
        
    def __repr__(self):
        
        return f"{self.name} {self.about}"
