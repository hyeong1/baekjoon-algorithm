select id, email, first_name, last_name
from developers
where skill_code & (select code from skillcodes where name like "Py%")
   or skill_code & (select code from skillcodes where name like "C#")
order by id