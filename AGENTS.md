@.ai-instructions/profiles/tier-b-course.md

@.ai-instructions/modules/pytask.md

# Applied Data Analytics: Topics

## Overview

Topic-based screencasts and material for Applied Data Analytics, published at
https://www.wiwi.uni-bonn.de/gaudecker/_static/applied-data-analytics. The course repo
(`ada_course`) links to these topics week by week.

## Build & Test

- `pixi run npm install` — once, for Slidev
- `pixi run pytask` — export screencast slides, generate `site_source/` and the table of
  contents, build the Jupyter Book (v1, `--warningiserror`), and copy it to
  `~/admin/website/_static/applied-data-analytics` if that directory exists. On the
  Linux boxes launch it as `zsh -ic "cap pixi run pytask"`.
- `./developer_run.sh` — clean rebuild (removes `node_modules`, `site_source`,
  `.slides_pdf`)
- `prek run --all-files` — lint, format, and type-check

## Architecture

- `src/ada_topics/<chapter>/<topic>/` — each topic has `config.py`, objectives and
  materials, and usually `screencast/slides.md` (Slidev).
- `src/ada_topics/config.py` — paths and `load_sources`; `task_create_book.py` builds
  the site, `task_export_screencasts.py` the slide PDFs.
- `site_source/` is generated and ignored. Delete a stale `site_source/_toc.yml` if the
  build complains about missing pages.
- Plotly examples use `pio.templates.default = "plotly_dark+presentation"`.
- Work happens directly on `main`; commits there need `SKIP=no-commit-to-branch`.
