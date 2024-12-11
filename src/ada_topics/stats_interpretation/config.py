"""Definitions of source files for the current chapter."""

import itertools

from ada_topics.stats_interpretation.graphs_terminology import (
    SITE_CONTENTS as subchapter_slug,
)

TOPICS = [
    subchapter_slug,
]


SITE_CONTENTS = {
    "chapter_title": "Data analysis — Interpretation challenges",
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