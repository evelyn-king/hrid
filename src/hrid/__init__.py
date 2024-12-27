"""hrid: A Python library for generating human readable ids."""

from hrid._version import __version__
from hrid.generator import HRIDGenerator, hrid
from hrid.sets import Dictionary, WordSet

__all__ = ["__version__", "Dictionary", "WordSet", "HRIDGenerator", "hrid"]
