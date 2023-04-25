Drop table user_details;

CREATE TABLE IF NOT EXISTS user_details (
    firstname VARCHAR NOT NULL,
    lastname VARCHAR NOT NULL,
    country VARCHAR NOT NULL,
    username VARCHAR UNIQUE NOT NULL,
    password VARCHAR NOT NULL,
    email VARCHAR UNIQUE NOT NULL);