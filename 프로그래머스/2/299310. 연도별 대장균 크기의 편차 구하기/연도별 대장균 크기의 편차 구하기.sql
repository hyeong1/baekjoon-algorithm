select YEAR(DIFFERENTIATION_DATE) as YEAR, 
       (select max(SIZE_OF_COLONY)
        from ecoli_data
        where year(DIFFERENTIATION_DATE) = year) - size_of_colony as YEAR_DEV,
       id
from ecoli_data
order by 1, 2