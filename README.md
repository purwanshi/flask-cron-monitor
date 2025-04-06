#systemD set up !!
create file-  sudo nano /etc/systemd/system/flask_app.service
//
[Unit]
Description=Gunicorn instance to serve Flask App
After=network.target

[Unit]
Description=Gunicorn instance to serve Flask App
After=network.target

[Service]
User=princess
Group=www-data
WorkingDirectory=/home/princess/flask_app
ExecStart=/home/princess/flask_app/venv/bin/gunicorn --workers 3 --bind 0.0.0.0:8000 app:app

[Install]
WantedBy=multi-user.target
//

-sudo systemctl daemon-reload
-sudo systemctl start flask_app
-sudo systemctl enable flask_app<!--refusing action stop disable and create a fresh file-->
<!--for no file-->
cd ~/flask_app
python3 -m venv venv
source venv/bin/activate
pip install gunicorn flask


#for Nginx as revrse proxy!!!
-sudo apt update
-sudo apt install nginx -y
-sudo systemctl start nginx
sudo systemctl enable nginx
## configuration file-
-sudo nano /etc/nginx/sites-available/flask_app
//
server {
    listen 80;
    server_name localhost;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
//

-sudo ln -s /etc/nginx/sites-available/flask_app /etc/nginx/sites-enabled
-sudo rm /etc/nginx/sites-enabled/default
-sudo nginx -t
-sudo systemctl restart nginx

#jenkins set up instructions !!!!!!!!
-sudo apt update && sudo apt upgrade -y
-sudo apt install openjdk-11-jdk -y
-java -version
-wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
-echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
-sudo apt update
-sudo apt install jenkins -y
-sudo systemctl start jenkins
-sudo systemctl enable jenkins
-sudo cat /var/lib/jenkins/secrets/initialAdminPassword
<!-- no installation candidate-->
sudo apt-cache policy Jenkins 

##none candidate installed
-wget https://pkg.jenkins.io/debian-stable/binary/jenkins_2.426.1_all.deb
-sudo dpkg -i jenkins_2.426.1_all.deb
-sudo apt --fix-broken install -y
-sudo dpkg -i jenkins_2.426.1_all.deb

##manage plugins<!--manually installing pipeline plugin -->
-wget https://updates.jenkins.io/latest/workflow-aggregator.hpi -P ~/Downloads
workflow-aggregator.hpi 
-sudo cp ~/Downloads/workflow-aggregator.hpi /var/lib/jenkins/plugins/
-sudo chown jenkins:jenkins /var/lib/jenkins/plugins/workflow-aggregator.hpi
-sudo systemctl restart jenkins
<!--additional depnedencies-->
wget https://updates.jenkins.io/latest/workflow-step-api.hpi -P ~/Downloads
wget https://updates.jenkins.io/latest/workflow-job.hpi -P ~/Downloads
wget https://updates.jenkins.io/latest/workflow-cps.hpi -P ~/Downloads
<!--reinstalling jenkins and select plugins while reinstalling helps to download pipeline plugin-->
##jenkin architecture
master- 
sudo apt update
sudo apt install openjdk-11-jdk -y
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt update
sudo apt install jenkins -y
sudo systemctl start jenkins
sudo systemctl enable jenkins
sudo systemctl status jenkins
sudo cat /var/lib/jenkins/secrets/initialAdminPassword









