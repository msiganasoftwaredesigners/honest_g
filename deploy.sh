#!/bin/bash

echo "Pulling the latest changes..."
git pull origin master

echo "Stopping existing containers..."
docker stop samiahomes_django_web || true
docker rm samiahomes_django_web || true

echo "Building Docker containers..."
docker-compose -f docker-compose.yml up --build -d

echo "Restarting the Django application..."
docker-compose restart django-web

echo "Deployment completed successfully!"
