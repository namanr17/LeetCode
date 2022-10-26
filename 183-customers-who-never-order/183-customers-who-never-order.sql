# Write your MySQL query statement below
select C.name as Customers
from Customers C
where C.id not in (select c.id from Customers c join Orders o where c.id = o.customerId)