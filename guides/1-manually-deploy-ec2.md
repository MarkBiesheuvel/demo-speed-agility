
Demo 1: Manually deploying on EC2
==


Go through the EC2 launch wizard.
--

Select the Amazon Linux 2 AMI, select a public subnet and a security group that allows HTTP from anywhere.


Configure the EC2 instance
--

Login via SSH or via SSM Session Manager

Switch to root.
```bash
sudo su -
```

Install git and python.
```bash
yum install -y git python3
```

Download the source code of this project.
```bash
git clone https://github.com/MarkBiesheuvel/demo-speed-agility.git
```

Change directory to the source code.
```bash
cd demo-speed-agility/source/
```

Install python dependencies
```bash
python3 -m pip install -r requirements.txt
```

Run the webserver on port 80
```bash
gunicorn -w 4 app:app -b 0.0.0.0:80
```


Visit the webpage
--

Open the public IP address of the EC2 instance in your browser.
