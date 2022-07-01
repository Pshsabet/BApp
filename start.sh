cd /app
echo "----- Now trying to run gunicorn ------ " 
CMD gunicorn -b :5000 --reload --access-logfile - --error-logfile - app:app 
