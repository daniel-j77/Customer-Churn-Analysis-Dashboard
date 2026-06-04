-- Total Customers

SELECT COUNT(*)
FROM customers;

-- Churn Customers

SELECT COUNT(*)
FROM customers
WHERE Churn='Yes';

-- Churn Rate

SELECT
COUNT(
CASE
WHEN Churn='Yes'
THEN 1
END
)*100.0
/
COUNT(*) AS churn_rate
FROM customers;

-- Average Monthly Charge

SELECT AVG(
MonthlyCharge
)
FROM customers;

-- Churn By Plan

SELECT
Plan,
COUNT(*)
FROM customers
WHERE Churn='Yes'
GROUP BY Plan;