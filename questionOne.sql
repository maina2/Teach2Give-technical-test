-- Write a query that will display the results below (Note: some columns might be renamed 
-- but use the column names above). It should only show 2020 data and order by driver 
-- points.

SELECT c.circuit_location, 
    r.grid, 
    r.position, 
    r.fastest_lap, 
    r.points, 
    d.driver_name, 
    ra.race_name, 
    ra.race_time, 
    ra.race_year, 
    co.team, 
    ra.race_date 
FROM circuits c 
JOIN races ra ON c.circuitId = ra.circuitId
JOIN results r ON ra.raceId = r.raceId 
JOIN drivers d ON r.driverId = d.driverId
WHERE ra.race_year = 2020
ORDER BY r.points;