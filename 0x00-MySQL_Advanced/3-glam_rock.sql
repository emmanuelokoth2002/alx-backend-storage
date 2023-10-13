-- List bands with Glam rock as their main style, ranked by longevity
SELECT band_name, 
       IFNULL(YEAR(2022) - YEAR(formed), 0) AS lifespan
FROM metal_bands
WHERE split = 'Glam rock'
ORDER BY lifespan DESC, band_name;
