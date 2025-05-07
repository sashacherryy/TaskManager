Start Backend:

.env -> {
   DB_USER
   DB_PASSWORD
   DB_HOST
   DB_NAME
   DB_PORT
}

1) ../../../Backend> pip install -r requirements.txt

2) ../../../Backend> uvicorn app.main:app --reload

SwaggerUI: http://localhost:8000/docs
