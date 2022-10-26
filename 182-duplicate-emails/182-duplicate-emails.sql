# Write your MySQL query statement below
select distinct P.email as Email
from (select p.id, p.email, count(p.id) as count_p from Person as p group by p.email) as P
where P.count_p > 1