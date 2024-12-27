"""Containers for collections of words."""

from collections.abc import Hashable, Mapping, Sequence
from copy import deepcopy
from pathlib import Path

from ruamel.yaml import YAML


class WordSet:
    """A set of words."""

    def __init__(self, words: Sequence[str]):
        self.__words = tuple(sorted(set(words)))

    @property
    def words(self) -> set[str]:
        """The set of words in this WordSet."""
        return self.__words

    @classmethod
    def from_file(cls, word_file: str | Path) -> "WordSet":
        """Load a WordSet from a file."""
        word_file = _normalize_path(word_file)
        if word_file.suffix in [".yml", ".yaml"]:
            return cls.from_yaml(word_file)
        else:
            raise ValueError(f"Unsupported extension {word_file.suffix}")

    @classmethod
    def from_yaml(cls, word_file: str | Path) -> "WordSet":
        """Load a WordSet from a yaml file."""
        word_file = _normalize_path(word_file)
        loader = YAML(typ="safe")
        with word_file.open(encoding="utf-8") as fp:
            word_list = loader.load(fp)
        del loader
        return cls(word_list)


class Dictionary(Mapping):
    """A container for labeled WordSets."""

    def __init__(self, starting_dict: dict[str, WordSet] | None = None):
        if starting_dict is None:
            starting_dict = {}
        self.__dictionary = deepcopy(starting_dict)

    @classmethod
    def from_directory(cls, directory: str | Path) -> "Dictionary":
        """Load a dictionary from a directory of files."""
        directory = _normalize_path(directory)
        if not directory.is_dir():
            raise ValueError("Please specify a directory")
        word_sets = {}
        file_list = [path for path in directory.iterdir() if path.is_file()]
        for path in file_list:
            word_sets[path.stem] = WordSet.from_file(path)
        return Dictionary(word_sets)

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


def _normalize_path(path: str | Path) -> Path:
    if isinstance(path, str):
        return Path(path)
    else:
        return path
