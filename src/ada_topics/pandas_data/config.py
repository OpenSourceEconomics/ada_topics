"""Definitions of source files for the current chapter."""

import itertools

from ada_topics.pandas_data.birds_eye import (
    SITE_CONTENTS as BIRDS_EYE,
)

TOPICS = [
    BIRDS_EYE,
]
SITE_CONTENTS = {
    "chapter_title": "First steps with pandas",
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