# Setup instructions
First, make sure to rename the "example.env" file to ".env" and replace the environnement informations with your ones in it. You also need to put your own database user and password in the "docker-compose.yaml" file.
Then, you can run the following commands to start the application in your Docker environnement. :
```sh
docker build -t easy_link:latest .
docker-compose up -d
```