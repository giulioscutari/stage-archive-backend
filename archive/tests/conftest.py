import pytest
from model_bakery import baker


@pytest.fixture()
def one_author():

    author = baker.make("discord_messages.Author", name="Olly", discriminator="2069")
    return author
