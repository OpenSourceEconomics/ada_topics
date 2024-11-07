"""Definitions of source files for the current chapter."""

import itertools

from ada_topics.stats_dispersion_concentration.absolute import SITE_CONTENTS as absolute
from ada_topics.stats_dispersion_concentration.kurtosis import SITE_CONTENTS as kurtosis
from ada_topics.stats_dispersion_concentration.skewness import SITE_CONTENTS as skewness
from ada_topics.stats_dispersion_concentration.squared import SITE_CONTENTS as squared

TOPICS = [
    absolute,
    squared,
    kurtosis,
    skewness,
]


SITE_CONTENTS = {
    "chapter_title": "Statistics — Dispersion & concentration",
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
