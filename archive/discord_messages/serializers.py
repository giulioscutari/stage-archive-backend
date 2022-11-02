from rest_framework.serializers import ModelSerializer


class GuildSerializer(ModelSerializer):
    class Meta:
        fields = (
            "discord_id",
            "icon_url",
            "name",
        )


class CategorySerializer(ModelSerializer):
    class Meta:
        fields = ("server_id", "name")


class ChannelSerializer(ModelSerializer):
    class Meta:
        fields = (
            "category",
            "discord_id",
            "guild",
            "name",
            "topic",
        )


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


class MessageSerializer(ModelSerializer):
    class Meta:

        fields = ("discord_id", "timestamp_sent", "timestamp_edited", "content")
