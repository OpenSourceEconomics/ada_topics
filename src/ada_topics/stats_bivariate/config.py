"""Definitions of source files for the current chapter."""

import itertools

from ada_topics.stats_bivariate.correlation import SITE_CONTENTS as correlation
from ada_topics.stats_bivariate.covariance import SITE_CONTENTS as covariance
from ada_topics.stats_bivariate.ols_derivation import SITE_CONTENTS as ols_derivation
from ada_topics.stats_bivariate.ols_intuition import SITE_CONTENTS as ols_intuition
from ada_topics.stats_bivariate.regression_intuition import (
    SITE_CONTENTS as regression_intuition,
)
from ada_topics.stats_bivariate.strategies import SITE_CONTENTS as strategies

TOPICS = [
    strategies,
    covariance,
    correlation,
    regression_intuition,
    ols_intuition,
    ols_derivation,
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
