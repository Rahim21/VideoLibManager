# -----------------------------------------------------------------------------
# Auteurs: HAYAT Rahim et DRIOUCHE Sami
# -----------------------------------------------------------------------------
# models/user_model.py
class User:
    def __init__(self, id, email, password, nom=None, prenom=None, pseudo=None, age=None):
        self.id = id
        self.email = email
        self.password = password
        self.nom = nom
        self.prenom = prenom
        self.pseudo = pseudo
        self.age = age
