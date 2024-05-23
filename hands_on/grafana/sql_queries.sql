--- Number of Visits on Each Minute
SELECT toStartOfMinute(timestamp) as time, count(*) as visit FROM "default"."clickstream" GROUP BY time ORDER BY time ASC;

--- Most Visited Pages:
SELECT
    page_title,
    COUNT(*) AS visits
FROM clickstream
GROUP BY page_title
ORDER BY visits DESC
LIMIT 10;

-- Most Visited Products
SELECT
    page_title,
    COUNT(*) AS visits
FROM clickstream
WHERE page_url LIKE '/product_details/%'
GROUP BY page_title
ORDER BY visits DESC
LIMIT 10;

-- Most Visited Categories
SELECT
    page_title,
    COUNT(*) AS visits
FROM clickstream
WHERE page_url LIKE '/categories/%'
GROUP BY page_title
ORDER BY visits DESC
LIMIT 10;