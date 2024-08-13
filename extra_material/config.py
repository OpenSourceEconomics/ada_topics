"""Definitions of source files for the current chapter."""

import itertools

from ada_topics.extra_material.data_conceptualization import (
    SITE_CONTENTS as DATA_CONCEPTUALIZATION,
)

TOPICS = [
    DATA_CONCEPTUALIZATION,
]


SITE_CONTENTS = {
    "chapter_title": "Template Chapter",
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
