FROM python:3.8
RUN apt-get update && apt-get install -y portaudio19-dev
RUN apt-get update && apt-get install -y alsa-utils

# Update the package manager and install necessary dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        alsa-utils \
        libasound2-dev \
        portaudio19-dev \
    && rm -rf /var/lib/apt/lists/*



# RUN apt update && apt install -y espeak ffmpeg libespeak1
# RUN apt-get update && apt-get install -y alsa-firmware-loaders
# RUN apt-get update && apt-get install -y alsa-lib

RUN alsa force-reload

# Clean up the package manager cache
RUN rm -rf /var/lib/apt/lists/*


# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "main.py"]
