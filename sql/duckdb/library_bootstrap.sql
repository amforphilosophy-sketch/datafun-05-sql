-- library_bootstrap.sql
-- Create tables and load CSV data for the library domain.

CREATE TABLE branch (
    branch_id    TEXT PRIMARY KEY,
    branch_name  TEXT,
    city         TEXT,
    system_name  TEXT
);

CREATE TABLE checkout (
    checkout_id    TEXT PRIMARY KEY,
    branch_id      TEXT REFERENCES branch(branch_id),
    material_type  TEXT,
    duration_days  INTEGER,
    fine_amount    DOUBLE,
    checkout_date  DATE
);

COPY branch FROM 'data/raw/library/branch.csv' (HEADER, AUTO_DETECT TRUE);
COPY checkout FROM 'data/raw/library/checkout.csv' (HEADER, AUTO_DETECT TRUE);
