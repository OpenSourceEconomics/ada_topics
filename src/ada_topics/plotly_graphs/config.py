"""Definitions of source files for the current chapter."""

import itertools

from ada_topics.plotly_graphs.modify_plotly_graphs import (
    SITE_CONTENTS as MODIFY_PLOTLY_GRAPHS,
)
from ada_topics.plotly_graphs.plotly_intro import (
    SITE_CONTENTS as PLOTLY_INTRO,
)

TOPICS = [
    PLOTLY_INTRO,
    MODIFY_PLOTLY_GRAPHS,
]


SITE_CONTENTS = {
    "chapter_title": "Plotly Graphs",
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
