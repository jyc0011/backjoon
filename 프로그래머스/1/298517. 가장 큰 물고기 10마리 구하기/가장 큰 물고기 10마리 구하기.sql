SELECT ID, LENGTH
FROM FISH_INFO
WHERE LENGTH IS NOT NULL
-- NULL값이 아닌 것만
ORDER BY LENGTH DESC, ID ASC
-- LENGTH에 대해 내림차순으로 먼저 정렬
-- 동일 값 있으면 ID는 오름차순
LIMIT 10;
-- 상위 10개만 출력