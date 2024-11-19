"""Definitions of source files for the current chapter."""

import itertools

from ada_topics.stats_dispersion_concentration.absolute import SITE_CONTENTS as absolute
from ada_topics.stats_dispersion_concentration.concentration_quantile import (
    SITE_CONTENTS as concentration_quantile,
)
from ada_topics.stats_dispersion_concentration.gini import SITE_CONTENTS as gini
from ada_topics.stats_dispersion_concentration.lorenz_curves import (
    SITE_CONTENTS as lorenz_curves,
)
from ada_topics.stats_dispersion_concentration.measurement_error import (
    SITE_CONTENTS as measurement_error,
)
from ada_topics.stats_dispersion_concentration.skewness import SITE_CONTENTS as skewness
from ada_topics.stats_dispersion_concentration.squared import SITE_CONTENTS as squared

TOPICS = [
    absolute,
    squared,
    skewness,
    measurement_error,
    concentration_quantile,
    lorenz_curves,
    gini,
]


SITE_CONTENTS = {
    "chapter_title": "Descriptive Statistics — Measures of dispersion & concentration",
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
