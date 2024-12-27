"""Tests for the Dictionary class."""

import pytest

from hrid import Dictionary, WordSet


@pytest.fixture
def example_dictionary() -> Dictionary:
    """An example dictionary for testing."""
    return Dictionary({"adverbs": WordSet(["quietly", "loudly"])})


def test_dictionary_methods(example_dictionary: Dictionary):
    """Test the standard dictionary methods for a Dictionary."""
    assert set(example_dictionary.keys()) == {
        "adverbs",
    }
    assert tuple(example_dictionary["adverbs"].words) == (
        "loudly",
        "quietly",
    )

    # Add an item
    example_dictionary["nouns"] = WordSet(["cats", "dogs"])
    assert set(example_dictionary) == {"adverbs", "nouns"}

    # Remove an item
    del example_dictionary["adverbs"]
    assert set(example_dictionary) == {"nouns"}


def test_directory_loading(datadir):
    """Test loading a Dictionary from a file."""
    loaded_dictionary = Dictionary.from_directory(datadir)
    assert set(loaded_dictionary) == {"nouns", "verbs"}
    assert loaded_dictionary["nouns"].words == (
        "cats",
        "dogs",
    )
    assert loaded_dictionary["verbs"].words == (
        "whisper",
        "yell",
    )


def test_bad_dictionaries(example_dictionary):
    """Test that expected errors are raised for a Dictionary."""
    with pytest.raises(TypeError):
        example_dictionary["nouns"] = ["cats", "dogs"]

    with pytest.raises(ValueError):
        example_dictionary["adverbs"] = example_dictionary["adverbs"]

    with pytest.raises(KeyError):
        del example_dictionary["verbs"]
