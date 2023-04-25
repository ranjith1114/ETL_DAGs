INSERT INTO user_details (firstname, lastname, country, username, password, email) 
VALUES 
    ('John', 'Doe', 'USA', 'johndoe', 'password123', 'johndoe@example.com'),
    ('Jane', 'Doe', 'USA', 'janedoe', 'password456', 'janedoe@example.com'),
    ('Alice', 'Smith', 'Canada', 'alicesmith', 'password789', 'alicesmith@example.com'),
    ('Bob', 'Johnson', 'UK', 'bobjohnson', 'password123', 'bobjohnson@example.com'),
    ('Emma', 'Wilson', 'Australia', 'emmawilson', 'password456', 'emmawilson@example.com'),
    ('David', 'Lee', 'USA', 'davidlee', 'password789', 'davidlee@example.com'),
    ('Julia', 'Chen', 'China', 'juliachen', 'password123', 'juliachen@example.com'),
    ('Daniel', 'Kim', 'Korea', 'danielkim', 'password456', 'danielkim@example.com'),
    ('Maria', 'Garcia', 'Spain', 'mariagarcia', 'password789', 'mariagarcia@example.com'),
    ('Mohammed', 'Ali', 'Egypt', 'mohammedali', 'password123', 'mohammedali@example.com');


country VARCHAR NOT NULL,
username VARCHAR UNIQUE NOT NULL,
 password VARCHAR NOT NULL,
    email VARCHAR UNIQUE NOT NULL