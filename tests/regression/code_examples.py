import runpy
import subprocess
from pathlib import Path

import pytest

base_path = Path(__file__).parent.parent.parent
markdown_dir = base_path / "doc/source/Code_Examples"
markdowns = [md for md in markdown_dir.glob("*.md") if md.name != "index.md"]
markdowns.append(base_path / "README.md")


@pytest.mark.parametrize("markdown", markdowns)
def test_markdown(markdown: Path, tmp_path, util):
    tmp_py = tmp_path / markdown.with_suffix(".py").name

    # Convert markdown file to py file in a tmp directory
    subprocess.run(["jupytext", "--output", tmp_py, markdown])

    util.update_file_with_token_and_qa(tmp_py)

    runpy.run_path(tmp_py.resolve().as_posix())
