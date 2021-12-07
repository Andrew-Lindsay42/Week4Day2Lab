DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS staff;

CREATE TABLE staff (
  name VARCHAR(255),
  start_date VARCHAR(255),
  department VARCHAR(255),
  performance INT,
  id SERIAL PRIMARY KEY
);

CREATE TABLE animals (
  name VARCHAR(255),
  type VARCHAR(255),
  keeper INT REFERENCES staff(id),
  id SERIAL PRIMARY KEY
)