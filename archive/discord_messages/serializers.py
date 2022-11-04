from rest_framework.serializers import ModelSerializer
from discord_messages.models import Guild, Category, Channel, Author, Message

class GuildSerializer(ModelSerializer):
    class Meta:
        fields = (
            "discord_id",
            "icon_url",
            "name",
        )
        model = Guild


class CategorySerializer(ModelSerializer):
    class Meta:
        fields = ("server_id", "name")
        model = Category


class ChannelSerializer(ModelSerializer):
    class Meta:
        fields = (
            "category",
            "discord_id",
            "guild",
            "name",
            "topic",
        )
        model = Channel


class AuthorSerializer(ModelSerializer):
    class Meta:
        fields = (
            "discord_id",
            "name",
            "discriminator",
            "unique_name",
            "avatar_url",
            "color",
            "is_bot",
        )
        model = Author


class MessageSerializer(ModelSerializer):
    class Meta:

        fields = ("discord_id", "timestamp_sent", "timestamp_edited", "content")
        model = Message
