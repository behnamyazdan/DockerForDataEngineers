USE default;

CREATE TABLE IF NOT EXISTS clickstream
(
    user_id UInt32,
    page_title LowCardinality(String),
    page_url LowCardinality(String),
    timestamp Datetime64(3),
    event_type LowCardinality(String),
    ttl DateTime DEFAULT now()
)
ENGINE MergeTree
PARTITION BY toYYYYMMDD(timestamp)
ORDER BY (timestamp, user_id)
TTL ttl + INTERVAL 7 DAY;


CREATE TABLE IF NOT EXISTS kafka_clickstream
(
    `message` String
)
ENGINE Kafka
SETTINGS
    kafka_broker_list = 'kafka:9092',
    kafka_topic_list = 'cdc_.public.clickstream',
    kafka_group_name = 'clickhouse_clickstream_consumer',
    kafka_format = 'JSONAsString',
    kafka_num_consumers = 1,
    kafka_max_block_size = 1048576;



CREATE MATERIALIZED VIEW IF NOT EXISTS mv_clickstream to clickstream
(
    user_id String,
    page_title String,
    page_url String,
    timestamp String,
    event_type String
) AS SELECT
    JSONExtractString(message, 'after.user_id') AS user_id,
    JSONExtractString(message, 'after.page_title') AS page_title,
    JSONExtractString(message, 'after.page_url') AS page_url,
    JSONExtractString(message, 'after.timestamp') AS timestamp,
    JSONExtractString(message, 'after.event_type') AS event_type
FROM kafka_clickstream
SETTINGS stream_like_engine_allow_direct_select = 1;