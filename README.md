# Django blog example

This repo contains the code from my Django introduction talk at GDS. It's a very simple blog, meant only to 
demonstrate how to get up and running with Django.

## Steps

These assume you already have a working Python installation (2.7 or 3.4+), including `virtualenv`. If not these can be installed via your system's package manager, eg Homebrew.

1. Clone the code:

        git clone https://github.com/danielroseman/gds_blog.git

2. Create a new virtualenv and activate it:

        cd gds_blog
        virtualenv .
        . bin/activate

3. Install the requirements (currently, only Django 1.8):

        pip install -r requirements.txt

4. Create the database tables (this will use an sqlite3 file for simplicity):

        ./manage.py migrate

5. Create a superuser to access the admin site:

        ./manage.py createsuperuser

6. Run the server:

        ./manage.py runserver

You can now go to http://127.0.0.1:8000 to view the site, and http://127.0.0.1:8000/admin/ for the admin interface. You can also run a Python shell to interact directly with the code by doing `./manage.py shell`.
