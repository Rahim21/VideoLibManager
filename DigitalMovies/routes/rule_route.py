# -----------------------------------------------------------------------------
# Auteurs: HAYAT Rahim et DRIOUCHE Sami
# -----------------------------------------------------------------------------
# routes/rule_route.py
from flask import Blueprint, render_template, redirect, url_for, request, g
from functools import wraps

rule_blueprint = Blueprint('rule', __name__)

# Liste des routes avec la possibilité d'avoir ou non un token sans redirection
exempt_routes = ['page.index']

def require_token(view_func):
    @wraps(view_func)
    def decorated_function(*args, **kwargs):
        g.token = request.cookies.get('token')

        # Vérifie si la route actuelle est exemptée d'exigence de token
        if request.endpoint in exempt_routes:
            return view_func(*args, **kwargs)
        
        # Sinon, redirige vers la page d'inscription si le token n'est pas présent
        return view_func(*args, **kwargs) if g.token else redirect(url_for('page.login'))

    return decorated_function