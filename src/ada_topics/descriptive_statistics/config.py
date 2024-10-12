"""Definitions of source files for the current chapter."""

import itertools

from ada_topics.descriptive_statistics.central_tendency_cardinal_data import (
    SITE_CONTENTS as CENTRAL_TENDENCY_CARDINAL_DATA,
)
from ada_topics.descriptive_statistics.central_tendency_ordinal_data import (
    SITE_CONTENTS as CENTRAL_TENDENCY_ORDINAL_DATA,
)
from ada_topics.descriptive_statistics.histograms import (
    SITE_CONTENTS as HISTOGRAMS,
)
from ada_topics.descriptive_statistics.what_are_data import (
    SITE_CONTENTS as WHAT_ARE_DATA,
)

TOPICS = [
    WHAT_ARE_DATA,
    HISTOGRAMS,
    CENTRAL_TENDENCY_ORDINAL_DATA,
    CENTRAL_TENDENCY_CARDINAL_DATA,
]


SITE_CONTENTS = {
    "chapter_title": "Descriptive Statistics",
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
