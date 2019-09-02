
Demo 2: Manually deploying with Docker on ECS
==

Build the container on local machine
--

Run build command in project root directory.
```bash
docker build -t speed-agility ./source
```

Try out the container locally. The port can be found with the `ps` command.
```bash
docker run -p 0:80 -d speed-agility
docker ps
```

Create a container repository
--

Go to ECR. Click "Create repository". Fill in the name `speed-agility` and finish.

Push to the repository
--

Login to ECR.
```bash
$(aws ecr get-login --no-include-email)
```

Tag the image. Fill in `account_id` and `region`.
```bash
docker tag speed-agility:latest {account_id}.dkr.ecr.{region}.amazonaws.com/speed-agility:latest
```

Push the image. Fill in `account_id` and `region`.
```bash
docker push {account_id}.dkr.ecr.{region}.amazonaws.com/speed-agility:latest
```

Create a new task definition
--

Go to "ECS > Task Definitions". Click "Create new Task Definition".
Select "FARGATE". Name: `speed-agility`. Role: `None`. Any Memory and CPU option.

Click "Add container". Name: `speed-agility`. Image `{account_id}.dkr.ecr.{region}.amazonaws.com/speed-agility:latest`. Click "Add port mapping", enter `80`.

Launch task
--

Go to "ECS > Clusters". Create a "Networking only" cluster if none exist.

Open the cluster and go to "Tasks" tab. Click "Run new Task". Launch type: `FARGATE`. Task definition: `speed-agility:1`. Any VPC and public subnet combination. Auto-assign public IP: `ENABLED`. Click "Run Task".

Wait for the container to transition in the "RUNNING" state and open the public ip in your browser.
