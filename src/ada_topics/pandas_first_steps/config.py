"""Definitions of source files for the current chapter."""

import itertools

from ada_topics.pandas_first_steps.columns_and_indices import SITE_CONTENTS as COLUMNS_AND_INDICES
from ada_topics.pandas_first_steps.creating_variables import SITE_CONTENTS as CREATING_VARIABLES
from ada_topics.pandas_first_steps.dataframes_and_series import (
    SITE_CONTENTS as DATAFRAMES_AND_SERIES,
)
from ada_topics.pandas_first_steps.datatypes import SITE_CONTENTS as DATATYPES
from ada_topics.pandas_first_steps.functional import SITE_CONTENTS as FUNCTIONAL_DATA_MANAGEMENT
from ada_topics.pandas_first_steps.inspecting_and_summarizing import (
    SITE_CONTENTS as INSPECTING_AND_SUMMARIZING,
)
from ada_topics.pandas_first_steps.loading_and_saving import SITE_CONTENTS as LOADING_AND_SAVING
from ada_topics.pandas_first_steps.merging import SITE_CONTENTS as MERGING
from ada_topics.pandas_first_steps.rules import SITE_CONTENTS as RULES
from ada_topics.pandas_first_steps.selection import SITE_CONTENTS as SELECTION
from ada_topics.pandas_first_steps.what_is_pandas import SITE_CONTENTS as WHAT_IS_PANDAS

TOPICS = [
    WHAT_IS_PANDAS,
    DATAFRAMES_AND_SERIES,
    DATATYPES,
    LOADING_AND_SAVING,
    COLUMNS_AND_INDICES,
    SELECTION,
    INSPECTING_AND_SUMMARIZING,
    CREATING_VARIABLES,
    RULES,
    MERGING,
    FUNCTIONAL_DATA_MANAGEMENT,
]
SITE_CONTENTS = {
    "chapter_title": "First steps with pandas",
    "pages": tuple(
        itertools.chain(
            ("content_objectives.md",),
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
