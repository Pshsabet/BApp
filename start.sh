cd /app
echo "----- Now trying to run gunicorn ------ " 
CMD gunicorn app.app:server
