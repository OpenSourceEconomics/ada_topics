"""Definitions of source files for the current chapter."""

import itertools

from ada_topics.python_basics.assignment_and_scalar_types import (
    SITE_CONTENTS as ASSIGNMENT_AND_SCALAR_TYPES,
)
from ada_topics.python_basics.functions_basics import (
    SITE_CONTENTS as FUNCTIONS_BASICS,
)
from ada_topics.python_basics.functions_principles import (
    SITE_CONTENTS as FUNCTIONS_PRINCIPLES,
)

TOPICS = [
    ASSIGNMENT_AND_SCALAR_TYPES,
    FUNCTIONS_BASICS,
    FUNCTIONS_PRINCIPLES,
]

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
