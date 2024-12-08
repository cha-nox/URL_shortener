# Setup instructions
First, make sure to rename the "example.env" file to ".env".
Then, replace the environnement informations with your ones in both the .env file and in the docker-compose.yaml file.
Once done, you can run the following commands to start the application in your Docker environnement. :
```sh
docker build -t easy_link:latest .
docker-compose up -d
```