cd /app
echo "----- Now trying to run gunicorn ------ " 
CMD [ "gunicorn", "--workers=5", "--threads=1", "-b 5000", "app:server"]
