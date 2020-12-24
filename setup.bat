pip3 install -r requirements.txt
python ./setupfiles/dotenv_setup.py
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput