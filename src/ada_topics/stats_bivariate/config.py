"""Definitions of source files for the current chapter."""

import itertools

from ada_topics.stats_bivariate.correlation import SITE_CONTENTS as correlation
from ada_topics.stats_bivariate.covariance import SITE_CONTENTS as covariance
from ada_topics.stats_bivariate.strategies import SITE_CONTENTS as strategies

TOPICS = [
    strategies,
    covariance,
    correlation,
]


SITE_CONTENTS = {
    "chapter_title": "Descriptive Statistics — Measures for bivariate data",
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
