"""Definitions of source files for the current chapter."""

import itertools

from ada_topics.python_basics.assigning_variables import (
    SITE_CONTENTS as ASSIGNING_VARIABLES,
)
from ada_topics.python_basics.functions_basics import (
    SITE_CONTENTS as FUNCTIONS_BASICS,
)
from ada_topics.python_basics.functions_principles import (
    SITE_CONTENTS as FUNCTIONS_PRINCIPLES,
)
from ada_topics.python_basics.scalar_types import (
    SITE_CONTENTS as SCALAR_TYPES,
)
from ada_topics.python_basics.strings_intro import (
    SITE_CONTENTS as STRINGS_INTRO,
)

TOPICS = [
    ASSIGNING_VARIABLES,
    SCALAR_TYPES,
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
