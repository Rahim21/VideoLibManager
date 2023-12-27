# models/user_model.py
class User:
    def __init__(self, id, nom, prenom, pseudo, email, password, age):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.pseudo = pseudo
        self.email = email
        self.password = password
        self.age = age
