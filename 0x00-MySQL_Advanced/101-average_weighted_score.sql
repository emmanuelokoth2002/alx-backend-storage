DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE user_id INT;
    DECLARE total_score FLOAT DEFAULT 0;
    DECLARE total_weight INT DEFAULT 0;

    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN cur;
    read_loop: LOOP
        FETCH cur INTO user_id;
        IF done = 1 THEN
            LEAVE read_loop;
        END IF;

        SELECT SUM(p.weight * c.score), SUM(p.weight)
        INTO total_score, total_weight
        FROM projects p
        JOIN corrections c ON p.id = c.project_id
        WHERE c.user_id = user_id;

        IF total_weight > 0 THEN
            UPDATE users
            SET average_score = total_score / total_weight
            WHERE id = user_id;
        ELSE
            UPDATE users
            SET average_score = 0
            WHERE id = user_id;
        END IF;
    END LOOP;

    CLOSE cur;
END //

DELIMITER ;
