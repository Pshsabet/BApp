cd /app
echo "----- Now trying to run gunicorn ------ " 
CMD [ "gunicorn", "--workers=5", "--threads=1", "-b 0.0.0.0:80", "app:server"]
