# base image  
FROM python:3.10-slim-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# where your code lives  
WORKDIR /code

# copy whole project to the Docker working directory
COPY herptracker .

# run this command to install all dependencies  
RUN pip install -r requirements.txt  

# port where the Django app runs  
#EXPOSE 8000  
# start server  
#CMD python manage.py runserver