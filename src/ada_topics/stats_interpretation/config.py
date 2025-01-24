"""Definitions of source files for the current chapter."""

import itertools

from ada_topics.stats_interpretation.graphs_causality import (
    SITE_CONTENTS as graphs_causality,
)
from ada_topics.stats_interpretation.graphs_models import (
    SITE_CONTENTS as graphs_models,
)
from ada_topics.stats_interpretation.graphs_terminology import (
    SITE_CONTENTS as graphs_terminology,
)
from ada_topics.stats_interpretation.observing_intervening_counterfactuals import (
    SITE_CONTENTS as observing_intervening_counterfactuals,
)
from ada_topics.stats_interpretation.proxy_failure import (
    SITE_CONTENTS as proxy_failure,
)
from ada_topics.stats_interpretation.selection_intro import (
    SITE_CONTENTS as selection_intro,
)
from ada_topics.stats_interpretation.selection_models import (
    SITE_CONTENTS as selection_models,
)
from ada_topics.stats_interpretation.selection_one_sided import (
    SITE_CONTENTS as selection_one_sided,
)
from ada_topics.stats_interpretation.selection_two_sided import (
    SITE_CONTENTS as selection_two_sided,
)

TOPICS = [
    graphs_terminology,
    graphs_models,
    graphs_causality,
    observing_intervening_counterfactuals,
    selection_intro,
    selection_models,
    selection_one_sided,
    selection_two_sided,
    proxy_failure,
]


SITE_CONTENTS = {
    "chapter_title": "Data analysis — Interpretation challenges",
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
