"""Definitions of source files for the current chapter."""

import itertools

from ada_topics.pandas_data.birds_eye import (
    SITE_CONTENTS as BIRDS_EYE,
)
from ada_topics.pandas_data.datatypes import (
    SITE_CONTENTS as DATATYPES,
)
from ada_topics.pandas_data.groupby import SITE_CONTENTS as GROUPBY

TOPICS = [
    BIRDS_EYE,
    DATATYPES,
    GROUPBY,
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
