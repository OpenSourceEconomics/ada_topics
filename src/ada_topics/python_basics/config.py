"""Definitions of source files for the current chapter."""

import itertools

from ada_topics.python_basics.assignment_calculations import (
    SITE_CONTENTS as assignment_calculations,
)
from ada_topics.python_basics.boolean_logic import (
    SITE_CONTENTS as boolean_logic,
)
from ada_topics.python_basics.dicts import SITE_CONTENTS as dicts
from ada_topics.python_basics.functions_basics import SITE_CONTENTS as functions_basics
from ada_topics.python_basics.if_conditions import SITE_CONTENTS as if_conditions
from ada_topics.python_basics.imports import (
    SITE_CONTENTS as imports,
)
from ada_topics.python_basics.lists_tuples import SITE_CONTENTS as lists_tuples
from ada_topics.python_basics.print import SITE_CONTENTS as print  # noqa: A001
from ada_topics.python_basics.scalar_types import (
    SITE_CONTENTS as scalar_types,
)
from ada_topics.python_basics.tracebacks import SITE_CONTENTS as tracebacks

TOPICS = [
    assignment_calculations,
    scalar_types,
    boolean_logic,
    imports,
    print,
    tracebacks,
    lists_tuples,
    dicts,
    if_conditions,
    functions_basics,
    # strings_intro,
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
