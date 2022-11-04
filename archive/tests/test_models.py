import pytest


def test_unique_name(db, one_author):
    assert one_author.unique_name == "Olly#2069"
