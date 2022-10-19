FROM python:3.8-slim
WORKDIR /app
ENV GOOGLE_APPLICATION_CREDENTIALS="/app/firestore_servicekey.json"
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt  
CMD ["flask","--app","firestore_visitor_counter_api.py","run","--host=0.0.0.0"]
