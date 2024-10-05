FROM python:3.13-rc-alpine

# Create a new user "userapi"
RUN adduser -D userapi
WORKDIR /FlaskITVDN

# Install dependencies from requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY ./ ./

# Change ownership of the files to the "userapi" user
RUN chown -R userapi:userapi ./

# Switch to the "userapi" user
USER userapi

# Expose port 8000
EXPOSE 5000

# Command to run the application
CMD ["python", "./wsgi.py"]

#CMD gunicorn --bind 0.0.0.0:$PORT wsgi:app