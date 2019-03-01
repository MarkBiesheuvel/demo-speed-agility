
# Demo 2: Automatically deploy with Docker on ECS

## Build the container on local machine

Run build command in `source` directory.
```bash
docker build -t speed-agility .
```

Try out the container locally. The port can be found with the `ps` command.
```bash
docker run -p 0:80 -d speed-agility
docker ps
```

## Push to ECR

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
