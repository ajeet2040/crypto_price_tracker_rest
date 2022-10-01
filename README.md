# crypto_price_tracker_rest
This app keeps track of price of crypto coin `Bitcoin` at a scheduled interval and also stores the price.
It triggers an email if price drops/rise above a configurable range. It exposes an API to view the stored prices
along with its timestamp.

## Prerequisites
    - Docker (Installed)
    - There should not be any app running on port 8000.
      (This can be changed in docker compose yaml file.) (Ideally should be a part of .env)

## How to Run (Locally)
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
   For more detailed documentation, view TODO

## Assumptions:
1. Max pagination limit is 1000 records for API and Default limit is 10 records.
2. For API `api/prices/`, all params are optional and records are sorted by latest first.
3. For API `api/prices/`, timestamp will be unique column.

## Important!
Due to Mailtrap requiring business account for smtp Inbox activation, unable to complete full settings of same.
Was not able to see the received emails.
However, Mailtrap does returns 200 response.

## Future Considerations
   - Use a production database like `Postgres` instead of sqllite.
   - Docker configuration for production builds with a production server like `gunicorn`.
   - Support for other coins and currencies.
   - Authentication and Rate Limit to API.
