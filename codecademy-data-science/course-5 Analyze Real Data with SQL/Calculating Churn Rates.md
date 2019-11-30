# Calculating Churn Rates

Take a look at the first 100 rows

``` sql
select *
from subscriptions 
limit 100;
```

Determine the range of months of data provided. Which months will you be able to calculate churn for?

``` sql
select max(subscription_start), min(subscription_start)
from subscriptions;  
```

