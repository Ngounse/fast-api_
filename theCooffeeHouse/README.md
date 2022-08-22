### Install the requirements:

```bash
# pip install -r requirements.txt

# Configure the location of your MongoDB database:
export MONGODB_URL="mongodb+srv://<username>:<password>@<url>/<db>?retryWrites=true&w=majority"

# Start the service:
# cd theCooffeeHouse
# uvicorn main_schema:app --reload
```

### Alternative API docs
```base
# http://127.0.0.1:8000/redoc
```