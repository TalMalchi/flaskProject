FROM python


WORKDIR /app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=127.0.0.1

COPY requirements.txt .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

CMD ["python", "app.py"]

#The Dockerfile is pretty straightforward. It starts with the base image python:3 , which is a pre-built image that contains Python 3. It then exports port 5000 , which is the port that the Flask app will run on. It then sets the working directory to /app , which is where the app will be located in the container. It then copies the requirements.txt file into the container and installs the dependencies. Finally, it copies the rest of the app into the container and runs the app.
