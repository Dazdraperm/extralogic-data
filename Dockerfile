FROM python:3.10-slim-buster

# Stdout and stderr streams to be unbuffered.
ENV PYTHONUNBUFFERED 1

# Workdir path.
WORKDIR usr/app/src

# Copy project.
COPY ./src usr/app/src


# Install requirements to Workdir.
COPY requirements.txt .
RUN pip install -r requirements.txt

# Listens on the specified network ports at runtime.
EXPOSE 8000

# Run server
CMD python usr/app/src/ flask run -h 0.0.0.0 -p 8000
