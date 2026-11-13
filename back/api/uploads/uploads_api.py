import re

from flask import Blueprint, abort, request, send_from_directory

uploads_api = Blueprint('uploads', __name__)

# Seuls des noms de fichiers simples (pas de "/", pas de "..") avec une
# extension d'image autorisée sont acceptés.
ALLOWED_NAME = re.compile(r'^[A-Za-z0-9_-]+\.(?:jpg|jpeg|png|webp)$')

@uploads_api.route('/')
def get_upload():
   name = request.args.get("name", "")

   # 1. Liste blanche : rejette tout ce qui n'est pas un nom d'image attendu
   if not ALLOWED_NAME.fullmatch(name):
      abort(400)

   # 2. send_from_directory confine la lecture au dossier "uploads"
   #    (safe_join : refuse toute sortie du répertoire) et renvoie 404
   #    si le fichier n'existe pas.
   return send_from_directory('uploads', name)
