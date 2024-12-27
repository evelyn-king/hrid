"""Tests for the WordSet class."""

from pathlib import Path

import pytest

from hrid.sets import WordSet


@pytest.fixture
def sample_word_set():
    """An example of a WordSet."""
    word_list = {"animal", "vegetable", "mineral"}
    return WordSet(word_list)


def test_word_set_basics(sample_word_set: WordSet):
    """Test simplest version of a wordset."""
    # Ensure sorting on init
    assert sample_word_set.words == ("animal", "mineral", "vegetable")


def test_unique_words(sample_word_set: WordSet):
    """Test that only unique words are in a WordSet."""
    list_with_dupes = ["animal", "animal", "vegetable", "mineral"]
    new_word_set = WordSet(list_with_dupes)
    assert sample_word_set.words == new_word_set.words


def test_yaml_loader(datadir: Path, sample_word_set: WordSet):
    """Test loading from a yaml file."""
    test_file = datadir / "sample.yaml"
    loaded_word_set = WordSet.from_yaml(test_file)
    assert sample_word_set.words == loaded_word_set.words


def test_loading_error(datadir: Path):
    """Ensure a value error is raised for an unsupported extension."""
    with pytest.raises(ValueError, match=".csv"):
        _ = WordSet.from_file(datadir / "bad_data.csv")
