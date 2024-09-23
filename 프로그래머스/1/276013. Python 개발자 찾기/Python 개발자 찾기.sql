select id, email, first_name, last_name
from developer_infos
where skill_1 like "py%"
   or skill_2 like "py%"
   or skill_3 like "py%"
order by id