"""Definitions of source files for the current chapter."""

import itertools

from ada_topics.plotly_graphs.modifying_plotly_graphs import (
    SITE_CONTENTS as modifying_plotly_graphs,
)
from ada_topics.plotly_graphs.plotly_intro import (
    SITE_CONTENTS as plotly_intro,
)

TOPICS = [
    plotly_intro,
    modifying_plotly_graphs,
]


SITE_CONTENTS = {
    "chapter_title": "Visualisations with plotly",
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
