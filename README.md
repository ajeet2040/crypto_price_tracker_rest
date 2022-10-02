# crypto_price_tracker_rest
This app keeps track of price of crypto coin `Bitcoin` at a scheduled interval and also stores the price.
It triggers an email if price drops/rise above a configurable range. It exposes an API to view the stored prices
along with its timestamp.

## Prerequisites
    - Docker (Installed)
    - There should not be any app running on port 8000.
      (This can be changed in port binding of docker compose yaml file.)


## HOW TO RUN (LOCALLY)
1. After cloning/downloading the project, create a `.env` file in root directory by copying contents from `.env.dist` file.
2. Replace the below variables in the `.env` file.
    ```
    min=<min>
    max=<max>
    email=<email>
    username = <username>
    password = <password>
    ```
    > NOTE: For Prod, please set variables 'DEBUG' and 'SECRET_KEY' as well.

3. Run the below command ro 
    ```
    docker-compose up
    ```

## Sample API Request (For Local run on port 8000)
   ```
   http://localhost:8000/api/prices/?offset=0&limit=10&date=01-10-2022
   ```
   For more detailed documentation, view https://documenter.getpostman.com/view/22925969/2s83tFJBsN

## Assumptions:
1. Max pagination limit is 1000 records for API and Default limit is 10 records.
2. For API `api/prices/`, all params are optional and records are sorted by latest timestamp first.
3. For API `api/prices/`, timestamp will be unique column.

## Important!
Due to Mailtrap requiring business account for smtp Inbox activation, unable to view messages in inbox.
Was not able to see the received emails.
However, Mailtrap provided smtp creds and does returns 200 response.

## Testing.
A sample test case was added for checking response of prices api. 
> NOTE: Only one was added for demonstration due to time limit.

- Setup virtual env and install dependencies (One time)
    ```
    python -m venv venv
    source venv/bin/activate # For Windows, use .\env\Scripts\activate
    pip install -r requirements.txt
    pip install pytest-django 
    ```
- Run tests
    ```
    pytest
    ```

## Future Considerations
   - Add more Unit Test Cases.
   - Use a production database like `Postgres` instead of sqllite.
   - Docker configuration for production builds with a production server like `gunicorn`.
   - Support for other coins and currencies. (At present,module(fetch and save periodic) is designed in a way to support this.
