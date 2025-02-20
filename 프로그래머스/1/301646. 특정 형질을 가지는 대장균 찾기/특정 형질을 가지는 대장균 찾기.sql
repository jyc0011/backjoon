SELECT COUNT(*) AS COUNT
-- 조건을 만족하는 행의 개수를 구한다
FROM ECOLI_DATA
-- ECOLI_DATA 테이블로부터 한다
WHERE (GENOTYPE & 2) = 0
-- 2번 형질이 없는 개체만 선택
-- 2는 10₍₂₎이므로, AND 연산 후 0이면 2번 형질이 없는 것
AND (GENOTYPE & 1 <> 0 OR GENOTYPE & 4 <> 0);
-- 1번(1₍₂₎) 또는 3번(100₍₂₎) 형질을 보유한 개체 선택
-- GENOTYPE & 1 <> 0 → 1번 형질이 포함됨
-- GENOTYPE & 4 <> 0 → 3번 형질이 포함됨