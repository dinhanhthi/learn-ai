# Marketing Attribution

The ways (sources) customers come to our website is called **channels** / **touchpoints** / **sources**.

If an ad campaign drives a lot of visits to their site, then they know that source is working! We say that **those visits are attributed** to the ad campaign.

But how do websites capture that information? The answer is **UTM parameters**. 

You can see a common schema for a "page visits" table at [this link](./pdf/page_visits_schema.pdf).

## First / Last Touch

June's first touch — the **first time** she was exposed to CoolTShirts.com

June’s **last touch** — the exposure to CoolTShirts.com that led to a purchase (from `facebook`, for example)

If you want to increase sales at CoolTShirts.com, *would you count on buzzfeed or increase facebook ads?* The real question is: should June’s purchase be attributed to buzzfeed or to facebook?

- First-touch attribution only considers the first utm_source for each customer, which would be buzzfeed in this case. *This is a good way of knowing how visitors initially discover a website.*
- Last-touch attribution only considers the last utm_source for each customer, which would be facebook in this case. *This is a good way of knowing how visitors are drawn back to a website, especially for making a final purchase.*

The results can be crucial to improving a company’s marketing and online presence. Most companies analyze both first- and last-touch attribution and display the results separately.

## Review

You can now wield SQL to find where, when, and how users are visiting a website. Well done! Here’s a summary of what you learned:

- **UTM parameters** are a way of tracking visits to a website. Developers, marketers, and analysts use them to capture information like the time, attribution source, and attribution medium for each user visit.
- **First-touch attribution** only considers the first source for each customer. This is a good way of knowing how visitors initially discover a website.
- **Last-touch attribution** only considers the last source for each customer. This is a good way of knowing how visitors are drawn back to a website, especially for making a final purchase.
- Find first and last touches by grouping `page_visits` by `user_id` and finding the `MIN` and `MAX` of `timestamp`.
- To find firstand last-touch attribution, join that table back with the original `page_visits` table on `user_id` and `timestamp`.