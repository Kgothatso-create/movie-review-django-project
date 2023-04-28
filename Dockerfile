# Base image
FROM pypy:latest

# Set the working directory
WORKDIR /movie_zone

# Copy the requirements file
COPY requirements.txt requirements.txt
COPY manage.py manage.py

# Install the requirements
RUN pip install -r requirements.txt

# Run migrations
RUN python manage.py makemigrations
RUN python manage.py migrate


# Copy the application code
COPY . .

# Expose the application port
EXPOSE 8000

# Start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
