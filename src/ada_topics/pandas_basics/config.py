"""Definitions of source files for the current chapter."""

import itertools

from ada_topics.pandas_basics.series_intro import SITE_CONTENTS as SERIES_INTRO

TOPICS = [
    SERIES_INTRO,
]


SITE_CONTENTS = {
    "chapter_title": "Pandas Basics",
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
