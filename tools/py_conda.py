"""
This snippet must be in Anaconda environment
build environment for this Snippet just by installing conda package `pip install conda` in a conda virtual environment
"""

import conda.cli


def install_conda_package(pkg: str):
    conda.cli.main('conda', 'install', '-y', pkg)
