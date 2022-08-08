
```bash
# Install the requirements:
pip install -r requirements.txt

# Configure the location of your MongoDB database:
export MONGODB_URL="mongodb+srv://<username>:<password>@<url>/<db>?retryWrites=true&w=majority"

# Start the service:
# cd fastApi_\&_SQLlAlchemy_\&_postgresSQL/
# uvicorn main_schema:app --reload
```