-- Last updated: 9/2/2025, 1:41:20 PM
# Write your MySQL query statement below
select player_id,MIN(event_date) as first_login from Activity group by player_id;
