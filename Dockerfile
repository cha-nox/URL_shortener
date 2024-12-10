# Getting official Python image
FROM python:3.12-slim

# Defining the working directory
WORKDIR /easy_link

# Copying the requirements file into the container
COPY requirements.txt requirements.txt

# Keeping Package Installer for Python up to date
RUN python3 -m pip install --upgrade pip

# Installing Python dependencies into the container
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Copying the application itself into the container
COPY . .

# Removing the requirements file
RUN rm requirements.txt

# Exposing the port required by the application
EXPOSE 5001

# Making the init script executable
RUN chmod +x init.sh

# Defining the running command
CMD ["./init.sh"]