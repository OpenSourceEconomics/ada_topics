"""Definitions of source files for the current chapter."""

import itertools

from ada_topics.jupyter_notebooks.creating_and_executing_cells import (
    SITE_CONTENTS as CREATING_AND_EXECUTING_CELLS,
)
from ada_topics.jupyter_notebooks.markdown_cells import SITE_CONTENTS as MARKDOWN_CELLS
from ada_topics.jupyter_notebooks.opening_notebooks import (
    SITE_CONTENTS as OPENING_NOTEBOOKS,
)

TOPICS = [
    OPENING_NOTEBOOKS,
    CREATING_AND_EXECUTING_CELLS,
    MARKDOWN_CELLS,
]
SITE_CONTENTS = {
    "chapter_title": "Data wrangling with pandas",
    "pages": tuple(
        itertools.chain(
            *[topic["pages"] for topic in TOPICS],
        ),
    ),
    "other": tuple(
        itertools.chain(
            *[topic["other"] for topic in TOPICS],
        ),
    ),
    "built": tuple(
        itertools.chain(
            *[topic["built"] for topic in TOPICS],
        ),
    ),
}
