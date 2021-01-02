# User Churn

## What is Churn

A common revenue model for SaaS (Software as a service) companies is to charge a monthly subscription fee for access to their product. Frequently, these companies *aim to continually increase the number of users paying for their product*. One metric that is helpful for this goal is churn rate.

**Churn rate** is the percent of subscribers that have canceled within a certain period, usually a month. For a user base to grow, the *churn rate must be less than the new subscriber rate for the same period*.

For example, suppose you were analyzing data for a monthly video streaming service called CodeFlix. At the beginning of February, CodeFlix has 1,000 customers. In February, 250 of these customers cancel. The churn rate for February would be:

250 / 1000 = 25% churn rate

``` sql
select 250. / 1000;
```

## Single Month I

- For the numerator, we only want the portion of the customers who canceled during December. 
- For the denominator, we only want to be considering customers who were active at the beginning of December:

``` sql
SELECT 1.0 * 
(
  SELECT COUNT(*)
  FROM subscriptions
  WHERE subscription_start < '2016-12-01'
  AND (
    subscription_end
    BETWEEN '2016-12-01'
    AND '2016-12-31'
  )
) / (
  SELECT COUNT(*) 
  FROM subscriptions 
  WHERE subscription_start < '2016-12-01'
  AND (
    (subscription_end >= '2016-12-01')
    OR (subscription_end IS NULL)
  )
) 
AS result;
```

## Single Month II

The previous method worked, but you may have noticed we selected the same group of customers twice for the same month and repeated a number of conditional statements.

Companies typically look at churn data over a period of many months. We need to modify the calculation a bit to make it easier to mold into a multi-month result. This is done by making use of `WITH` and `CASE`.

``` sql
WITH enrollments AS 
(SELECT *
FROM subscriptions
WHERE subscription_start < '2017-01-01'
AND (
  (subscription_end >= '2017-01-01')
  OR (subscription_end IS NULL)
)),
status AS 
(SELECT 
CASE
  WHEN (subscription_end > '2017-01-31')
    OR (subscription_end IS NULL) THEN 0
  ELSE 1
  END as is_canceled,
CASE
  WHEN (subscription_start < '2017-01-01')
    AND (
      (subscription_end >= '2017-01-01')
        OR (subscription_end IS NULL)
    ) THEN 1
    ELSE 0
  END as is_active
FROM enrollments
)
SELECT 1.0 * SUM(is_canceled)/SUM(is_active) FROM status;
```

## Multiple Month: Create Months Temporary Table

We need a table for January, February, and March of 2017.

``` sql
WITH months AS (
  SELECT 
    '2017-01-01' AS first_day, 
    '2017-01-31' AS last_day 
  UNION 
  SELECT 
    '2017-02-01' AS first_day, 
    '2017-02-28' AS last_day 
  UNION 
  SELECT 
    '2017-03-01' AS first_day, 
    '2017-03-31' AS last_day
), 
cross_join AS (
  SELECT *
  FROM subscriptions
  CROSS JOIN months
), 
status AS (
  SELECT 
    id, 
    first_day AS month, 
    CASE
      WHEN (subscription_start < first_day) 
        AND (
          subscription_end > first_day 
          OR subscription_end IS NULL
        ) THEN 1
      ELSE 0
    END AS is_active, 
    CASE
      WHEN subscription_end BETWEEN first_day AND last_day THEN 1
      ELSE 0
    END AS is_canceled 
  FROM cross_join
), 
status_aggregate AS (
  SELECT 
    month, 
    SUM(is_active) AS active, 
    SUM(is_canceled) AS canceled 
  FROM status 
  GROUP BY month
) 
SELECT
  month, 
  1.0 * canceled / active AS churn_rate 
FROM status_aggregate;
```

## Conclusion

In this lesson you learned:

- The churn rate is a percent of subscribers at the beginning of a period that cancel within that period. “Monthly churn” is a typical metric and what was used in the examples.
- How to calculate this metric using SQL for a single month. This used COUNT() and conditions to determine the number of subscribers that were active and how many canceled.
- A more complex method to track the subscriber churn rate over many months.