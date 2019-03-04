Demo: Speed & Agility
==

Amazon Web Services defines six advantages to cloud computing. This projects demonstrates one of those advantages: **Increase speed and agility**.

> In a cloud computing environment, new IT resources are only a click away, which means that you reduce the time to make those resources available to your developers from weeks to just minutes. This results in a dramatic increase in agility for the organization, since the cost and time it takes to experiment and develop is significantly lower.

Source: [docs.aws.amazon.com][1]

[1]: https://docs.aws.amazon.com/aws-technical-content/latest/aws-overview/six-advantages-of-cloud-computing.html


Traditional approach
--

In an on-premises datacenter, it can take weeks to provision new resources, due to various manual processes and interactions.


Demo #1: Manually deploying on EC2
--

The simplest (and most similar to the traditional approach) way to deploy an application would be to launch an EC2 instance and configure it as a normal VM. When you do this process manually it takes a couple of minutes to get up and running. Already much quicker than a couple of weeks.

Guide: [1-manually-deploy-ec2.md](guides/1-manually-deploy-ec2.md)


Demo #2: Manually deploying with Docker on ECS
--

To avoid reconfiguring every instance, it is possible to create an Amazon Machine Image (AMI). An alternative to is to create a Docker container image and use ECS. When manually building an image, it takes around a minute. However, this image can be used multiple times. A manual deployment can be done in a couple of seconds.

Guide: [2-manually-deploy-docker.md](guides/2-manually-deploy-docker.md)


Demo #3: Automatically deploying Docker on ECS
--

With a CI/CD pipeline it is possible to automate all the steps from Demo #2. The only manual action that is need, is a commit and push to a Git repository, which is most likely already part of the developer workflow. The pipeline will then build a new image and deploy it for you.

Guide: [3-automatically-deploy-docker.md](guides/3-automatically-deploy-docker.md)
