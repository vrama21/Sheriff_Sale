## Local Setup
- Start local database

    `sudo pg_ctlcluster 13 main start`

- Check local databases
  
    `psql -l`

- Start a gunicorn server

    `gunicorn wsgi:app`

