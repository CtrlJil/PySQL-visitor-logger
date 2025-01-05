--Optimizing and Securing the System to Prevent SQL Injection

query = "INSERT INTO visitors (ip_address, user_agent) VALUES (%s, %s)"
cursor.execute(query, (ip_address, user_agent))
db.commit()
--Set Up Database Indexes for Faster Queries

CREATE INDEX idx_ip ON visitors (ip_address);
CREATE INDEX idx_time ON visitors (visit_time);

--Automatically Delete Old Visitor Data
CREATE EVENT delete_old_records
ON SCHEDULE EVERY 1 DAY
DO
DELETE FROM visitors WHERE visit_time < NOW() - INTERVAL 90 DAY;
