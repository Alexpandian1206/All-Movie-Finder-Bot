FROM python:3.8-slim-buster

# Update system and install git
RUN apt update && apt upgrade -y
RUN apt install git -y

# Install Python dependencies
COPY requirements.txt /requirements.txt
RUN pip3 install -U pip && pip3 install -U -r /requirements.txt

# Create the directory for the bot and set the working directory
RUN mkdir /Droplink-Movie-Finder-Bot
WORKDIR /Droplink-Movie-Finder-Bot

# Copy the start.sh script and make it executable
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Expose port 8080 for external access
EXPOSE 8080

# Run the bot
CMD ["/bin/bash", "/start.sh"]
