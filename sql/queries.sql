SELECT * FROM public.loggings
ORDER BY timestamp::TIMESTAMP DESC
;

SELECT
    worker_id,
    COUNT(*) AS recs
FROM public.loggings
GROUP BY 1
ORDER BY 2 DESC
;