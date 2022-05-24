FROM python:3.10-slim-buster

# Stdout and stderr streams to be unbuffered.
ENV PYTHONUNBUFFERED 1


# Set work directory
WORKDIR /usr/app

# Copy project.
COPY . /usr/app


# Install requirements to Workdir.
RUN pip install -r requirements.txt

ENV FLASK_APP=src
# run flask in dev mode
ENV FLASK_ENV=development

## Init db
CMD python -m flask init-db

# Run server
CMD flask run --host=0.0.0.0 --port=$PORT
