cd /app
echo "----- Now trying to run gunicorn ------ " 
CMD gunicorn -b 0.0.0.0:80 app.app:server
