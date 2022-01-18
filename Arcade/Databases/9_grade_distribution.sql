CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT Name, ID FROM Grades
    WHERE Final > (0.25 * (Midterm1 + Midterm2) + (0.5 * Final)) AND (Final > (0.5 * (Midterm1 + Midterm2)))
    ORDER BY SUBSTRING(name, 1, 3), id;
    
END