"""Definitions of source files for the current chapter."""

import itertools

from ada_topics.stats_misc.equivalence_scales import SITE_CONTENTS as equivalence_scales

TOPICS = [
    equivalence_scales,
]


SITE_CONTENTS = {
    "chapter_title": "Descriptive Statistics — Miscellaneous topics",
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
