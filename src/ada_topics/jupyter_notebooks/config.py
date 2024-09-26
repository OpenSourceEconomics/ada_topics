"""Definitions of source files for the current chapter."""

import itertools

from ada_topics.jupyter_notebooks.early_pitfalls import SITE_CONTENTS as EARLY_PITFALLS
from ada_topics.jupyter_notebooks.markdown import SITE_CONTENTS as MARKDOWN
from ada_topics.jupyter_notebooks.working_with_cells import (
    SITE_CONTENTS as WORKING_WITH_CELLS,
)

TOPICS = [
    WORKING_WITH_CELLS,
    MARKDOWN,
    EARLY_PITFALLS,
]
SITE_CONTENTS = {
    "chapter_title": "Working with Jupyter Notebooks",
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
