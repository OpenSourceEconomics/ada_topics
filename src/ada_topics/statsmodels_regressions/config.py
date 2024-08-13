"""Definitions of source files for the current chapter."""

import itertools

from ada_topics.statsmodels_regressions.import_formula import (
    SITE_CONTENTS as IMPORT_FORMULA,
)
from ada_topics.statsmodels_regressions.results_objects import (
    SITE_CONTENTS as RESULTS_OBJECTS,
)

TOPICS = [
    IMPORT_FORMULA,
    RESULTS_OBJECTS,
]
SITE_CONTENTS = {
    "chapter_title": "Regressions with Statsmodels",
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
