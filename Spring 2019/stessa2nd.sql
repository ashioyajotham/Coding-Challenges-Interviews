Problem statement:

- Consider the following database tables: users, properties, transactions
- And their associated schema:

a. users (id, name, email, phone_number, created_at, updated_at)
b. properties (id, user_id, street_address, unit_number, city, state, zip_code, created_at, updated_at)
c. transactions (id, user_id, property_id, account_id, transaction_category_id, amount, name, created_at, updated_at)
d. transaction_categories (id, name, created_at, updated_at)

Questions / Using SQL:

1. How many users do we have in our system?
SELECT COUNT(id) from users;



2. How many properties does each user own? Print out email and count. 
SELECT email, count(*) 
FROM users 
INNER JOIN properties ON users.id = properties.user_id 
GROUP BY email;



3. List users (id, email) who have orphan transactions. An orphan transaction is a transaction that doesn't belong to a property. 

SELECT DISTINCT id, email from users WHERE id IN
  (SELECT user_id FROM transactions WHERE property_id IS NULL);




4. Which properties have at least/more than 10 transactions? 

SELECT properties.*, count(*) 
FROM properties INNER JOIN transactions ON properties.id = transations.property_id 
GROUP BY properties.id 
HAVING count > 10




5. For each user and property, list down how many categorized/uncategorized transactions they have.

SELECT users.id, properties.id, ISNULL(transactions.transaction_category_id) as uncategorized, count(*)
FROM users 
OUTER JOIN properties ON users.id = properties.user_id 
OUTER JOIN transactions ON users.id = transactions.user_id
GROUP BY users.id, properties.id, ISNULL(transactions.transaction_category_id)


# 
# https://www.w3schools.com/sql/func_mysql_isnull.asp
# 



Syntax:

SELECT
FROM <tables>
[LEFT/INNER/RIGHT] JOIN <table columns> ON col1 = col2
WHERE
AND
OR
ORDER BY
GROUP BY
HAVING