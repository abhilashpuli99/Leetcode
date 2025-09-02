-- Last updated: 9/2/2025, 1:42:47 PM
# Write your MySQL query statement below
SELECT
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM Person p
LEFT JOIN Address a ON p.personId = a.personId;