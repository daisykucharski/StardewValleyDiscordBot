FROM python:3.9
# Run commands from /api directory inside container
WORKDIR /api
# Copy requirements from local to docker image
COPY ./requirements.txt /api
# Install the dependencies in the docker image
RUN pip3 install -r requirements.txt --no-cache-dir
# Copy everything from the current dir to the image
COPY . .