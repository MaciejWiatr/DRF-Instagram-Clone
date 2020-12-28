pip3 install -r requirements.txt
python ./setupfiles/dotenv_setup.py
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python ./manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')"
