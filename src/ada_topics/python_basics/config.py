"""Definitions of source files for the current chapter."""

import itertools

from ada_topics.python_basics.assignment_scalars import (
    SITE_CONTENTS as ASSIGNMENT_SCALARS,
)
from ada_topics.python_basics.boolean_logic import (
    SITE_CONTENTS as BOOLEAN_LOGIC,
)
from ada_topics.python_basics.functions_basics import (
    SITE_CONTENTS as FUNCTIONS_BASICS,
)
from ada_topics.python_basics.functions_principles import (
    SITE_CONTENTS as FUNCTIONS_PRINCIPLES,
)
from ada_topics.python_basics.strings_intro import (
    SITE_CONTENTS as STRINGS_INTRO,
)

TOPICS = [
    ASSIGNMENT_SCALARS,
    BOOLEAN_LOGIC,
    STRINGS_INTRO,
    FUNCTIONS_BASICS,
    FUNCTIONS_PRINCIPLES,
]

SITE_CONTENTS = {
    "chapter_title": "Python Basics",
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
