-- Last updated: 9/2/2025, 1:42:45 PM
# Write your MySQL query statement below
select email from Person group by email having count(email)>1;