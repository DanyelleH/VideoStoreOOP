CREATE DATABASE videostore;
\connect videostore

CREATE TABLE MembershipType(
    id serial PRIMARY KEY,
    type varchar(2),
    rental_limit int
);

INSERT INTO MembershipType (type, rental_limit) VALUES 
    ('px',3),('sx',1);


CREATE TABLE Customer (
    id serial PRIMARY KEY,
    account_type int REFERENCES membershipType(id),
    first_name  varchar(150),
    last_name varchar(150)
);

INSERT INTO Customer (account_type,first_name,last_name) VALUES
    (2,'Monica','Gellar'),
    (1,'Chandler','Bing'),
    (1,'Rachel','Green'),
    (2,'Ross','Gellar'),
    (2,'Phoebe','Buffay'),
    (1,'Joey','Tribbiani');

CREATE TABLE MoviesAvailable(
    id serial PRIMARY KEY,
    title varchar(255),
    qty int
);

INSERT INTO MoviesAvailable (title,qty) VALUES
    ('Toy Story',1),
    ('WALL-E',2),
    ('Up',5),
    ('Inside Out',1),
    ('The Prestige',2),
    ('The Dark Knight',3),
    ('Inception',4),
    ('Intersteller',2),
    ('Deadpool',3),
    ('The Godfather',0);

CREATE TABLE Current_rentals (
    id serial PRIMARY KEY,
    cust_id int REFERENCES Customer(id),
    movie_id int REFERENCES MoviesAvailable(id)
);

INSERT INTO Current_rentals (cust_id,movie_id) VALUES
    (1,10),
    (2,5), (2,6), (2,7),
    (3,4),(3,2),(3,5),
    (4,NULL),
    (5,2),
    (6,10),(6,9);