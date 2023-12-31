DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS DECIMAL(10, 6)
BEGIN
    DECLARE result DECIMAL(10, 6);
    
    IF b = 0 THEN
        SET result = 0;
    ELSE
        SET result = a / b;
    END IF;
    
    RETURN result;
END //

DELIMITER ;
