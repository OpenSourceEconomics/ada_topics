"""Create figure for this subchapter's screencast."""

import shutil
import subprocess
from pathlib import Path
from typing import Annotated

from pytask import Product, task

from ada_topics.config import SITE_SOURCE_DIR, SRC


def find_orig_screencasts():
    """Find all files matching screencast pattern, except for template chapter."""
    return [
        sc
        for sc in SRC.glob("**/screencast/slides.md")
        if SRC / "chapter_template" not in sc.parents
    ]


for orig_screencast in find_orig_screencasts():
    orig_dir = orig_screencast.parent
    screencast_dir = SITE_SOURCE_DIR / orig_dir.relative_to(SRC)
    screencast_md = screencast_dir / orig_screencast.name

    chapter_name = orig_dir.parent.parent.name
    topic_name = orig_dir.parent.name
    screencast_pdf = screencast_dir.parent / f"{chapter_name}-{topic_name}.pdf"

    # Just copy these guys over
    shutil.copy(SRC / "slidev_config" / "style.css", orig_dir / "style.css")

    # TODO(@hmgaudecker): Add symbolic links from src/.../screencast/public to generated
    # figures (get example in inspecting/summarizing to work):
    # https://github.com/OpenSourceEconomics/ada_topics/issues/6

    @task(id=f"{chapter_name}, {topic_name}")
    def task_export_pdf(
        screencast_md: Path = orig_screencast,
        screencast_pdf: Annotated[Path, Product] = screencast_pdf,
    ):
        """Create slidev presentation and export to pdf."""
        subprocess.run(
            f"npx slidev export {screencast_md.absolute()}"
            f" --output {screencast_pdf.absolute()}",
            shell=True,
            check=True,
        )
