from django.core.management import call_command
from discord_messages.models import Guild, Author, Category, Channel, Message
import datetime

def test_import_json(db):

    call_command("import_json", '/app/archive/tests/static_files/The_Jellyfish_Aquarium_-_Moderation_memorable-friend-quotes[991599401103536148].json')
    guild = Guild.objects.get(discord_id="963385109568946236")
    assert guild.name == "The Jellyfish Aquarium"
    assert guild.icon_url == "https://cdn.discordapp.com/icons/963385109568946236/b589570fac883133fe53b8b8e853ff0d.png"
    saturn = Author.objects.get(discord_id="760007440421879840")
    assert saturn.discord_id=="760007440421879840"
    assert saturn.name=="Saturn"
    assert saturn.discriminator=="7198"
    assert saturn.color=="#F5EEEE"
    assert saturn.is_bot==False
    assert saturn.avatar_url=="https://cdn.discordapp.com/avatars/760007440421879840/02e4722a6e5ed5e0744deef18669ba79.png?size=512"
    category = Category.objects.get(discord_id="963419294484537365")
    assert category.name == "Moderation 🏗📑"
    assert category.guild == guild
    channel = Channel.objects.get(discord_id="991599401103536148")
    assert channel.category == category
    assert channel.name == "memorable-friend-quotes"
    assert channel.topic == "Perfect for sharing quotes by people you know. For quotes from others please use the relevant topic channel instead"
    assert channel.guild == guild
    message = Message.objects.get(discord_id="1003168985145167887")
    assert message.timestamp_edited == None
    assert message.timestamp_sent == datetime.datetime(2022, 7, 31, 5, 15, 24, 37000, tzinfo=datetime.timezone.utc)
    assert message.content == "Cloudie — Today at 15:12\nI love soap, it's like, chemical warfare.\n*You will get no additional context, but it slew Dragoon so here it is.*"
    assert message.channel == channel
    assert message.author == Author.objects.get(discord_id="161808757330804736")
