FROM python:3.10-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    zip \
    unzip \
    openjdk-17-jdk \
    python3-pip \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install buildozer and dependencies
RUN pip install --upgrade pip
RUN pip install buildozer==1.4.3 Cython==0.29.33 kivy==2.1.0

# Optional: install android SDK/NDK via buildozer when run
WORKDIR /project
CMD ["bash"]