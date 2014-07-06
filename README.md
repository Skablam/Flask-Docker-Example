Flask-Docker-Example
====================

Used with Boot2Docker.

Build the container:

docker build -t=skablam/flask_example .

Run the container with:

docker run -d -P skablam/flask_example python /app.py

Find the ip address that Boot2Docker is using with:

Boot2Docker ip

Then hit the flask app on that ip using port 5000. i.e. 192.168.59.103:5000
