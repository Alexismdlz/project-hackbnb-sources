import re

from flask import Blueprint, abort, request, send_from_directory

uploads_api = Blueprint('uploads', __name__)

# Nom de fichier simple + extension d'image, rien d'autre (pas de / ni de ..)
ALLOWED_NAME = re.compile(r'^[A-Za-z0-9_-]+\.(?:jpg|jpeg|png|webp)$')

@uploads_api.route('/')
def get_upload():
   name = request.args.get("name", "")

   # On refuse tout ce qui ne ressemble pas à un nom d'image
   if not ALLOWED_NAME.fullmatch(name):
      abort(400)

   # send_from_directory empêche de sortir du dossier uploads (404 si absent)
   return send_from_directory('uploads', name)
