# Your Files

Projects include instructor example files that end with `_case`.
Keep these as working examples.

You will generally copy the instructor file, rename it with your alias,
and run your version in addition to the instructor version.

## Choose Your Name (example: `stellar_analytics`)

You may use your real name or any professional alias.
You are **never required to use your real name**.

Naming rules:

- all lowercase
- no spaces (use underscores as needed)

## 1. Python Files

Copy the instructor Python file and rename the copy using your alias.

```text
src/datafun/app_case.py
src/datafun/app_stellar_analytics.py
```

## 2. Python File Execution Command

In your `README.md`, add a line with the execution command just after the instructor command.
Use this command to run your file.

```shell
uv run python -m datafun.app_retail_duckdb_case
uv run python -m datafun.app_retail_duckdb_stellar_analytics
```

## 3. Data Files (If Provided)

Copy the instructor data file(s) if provided and rename the copy using your alias.
This helps discover how important paths are.
For assistance, use the VS Code search in files (the microscope icon on the left)
to find everywhere that `data/` appears in the project.

Paths are critical and can be hard to get right.
That's why we log them, and learn how to search for them.
In Python, we declare constants to help keep them straight.

```text
data/raw/retail/sale_yourname.csv
data/raw/retail/store_yourname.csv
```

You may modify the copied dataset as needed for your project,
or choose your own dataset if appropriate.
