"""Definitions of source files for the current chapter."""

import itertools

from ada_topics.python_basics.assignment_and_scalar_types import (
    SITE_CONTENTS as ASSIGNMENT_AND_SCALAR_TYPES,
)
from ada_topics.python_basics.getting_started_with_notebooks import (
    SITE_CONTENTS as GETTING_STARTED_WITH_NOTEBOOKS,
)

TOPICS = [GETTING_STARTED_WITH_NOTEBOOKS, ASSIGNMENT_AND_SCALAR_TYPES]

SITE_CONTENTS = {
    "chapter_title": "Python Basics",
    "pages": tuple(
        itertools.chain(
            ("content_objectives.md",),
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
