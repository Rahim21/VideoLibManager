# -----------------------------------------------------------------------------
# Auteurs: HAYAT Rahim et DRIOUCHE Sami
# -----------------------------------------------------------------------------
# routes/movie_route.py
from flask import Blueprint, request, render_template, make_response, g
import requests

movie_blueprint = Blueprint('movie', __name__)


