"""Tests for the HRIDGenerator class and the hrid utility function."""

import pytest

from hrid import HRIDGenerator, hrid


@pytest.fixture
def sample_generator() -> HRIDGenerator:
    """Generate an example HRIDGenerator."""
    return HRIDGenerator(seed=42)


def test_generation(sample_generator: HRIDGenerator):
    """Test that generated words have the expected structure."""
    test_word = sample_generator.hrid()
    used_words = test_word.split(sample_generator.separator)
    assert len(used_words) == 5
    assert sample_generator.min_int < int(used_words[0]) < sample_generator.max_int
    for word_type, word in zip(sample_generator.word_order[1:], used_words[1:]):
        assert word in sample_generator._dictionary[word_type].words


def test_reproducibility(sample_generator):
    """Test the reproducibility of a generator and the hrid function."""
    assert sample_generator.hrid() == HRIDGenerator(seed=42).hrid()
    assert HRIDGenerator(seed=42).hrid() == hrid(seed=42)
