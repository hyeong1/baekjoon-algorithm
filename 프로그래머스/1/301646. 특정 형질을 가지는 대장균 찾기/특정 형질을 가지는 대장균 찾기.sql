select count(*) as COUNT
from ecoli_data
where (2 & GENOTYPE = 0) and ((1 & genotype = 1) or (4 & genotype = 4))