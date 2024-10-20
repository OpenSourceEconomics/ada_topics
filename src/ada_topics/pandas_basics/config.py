"""Definitions of source files for the current chapter."""

import itertools

from ada_topics.pandas_basics.series_intro import SITE_CONTENTS as SERIES_INTRO
from ada_topics.pandas_basics.types_of_data_dtypes import (
    SITE_CONTENTS as TYPES_OF_DATA_DTYPES,
)

TOPICS = [
    SERIES_INTRO,
    TYPES_OF_DATA_DTYPES,
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
