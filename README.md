docker-compose up -d --build  
docker-compose exec web python manage.py migrate --noinput 
docker-compose exec web python manage.py createsuperuser

Swagger documentation: http://127.0.0.1:8000/api/doc/