"""Definitions of source files for the current chapter."""

import itertools

from ada_topics.pandas_basics.boolean_indexing import SITE_CONTENTS as boolean_indexing
from ada_topics.pandas_basics.concatenate import SITE_CONTENTS as concatenate
from ada_topics.pandas_basics.dataframes_indexing_slicing import (
    SITE_CONTENTS as dataframes_indexing_slicing,
)
from ada_topics.pandas_basics.dataframes_intro import SITE_CONTENTS as dataframes_intro
from ada_topics.pandas_basics.dataframes_reductions import (
    SITE_CONTENTS as dataframes_reductions,
)
from ada_topics.pandas_basics.groupby import SITE_CONTENTS as groupby
from ada_topics.pandas_basics.merge import SITE_CONTENTS as merge
from ada_topics.pandas_basics.missing_data import SITE_CONTENTS as missing_data
from ada_topics.pandas_basics.multiindices import SITE_CONTENTS as multiindices
from ada_topics.pandas_basics.quantiles import SITE_CONTENTS as quantiles
from ada_topics.pandas_basics.query import SITE_CONTENTS as query
from ada_topics.pandas_basics.series_intro import SITE_CONTENTS as series_intro
from ada_topics.pandas_basics.shift_diff import SITE_CONTENTS as shift_diff
from ada_topics.pandas_basics.simulating_data import SITE_CONTENTS as simulating_data
from ada_topics.pandas_basics.types_of_data_dtypes import (
    SITE_CONTENTS as types_of_data_dtypes,
)

TOPICS = [
    series_intro,
    types_of_data_dtypes,
    quantiles,
    boolean_indexing,
    missing_data,
    dataframes_intro,
    dataframes_indexing_slicing,
    dataframes_reductions,
    groupby,
    query,
    multiindices,
    shift_diff,
    concatenate,
    merge,
    simulating_data,
]


SITE_CONTENTS = {
    "chapter_title": "Pandas Basics",
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
