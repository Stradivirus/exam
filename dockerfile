FROM python:3.9

WORKDIR /work/django/exam

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput
#CMD ["gunicorn", "exam.wsgi:application", "--bind", "0.0.0.0:8000"]

CMD ["gunicorn", "exam.wsgi:application", "--bind", "unix:/work/django/exam/run/gunicorn.sock"]
