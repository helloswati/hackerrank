Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.
The STATION table is described as follows.


Solution:
SELECT COUNT(CITY) — COUNT(DISTINCT CITY) FROM STATION ;
