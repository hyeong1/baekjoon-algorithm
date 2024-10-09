-- 코드를 작성해주세요
SELECT COUNT(*) AS FISH_COUNT, CAST(DATE_FORMAT(TIME, '%c') AS UNSIGNED) AS MONTH
FROM FISH_INFO
GROUP BY CAST(DATE_FORMAT(TIME, '%c') AS UNSIGNED)
HAVING COUNT(*) > 0
ORDER BY CAST(MONTH AS UNSIGNED)
