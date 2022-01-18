CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT name from leaderboard
    ORDER BY score DESC LIMIT 5 OFFSET 3;
END