# datafun-05-sql

[![Workflow Guide](https://img.shields.io/badge/Pro--Guide-pro--analytics--02-green)](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](./pyproject.toml)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Professional Python project: relational data and SQL analytics.

Data analytics requires a variety of skills.
This course builds capabilities through working projects.

In the age of generative AI, durable skills are grounded in real work:
setting up a professional environment,
reading and running code,
understanding the logic,
and pushing work to a shared repository.
Each project follows the structure of professional Python projects.
We learn by doing.

## This Project

This project introduces **relational data and SQL** used when storing structured data in tables.
Analysts are typically highly skilled at both SQL and Python.

Sample datasets are provided in the `data/raw` folder
across several topic domains:

- **retail** - a store records many sales (the worked example)
- **library** - a library branch manages many checkouts
- **shelter** - a shelter manages many animal adoptions
- **civic_event** - an event manages many attendees

Each domain has two related tables in a 1-to-many relationship.
You will run the retail example, then implement the same pipeline for a domain you choose.

## Working Files

You'll work with just these areas:

- **data/raw/\*** - raw CSV input files
- **data/processed/** - processed data outputs, if created
- **artifacts/** - generated database files, logs, or reports
- **docs/** - the project narrative and documentation
- **sql/** - SQL query files
- **src/datafun/** - Python orchestration scripts
- **pyproject.toml** - update project metadata
- **zensical.toml** - update documentation site metadata

## Instructions (pro-analytics-02)

Follow the
[step-by-step workflow guide](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to complete:

1. Phase 1. **Start & Run**
2. Phase 2. **Change Authorship**
3. Phase 3. **Read & Understand**
4. Phase 4. **Modify**
5. Phase 5. **Apply**

## Challenges

Challenges are expected.
Sometimes instructions may not quite match your operating system.
When issues occur, share screenshots, error messages, and details about what you tried.
Working through issues is part of implementing professional projects.

## Success

After completing Phase 1. **Start & Run**, you'll have your own GitHub project,
running on your machine.

Running the examples should create generated database files in `artifacts/`.

A new file `project.log` will appear in the root project folder
and you should see:

```shell
========================
Executed successfully!
========================
```

A new file `project.log` will appear in the root project folder.

## Command Reference

The commands below are used in the workflow guide above.
They are provided here for convenience.

Follow the guide for the **full instructions**.

<details>
<summary>Show command reference</summary>

### In a machine terminal (open in your `Repos` folder)

After you get a copy of this repo in your own GitHub account,
open a machine terminal in your `Repos` folder:

```shell
# Replace username with YOUR GitHub username.
git clone https://github.com/amforphilosophy-sketch/datafun-05-sql

cd datafun-05-sql
code .
```

### In a VS Code terminal

These are listed for convenience.
For best results, follow the detailed instructions in
[pro-analytics-02 guide](https://denisecase.github.io/pro-analytics-02/).

```shell
uv self update
uv python pin 3.14
uv lock --upgrade
uv sync --extra dev --extra docs --upgrade

uvx pre-commit install

git add -A
uvx pre-commit run --all-files
# repeat if changes were made
uvx pre-commit run --all-files

# run the example pipelines (duckdb and sqlite)
uv run python -m datafun.app_retail_duckdb_case
uv run python -m datafun.app_retail_sqlite_case

# do chores
uv run ruff format .
uv run ruff check . --fix
uv run python -m pyright
uv run python -m pytest
uv run python -m zensical build

# save progress
git add -A
git commit -m "update"
git push -u origin main
```

</details>

## Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.
- You do not need to add to or modify `tests/`. They are provided for example only.
- Many files are silent helpers. Explore as you like, but nothing is required.
- You do NOT not to understand everything; understanding builds naturally over time.

## Troubleshooting >>>

If you see something like this in your terminal: `>>>` or `...`
You accidentally started Python interactive mode.
It happens.
Press `Ctrl+c` (both keys together) or `Ctrl+Z` then `Enter` on Windows.

## DuckDB Example Output and Modification

### My Modification

I added a new KPI query, **Total Revenue by Region**, alongside the instructor's revenue-by-store query. The original `case_retail_query_kpi_revenue.sql` reports revenue per individual store. My new query, `mohmand_retail_query_kpi_region.sql`, joins the store and sale tables, groups results with `GROUP BY s.region`, aggregates with `SUM`, `COUNT`, and `AVG`, and sorts by `total_revenue` descending. This rolls store-level data up to the regional level, which is useful for comparing overall regional performance rather than individual stores.

### Run Command

```shell
uv run python -m datafun.app_retail_duckdb_mohmand
```

### My Output

```shell
| INFO | P05 | RUN SQL query: /Users/ahmadmohmand/Repos/datafun-05-sql/sql/duckdb/mohmand_retail_query_kpi_region.sql
| INFO | P05 | ====================================
| INFO | P05 | mohmand_retail_query_kpi_region.sql
| INFO | P05 | ====================================
| INFO | P05 | region, sale_count, total_revenue, avg_sale_amount
| INFO | P05 | North, 20, 3359.0, 167.95
| INFO | P05 | South, 10, 1868.0, 186.8
| INFO | P05 | ====================================
| INFO | P05 | Executed successfully!
| INFO | P05 | END main()
```

### What I Observed

North had double the sales volume of South (20 vs 10) and the higher total revenue ($3,359.00 vs $1,868.00). However, South had the higher average sale amount ($186.80 vs $167.95). Grouping by region surfaces this trade-off between volume and per-sale value, an insight that the store-level query alone does not make obvious.
