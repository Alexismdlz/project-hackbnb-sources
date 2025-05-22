from flask import Blueprint, request, send_file

uploads_api = Blueprint('uploads', __name__)

@uploads_api.route('/')
def get_upload():
   return send_file('uploads/' + request.args.get("name"))
 