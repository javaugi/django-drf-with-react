https://www.valentinog.com/blog/tutorial-api-django-rest-react/

https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv

https://hackernoon.com/creating-websites-using-react-and-django-rest-framework-b14c066087c7

https://github.com/valentinogagliardi/django-drf-react-quickstart

https://gist.github.com/jpalala/01226fd38fbb421279ef97d62d394c23

related commands
1. pipenv install django djangorestframework
2. pipenv shell
3. django-admin startproject project
4. django-admin startapp app_name
5. django-admin startapp leads in th eproject folder
6. python manage.py makemigrations leads
7. python manage.py migrate
8. pipenv install coverage --dev
9. coverage run --source='.' manage.py test
10. coverage html
11. coverage report
12. python manage.py runserver

Development

    Install Python dependencies: pipenv install
    Install Javascript dependencies: npm i
    Make the bundle: npm run dev
    Migrate: pipenv run python ./project/manage.py migrate
    Populate the database: pipenv run python ./project/manage.py loaddata leads
    Run locally: pipenv run python ./project/manage.py runserver
    Head over http://127.0.0.1:8000/

Test

    Unit: cd project && pipenv run python manage.py test
    E2E: npm run e2e
    Coverage: cd project && pipenv run coverage run manage.py test

Production

    Make the bundle: npm run build
    ... TODO

TODO

    Authentication
    React routing
    Production

