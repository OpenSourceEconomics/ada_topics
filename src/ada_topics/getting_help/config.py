"""Definitions of source files for the current chapter."""

import itertools

from ada_topics.getting_help.asking import SITE_CONTENTS as ASKING
from ada_topics.getting_help.on_the_web import SITE_CONTENTS as ON_THE_WEB
from ada_topics.getting_help.strategies import SITE_CONTENTS as STRATEGIES
from ada_topics.getting_help.tracebacks import SITE_CONTENTS as TRACEBACKS
from ada_topics.getting_help.within_notebooks import SITE_CONTENTS as WITHIN_NOTEBOOKS

TOPICS = [
    STRATEGIES,
    TRACEBACKS,
    WITHIN_NOTEBOOKS,
    ON_THE_WEB,
    ASKING,
]


SITE_CONTENTS = {
    "chapter_title": "Template Chapter",
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
