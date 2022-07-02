cd /app
echo "----- Now trying to run gunicorn ------ " 
gunicorn -b 0.0.0.0:80 app.app:server
