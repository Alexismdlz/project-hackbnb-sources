apache2ctl -D FOREGROUND &
# gunicorn : serveur fait pour la prod, contrairement au serveur de dev de Flask.
# --preload : l'app (et donc le seed de la base) n'est chargée qu'une seule fois
exec gunicorn --workers 4 --preload --bind 127.0.0.1:9001 app:app
