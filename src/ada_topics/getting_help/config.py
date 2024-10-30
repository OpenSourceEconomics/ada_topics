"""Definitions of source files for the current chapter."""

import itertools

from ada_topics.getting_help.asking import SITE_CONTENTS as asking
from ada_topics.getting_help.on_the_web import SITE_CONTENTS as on_the_web
from ada_topics.getting_help.strategies import SITE_CONTENTS as strategies
from ada_topics.getting_help.tracebacks import SITE_CONTENTS as tracebacks
from ada_topics.getting_help.within_notebooks import SITE_CONTENTS as within_notebooks

TOPICS = [
    strategies,
    tracebacks,
    within_notebooks,
    on_the_web,
    asking,
]


SITE_CONTENTS = {
    "chapter_title": "Getting help",
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
