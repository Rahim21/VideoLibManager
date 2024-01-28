# -----------------------------------------------------------------------------
# Auteurs: HAYAT Rahim et DRIOUCHE Sami
# -----------------------------------------------------------------------------
# models/user_model.py
class User:
    def __init__(self, id, email, password, nom=None, prenom=None, pseudo=None, age=None, role="user", profile_picture=None, is_active=True):
        self.id = id
        self.email = email
        self.password = password
        self.nom = nom
        self.prenom = prenom
        self.pseudo = pseudo
        self.age = age
        self.role = role
        self.profile_picture = profile_picture
        self.is_active = is_active