3atmospheres.com old site
=========================

This is 3atmospheres' old website.

Requirements
------------

The following are the bare requirements.  The versions are not the minimum requirements -- only what we have currently tested on.

* Python v2.7.1
* PostgreSQL v8.4

The following are optional requirements; however, it is highly recommended to run the site in a virtual environment to get up and running quicker with ease.

* pip
* virtualenv
* virtualenvwrapper

Codebase
---------

Install
-------

> Please note: If you have chosen not to install pip, virtualenv, and/or virtualenvwrapper, you can skip the rest of this documentation and go straight to installing all the third party packages found in `requirements.txt`.

After you have cloned the `atmospheres_site` repository, you can install all the dependencies using pip in a virtual environment.

First, create the virtual environment:

    $ mkvirtualenv atmospheres_site

In the `atmospheres_site` directory, install the dependencies using pip and the `requirements.txt` file:

    (atmospheres_site) $ pip install -E requirements.txt

This should take care of all the dependencies for `atmospheres_site`.  Copy the `local_settings.py.sample` file and rename to `local_settings.py`:

    (atmospheres_site) $ cp local_settings.py.sample local_settings.py

Modify the contents of `local_settings.py`:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',    # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'atmospheres_site',                            # Or path to database file if using sqlite3.
            'USER': 'postgres',                                    # Not used with sqlite3.
            'PASSWORD': 'postgres',                                # Not used with sqlite3.
            'HOST': '',                                            # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                                            # Set to empty string for default. Not used with sqlite3.
        }
    }

Next, you'll need to create the PostgreSQL database with the `name` you provided and grant the `user` with all privileges to the database.

When this is complete, you should be able to sync the database and create the core tables, as well as create your local superuser for the application:

    (atmospheres_site) $ python manage.py syncdb

Finally, you should be able to run builtin Django server locally to see the site at 127.0.0.1:8000

    (atmospheres_site) $ python manage.py runserver

Deployment
----------
