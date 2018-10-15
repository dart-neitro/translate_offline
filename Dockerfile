# official image
FROM python:3.6-slim

## install requirements

# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
ADD ./application/requirements /app/requirements
# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements/dev.txt

# COPY run_service file
COPY ./run_service.sh /run/run_service.sh
RUN sed -i 's/\r//' /run/run_service.sh
RUN chmod +x /run/run_service.sh

# mount folder

ENTRYPOINT ["sh", "/run/run_service.sh"]
