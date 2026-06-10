"""app_library_duckdb_mohmand.py - Custom Project: Library domain (Ahmad Saleem Mohmand).

Author: Ahmad Saleem Mohmand
Date: 2026-06

Purpose:
- Read library csv files into a DuckDB database.
- Use Python to automate SQL scripts (stored in files).
- Log the pipeline process.

Paths (relative to repo root):
   SQL:  sql/duckdb/*.sql
   CSV:  data/raw/library/branch.csv
   CSV:  data/raw/library/checkout.csv
   DB:   artifacts/duckdb/library.duckdb
"""

# === DECLARE IMPORTS ===

import logging
from pathlib import Path
from typing import Final

# External (must be listed in pyproject.toml)
from datafun_toolkit.logger import get_logger, log_header
import duckdb

# === CONFIGURE LOGGER ONCE PER MODULE (FILE) ===

LOG: logging.Logger = get_logger("P05-LIBRARY", level="DEBUG")

# === DECLARE GLOBAL CONSTANTS ===

ROOT_DIR: Final[Path] = Path.cwd()

DATA_RAW_DIR: Final[Path] = ROOT_DIR / "data" / "raw" / "library"
ARTIFACTS_DIR: Final[Path] = ROOT_DIR / "artifacts" / "duckdb"
SQL_DIR: Final[Path] = ROOT_DIR / "sql" / "duckdb"

DB_PATH: Final[Path] = ARTIFACTS_DIR / "library.duckdb"

# === DECLARE HELPER FUNCTION:  READ SQL FROM PATH ===


def read_sql(sql_path: Path) -> str:
    """Read a SQL file from disk."""
    return sql_path.read_text(encoding="utf-8")


# === DECLARE HELPER FUNCTION:  RUN SQL ACTION (NO RESULTS) ===


def run_sql_script(con: duckdb.DuckDBPyConnection, sql_path: Path) -> None:
    """Execute a SQL action script file (DDL, COPY, or cleanup)."""
    LOG.info(f"RUN SQL script: {sql_path}")
    sql_text = read_sql(sql_path)
    con.execute(sql_text)
    LOG.info(f"DONE SQL script: {sql_path}")


# === DECLARE HELPER FUNCTION:  RUN SQL QUERY (LOG RESULTS) ===


def run_sql_query(con: duckdb.DuckDBPyConnection, sql_path: Path) -> None:
    """Execute a SQL query script file and log the results."""
    LOG.info("")
    LOG.info(f"RUN SQL query: {sql_path}")
    sql_text = read_sql(sql_path)

    result = con.execute(sql_text)
    rows = result.fetchall()
    columns = [col[0] for col in result.description]

    LOG.info("====================================")
    LOG.info(sql_path.name)
    LOG.info("====================================")
    LOG.info(", ".join(columns))

    for row in rows:
        LOG.info(", ".join(str(value) for value in row))


# === DEFINE THE MAIN FUNCTION ===


def main() -> None:
    """Run the library pipeline."""
    log_header(LOG, "P05 Custom Project (Library, DuckDB)")

    LOG.info("START main()")
    LOG.info(f"ROOT_DIR: {ROOT_DIR}")
    LOG.info(f"DATA_RAW_DIR: {DATA_RAW_DIR}")
    LOG.info(f"SQL_DIR: {SQL_DIR}")
    LOG.info(f"DB_PATH: {DB_PATH}")

    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

    con = duckdb.connect(str(DB_PATH))

    try:
        # STEP 1: CLEAN
        run_sql_script(con, SQL_DIR / "library_clean.sql")

        # STEP 2: BOOTSTRAP (create tables, load CSV data)
        run_sql_script(con, SQL_DIR / "library_bootstrap.sql")

        # STEP 3: RUN QUERIES
        run_sql_query(con, SQL_DIR / "library_query_checkouts_by_branch.sql")
        run_sql_query(con, SQL_DIR / "library_query_checkouts_by_material.sql")

        # STEP 4: RUN KPI QUERY
        run_sql_query(con, SQL_DIR / "library_query_kpi_system.sql")

        LOG.info("========================")
        LOG.info("Executed successfully!")
        LOG.info("========================")

    finally:
        con.close()

    LOG.info("END main()")


# === CONDITIONAL EXECUTION GUARD ===

if __name__ == "__main__":
    main()
