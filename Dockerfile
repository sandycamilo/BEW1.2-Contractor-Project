FROM python:3.7

# # The enviroment variable ensures that the python output is set straight
# # to the terminal with out buffering it first
 ENV PYTHONUNBUFFERED 1

# # create root directory for our project in the container
 RUN mkdir /journal

# # Set the working directory
 WORKDIR /journal

# # Copy the current directory contents into the container
COPY . /journal/

# # Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# # exposing to traffic
EXPOSE 8080 80 443

# # Run a startup script in the specified directory.
# HEALTHCHECK CMD curl --fail http://0.0.0.0:8000/ || exit 1

# # running the server
 ENTRYPOINT ["python3"]
 CMD ["manage.py", "runserver", "0.0.0.0:8080"]