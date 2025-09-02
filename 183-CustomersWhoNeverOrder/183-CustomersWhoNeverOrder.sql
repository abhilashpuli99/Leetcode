-- Last updated: 9/2/2025, 1:42:44 PM
# Write your MySQL query statement below
select name as Customers  from Customers where id not in(select customerId from Orders);
