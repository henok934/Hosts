#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Print each command before executing it
set -x

# Step 1: Activate the virtual environment (if applicable)
# Uncomment the next line if using a virtual environment
# source venv/bin/activate

# Step 2: Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Step 3: Run database migrations
echo "Applying database migrations..."
python manage.py migrate

# Step 4: Run tests (optional)
echo "Running tests..."
# Uncomment the next line to run tests
# python manage.py test

# Step 5: Collect static files (if applicable)
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Step 6: Start the server (optional)
# Uncomment the next line to start the server
# python manage.py runserver

# Step 7: Clean up temporary files (if necessary)
echo "Cleaning up..."
# Add any cleanup commands here

echo "Build process completed."
