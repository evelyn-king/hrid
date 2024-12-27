"""Modules containing HRID generators."""

import random
from collections.abc import Sequence
from pathlib import Path

from hrid.sets import Dictionary, WordSet

DICTIONARY_DATA = Path(__file__).parent / "dictionary"

DEFAULT_DICTIONARY = Dictionary.from_directory(DICTIONARY_DATA)
DEFAULT_WORD_ORDER = ("numbers", "adjectives", "nouns", "verbs", "adverbs")


class HRIDGenerator:
    """A generator class for human readable ids (hrid).

    Parameters
    ----------
    dictionary
        A dictionary of WordSets that underpin the generator.
    seed
        The seed to provide to the internal random number generator.
    word_order
        A sequence of word types to use for phrase generation. Must be
        keys of ``dictionary`` or "numbers".
    word_separator
        The character to use to separate the words in the phrase. By
        default "-".

    """

    def __init__(
        self,
        dictionary: Dictionary = DEFAULT_DICTIONARY,
        seed: int | None = None,
        *,
        word_order: Sequence[str] = DEFAULT_WORD_ORDER,
        word_separator: str = "-",
    ):
        self._dictionary: WordSet = dictionary
        self.generator: random.Random = random.Random(seed)
        filtered_word_order = [k for k in word_order if k in self._dictionary or k == "numbers"]
        self.word_order: Sequence[str] = filtered_word_order
        self.separator: str = word_separator

        self.min_int: int = 2
        self.max_int: int = 512

    def hrid(self) -> str:
        """Generate a pseudorandom id phrase.

        Returns
        -------
        str
            The generated phrase with each word given by the initial word order.

        """
        phrase_list = []
        for word_type in self.word_order:
            if word_type == "numbers":
                phrase_list.append(str(self.generator.randint(self.min_int, self.max_int)))
            else:
                word_list = self._dictionary[word_type]
                phrase_list.append(self.generator.choice(word_list.words))
        return self.separator.join(phrase_list)

    def reseed(self, seed: int | None = None):
        """Re-initialize the random number generator.

        Parameters
        ----------
        seed
            The seed to provide to the internal random number generator.

        """
        self.generator = random.Random(seed)


def hrid(seed: int | None = None):
    """Generate a pseudorandom hrid.

    This uses the default generator.

    Parameters
    ----------
    seed
        The seed to provide to the internal random number generator.

    Returns
    -------
    str
        The generated phrase with each word given by the initial word order.

    See Also
    --------
    HRIDGenerator

    """
    generator = HRIDGenerator(seed=seed)
    return generator.hrid()
