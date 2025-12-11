# Copilot instructions for `geodata-sampler`

Purpose: Help AI coding agents be immediately productive in this repository by describing the architecture, developer workflows, and project-specific conventions.

References:
- Must: Read and respect `.github/instructions/` files if it exists.

Quick setup
- Use Pipenv for local development: `pipenv install --dev` then `pipenv shell`.
- Create the Jupyter kernel (optional):
  `python -m ipykernel install --user --name=geodata-sampler-env --display-name="Geodata Sampler Kernel"`
- Typical run for notebooks: `jupyter lab` and open files in `notebooks/` (e.g. `generate_geoparquet_points.ipynb`).

Project layout (essential files)
- `core/` : main library modules. Important files:
- `notebooks/` : exploratory notebooks and runnable examples. Use these as canonical usage examples, particularly `generate_geoparquet_points.ipynb` which shows geopandas/parquet writing to `data/generated/`.
- `data/generated/` : repository output sink for generated GeoJSON / parquet files.
- `Pipfile` : source of truth for dependencies (uses `python_version = "3.14"`).

Data & architecture notes
- The library intentionally models GeoJSON as Python dicts and simple NamedTuples rather than heavy ORM objects.
- Prefer functional programming style: pure functions that take and return dicts/lists.
- Avoid to use shortcuts as variable name conventions (e.g., `gdf` for GeoDataFrame) in core library code; use full names for clarity.

Developer workflows (explicit)
- Install deps: `pipenv install --dev` (use `Pipfile`).
- Activate: `pipenv shell` before running notebooks or scripts.
- Run notebooks: `jupyter lab` or use VS Code Jupyter extension; the notebooks demonstrate intended usage and data paths.
- Run tests: `pipenv run pytest` (no custom test harness currently present).

If a `.github/copilot-instructions.md` already exists
- Merge conservatively: preserve any custom agent instructions and append updated sections above. Prefer the repository `README.md`, `Pipfile`, and `notebooks/` as canonical sources.

Next steps for reviewers
- Tell me if you'd like: a) tighter linting/format rules to include, b) explicit test examples, or c) an automation script that runs the example notebooks and verifies outputs.

-- End of instructions --
