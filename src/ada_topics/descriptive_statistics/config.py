"""Definitions of source files for the current chapter."""

import itertools

from ada_topics.descriptive_statistics.absolute_relative_diffs import (
    SITE_CONTENTS as absolute_relative_diffs,
)
from ada_topics.descriptive_statistics.central_tendency_cardinal_data import (
    SITE_CONTENTS as central_tendency_cardinal_data,
)
from ada_topics.descriptive_statistics.central_tendency_ordinal_data import (
    SITE_CONTENTS as central_tendency_ordinal_data,
)
from ada_topics.descriptive_statistics.central_tendency_properties import (
    SITE_CONTENTS as central_tendency_properties,
)
from ada_topics.descriptive_statistics.data_sources import (
    SITE_CONTENTS as data_sources,
)
from ada_topics.descriptive_statistics.histograms import (
    SITE_CONTENTS as histograms,
)
from ada_topics.descriptive_statistics.missing_data import (
    SITE_CONTENTS as missing_data,
)
from ada_topics.descriptive_statistics.quantiles import (
    SITE_CONTENTS as quantiles,
)
from ada_topics.descriptive_statistics.stocks_flows_levels_changes import (
    SITE_CONTENTS as stocks_flows_levels_changes,
)
from ada_topics.descriptive_statistics.types_of_data_dtypes import (
    SITE_CONTENTS as types_of_data_dtypes,
)
from ada_topics.descriptive_statistics.what_are_data import (
    SITE_CONTENTS as what_are_data,
)

TOPICS = [
    what_are_data,
    types_of_data_dtypes,
    stocks_flows_levels_changes,
    absolute_relative_diffs,
    data_sources,
    missing_data,
    histograms,
    central_tendency_ordinal_data,
    central_tendency_cardinal_data,
    central_tendency_properties,
    quantiles,
]


SITE_CONTENTS = {
    "chapter_title": "Descriptive Statistics",
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
