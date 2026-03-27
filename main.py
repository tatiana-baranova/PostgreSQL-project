# -- INSERT INTO users(email, login, name, date_of_birth, age) VALUES('lisa1@gmail.com', 'User', 'Lisa', '1985-01-01', '35');
# -- SELECT * FROM users;
# -- SELECT MAX(age) FROM users
# -- SELECT MIN(age) FROM users
# -- SELECT SUM(age) FROM users
# -- SELECT COUNT(age) FROM users
# -- SELECT ROUND(AVG(age)) FROM users

# -- SELECT email, SUM(age) AS age, AVG(id) FROM users GROUP BY email;
# -- ALTER TABLE IF EXISTS public.users
# --     ADD COLUMN age smallint NOT NULL DEFAULT 10;
# -- SELECT NOW()::time;
# -- SELECT * FROM users WHERE date_of_birth < NOW();