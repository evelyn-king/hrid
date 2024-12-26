"""Containers for collections of words."""

from collections.abc import Hashable, Mapping, Sequence
from copy import deepcopy
from pathlib import Path

from ruamel.yaml import YAML


class WordSet:
    """A set of words."""

    def __init__(self, words: Sequence[str]):
        self.__words = tuple(set(words))

    @property
    def words(self) -> set[str]:
        """The set of words in this WordSet."""
        return self.__words()

    @classmethod
    def from_yaml(cls, word_file: str | Path) -> "WordSet":
        """Load a WordSet from a yaml file."""
        if isinstance(word_file, str):
            word_file = Path(word_file)
        loader = YAML(typ="safe")
        with word_file.open(word_file, encoding="utf-8") as fp:
            word_list = loader.load(fp)
        del loader
        return word_list


class Dictionary(Mapping):
    """A container for labeled WordSets."""

    def __init__(self, starting_dict: dict[str, WordSet] | None = None):
        if starting_dict is None:
            starting_dict = {}
        self.__dictionary = deepcopy(starting_dict)

    def __getitem__(self, key: Hashable) -> WordSet:
        return self.__dictionary[key]

    def __iter__(self):
        return self.__dictionary.__iter__()

    def __len__(self) -> int:
        return len(self.__dictionary)

    def __setitem__(self, key: Hashable, item: WordSet) -> None:
        if key in self:
            msg = f"Key: {key} is already set!"
            raise ValueError(msg)
        if not isinstance(item, WordSet):
            msg = f"{item} is not a WordSet!"
            raise TypeError(msg)
        self.__dictionary[key] = item

    def __delitem__(self, key: Hashable) -> None:
        if key not in self:
            msg = f"Key: {key} is not in this WordSet"
            raise KeyError(msg)
        del self.__dictionary[key]
