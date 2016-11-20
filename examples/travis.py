import os

from configbuilder.builder.base import BaseYmlBuilder


print BaseYmlBuilder(
    language='python',
    python=['2.7', '3.5'],
    install=[
        'sudo apt-get update -y',
        """if [[ "$TRAVIS_PYTHON_VERSION" == "2.7" ]]; then else fi""".strip(os.linesep)
    ],
    script=['py.test']
)
