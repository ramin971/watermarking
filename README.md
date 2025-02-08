# HOW TO USE...
## Installation

   1. Clone the repository:

    git clone git@github.com:ramin971/watermarking.git

   2. Install the required dependencies:

    pip install -r requirements.txt

   3. Set up the database:

    python manage.py makemigrations
    python manage.py migrate

   4. Create a superuser for accessing the Django admin panel:

    python manage.py createsuperuser

   5. Run the development server:

    python manage.py runserver

   6. Run Redis on Docker:

    docker run --rm --name redis -p 6379:6379 redis

   7. Run Celery:

    celery -A watermarking worker --loglevel=info
