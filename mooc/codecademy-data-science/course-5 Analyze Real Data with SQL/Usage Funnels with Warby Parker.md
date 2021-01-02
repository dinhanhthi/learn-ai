# Usage Funnels with Warby Parker

[Warby Parker](https://www.warbyparker.com/) is a transformative lifestyle brand with a lofty objective: to offer designer eyewear at a revolutionary price while leading the way for socially conscious businesses. Founded in 2010 and named after two characters in an early Jack Kerouac journal, Warby Parker believes in creative thinking, smart design, and doing good in the world. For every pair of eyeglasses and sunglasses sold, a pair is distributed to someone in need.

In this project, you will analyze different Warby Parker’s marketing funnels in order to calculate conversion rates. Here are the funnels and the tables that you are given:

Quiz Funnel: `survey`

Home Try-On Funnel: `quiz`, `home_try_on`, `purchase`

This project was a collaboration with Warby Parker’s Data Science team (thank you!) and uses fictional data. Let’s get started!

## 1

To help users find their perfect frame, Warby Parker has a Style Quiz that has the following questions:

1. “What are you looking for?”
1. “What’s your fit?”
1. “Which shapes do you like?”
1. “Which colors do you like?”
1. “When was your last eye exam?”

The users’ responses are stored in a table called survey. 

*Select all columns from the first 10 rows. What columns does the table have?*

``` sql
SELECT *
FROM survey
LIMIT 10;
```

## 2

Users will “give up” at different points in the survey. Let’s analyze how many users move from Question 1 to Question 2, etc.

*What is the number of responses for each question?*

``` sql
SELECT question,
   COUNT(DISTINCT user_id)
FROM survey
GROUP BY 1;
```

## 4

Warby Parker’s purchase funnel is:

Take the Style Quiz → Home Try-On → Purchase the Perfect Pair of Glasses

During the Home Try-On stage, we will be conducting an A/B Test:

- 50% of the users will get 3 pairs to try on
- 50% of the users will get 5 pairs to try on

Let’s find out whether or not users who get more pairs to try on at home will be more likely to make a purchase.

The data will be distributed across three tables: `quiz`, `home_try_on`, `purchase`

Examine the first five rows of each table

*What are the column names?*

``` sql
SELECT *
FROM quiz
LIMIT 5;

SELECT *
FROM home_try_on
LIMIT 5;

SELECT *
FROM purchase
LIMIT 5;
```

## 5

Each row will represent a single user from the browse table:

- If the user has any entries in home_try_on, then is_home_try_on will be ‘True’.
- number_of_pairs comes from home_try_on table
- If the user has any entries in is_purchase, then is_purchase will be ‘True’.

Use a LEFT JOIN to combine the three tables, starting with the top of the funnel (quiz) and ending with the bottom of the funnel (purchase).

Select only the first 10 rows from this table (otherwise, the query will run really slowly).

``` sql
SELECT DISTINCT q.user_id,
   h.user_id IS NOT NULL AS 'is_home_try_on',
   h.number_of_pairs,
   p.user_id IS NOT NULL AS 'is_purchase'
FROM quiz q
LEFT JOIN home_try_on h
   ON q.user_id = h.user_id
LEFT JOIN purchase p
   ON p.user_id = q.user_id
LIMIT 10;
```