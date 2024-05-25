# Hello Postgres
Install Postgres using docker-compose and consume using python code

### Installing Postgres
Open terminal session in the same folder as docker-compose.yml file

Execute the docker compose command, this will download Postgres and install in local docker
```bash docker-compose up -d```

Verify the container is running 
```bash docker ps```

View container logs
```bash docker logs postgres```

Stop the container (when needed)
```bash docker-compose down```

### Access Postgres database through DBeaver
Open DBeaver application (incase need to install, https://dbeaver.io/download/)

Select "New Database Connection" -> Choose "PostgreSQL" 

Fill connection details:

    - Host: localhost

    - Port: 5432

    - Database: citizix_db

    - Username: citizix_user

    - Password: S3cret

Click "Test Connection" to verify the connection 

And Finish

### Create table and retrieve data from Postgres using python
Follow the jupyter notebook code 