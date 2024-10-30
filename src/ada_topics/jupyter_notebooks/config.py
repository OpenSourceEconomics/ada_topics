"""Definitions of source files for the current chapter."""

import itertools

from ada_topics.jupyter_notebooks.early_pitfalls import SITE_CONTENTS as early_pitfalls
from ada_topics.jupyter_notebooks.markdown import SITE_CONTENTS as markdown
from ada_topics.jupyter_notebooks.working_with_cells import (
    SITE_CONTENTS as working_with_cells,
)

TOPICS = [
    working_with_cells,
    markdown,
    early_pitfalls,
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
