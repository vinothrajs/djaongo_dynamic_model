CREATE DATABASE erp_poc

CREATE TABLE ledger (
    id SERIAL PRIMARY KEY,
    from_date DATE NOT NULL,
    to_date DATE NOT NULL,
    ledger_id VARCHAR(30) NOT NULL,
    cost INTEGER NOT NULL
);

INSERT INTO ledger (from_date, to_date, ledger_id, cost) VALUES 
('2024-01-01', '2024-01-31', 'ABC123', 100),
('2024-02-01', '2024-02-29', 'DEF456', 200),
('2024-03-01', '2024-03-31', 'GHI789', 300),
('2024-04-01', '2024-04-30', 'JKL012', 400);


INSERT INTO "mtable" (name) VALUES ('ledger');

INSERT INTO "mfield" (table_id, name, type) VALUES (1, 'from_date', 'DateField');
INSERT INTO "mfield" (table_id, name, type) VALUES (1, 'to_date', 'DateField');
INSERT INTO "mfield" (table_id, name, type) VALUES (1, 'ledger_id', 'CharField');
INSERT INTO "mfield" (table_id, name, type) VALUES (1, 'cost', 'IntegerField');