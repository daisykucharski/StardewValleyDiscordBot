FROM python:3.9
# Run commands from /bot directory inside container
WORKDIR /bot
# Copy requirements from local to docker image
COPY ./requirements.txt /bot
# Install the dependencies in the docker image
RUN pip3 install -r requirements.txt --no-cache-dir
# Copy everything from the current dir to the image
COPY . .