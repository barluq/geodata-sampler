# Dockerfile for a development container with GDAL and PostgreSQL client

# INFO: Part of the container tools is installed via the devcontainer.json file.
#       See Features section of the devcontainer.json for more details.

# Based on the official Dev Containers base image of the Ubuntu 24.04 LTS (Noble) version
FROM mcr.microsoft.com/devcontainers/base:noble

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        git \
        wget \
        gdal-bin \
        postgresql-client \
        libpq-dev \
        libgdal-dev \
        pkg-config \
        vim \
        less \
        tree \
        jq \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables for GDAL
ENV GDAL_CONFIG=/usr/bin/gdal-config
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

# Set python environment variables
# ENV PYTHONUNBUFFERED=1
# ENV PYTHONPATH=./src

# Install common development tools
RUN curl -fsSL https://get.docker.com | sh