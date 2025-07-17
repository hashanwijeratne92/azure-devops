"""
A minimal function to prove the pipeline can
install dependencies, import your code and run tests.
"""

import os


def greet() -> str:
    """
    Returns a friendly greeting. If the environment
    variable USERNAME is set (e.g. in your pipeline variables),
    it personalises the message.
    """
    name = os.getenv("USERNAME", "Azure DevOps")
    return f"Hello, {name}! This build ran successfully."
