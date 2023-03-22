# Set base image as jenkins official docker image
FROM jenkins/jenkins

# Define the proxies
ENV HTTP_PROXY "<proxy>"
ENV HTTPS_PROXY "<proxy>"

# Allow local checkout in jenkins
ENV JAVA_OPTS "-Dhudson.plugins.git.GitSCM.ALLOW_LOCAL_CHECKOUT=true"

# Set USER
USER root

RUN printf 'Acquire::http::Proxy "<proxy>";\n Acquire::https::Proxy "<proxy>";\n' >> /etc/apt/apt.conf

# Create USER
RUN useradd -ms /bin/bash <user>
RUN echo '<user>:<pass>' | chpasswd

# Update Ubuntu Software repository
RUN apt-get clean
RUN apt-get update -y

# Install python
RUN apt-get install -y python3
RUN apt-get install -y python3-venv

# Install Git
RUN apt-get install git

# Install other necessary packages
RUN apt-get install net-tools 
RUN apt-get install -y openssh-server 
RUN apt-get install -y vim 
RUN apt-get install -y curl
RUN apt install sudo 

# Set the workspace directory
WORKDIR /home

# Copy the contents
COPY ./requirements.txt .
COPY startup.sh .

# Setup the environment
RUN chmod +x startup.sh
RUN ./startup.sh
