from django.db import models

# Create your models here.


class Guild(models.Model):
    discord_id = models.CharField("discord id", max_length=18, unique=True)
    name = models.CharField("server name", max_length=255)
    icon_url = models.CharField("icon url", max_length=255)


class Category(models.Model):
    guild = models.ForeignKey("Guild",on_delete=models.DO_NOTHING, related_name="categories", to_field="discord_id")
    discord_id = models.CharField(max_length=18, unique=True)
    name = models.CharField("category name", max_length=255)


class Channel(models.Model):
    discord_id = models.CharField("discord id", max_length=18, unique=True)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True,to_field="discord_id")
    name = models.CharField("channel name", max_length=100)
    topic = models.TextField("channel topic")
    guild = models.ForeignKey("Guild", on_delete=models.SET_NULL, null=True)


class Author(models.Model):
    discord_id = models.CharField("discord id", max_length=18, unique=True)
    name = models.CharField("author name", max_length=255)
    discriminator = models.CharField("discriminator", max_length=4)
    avatar_url = models.CharField("avatar url", max_length=255)
    color = models.CharField("name color", max_length=7)
    is_bot = models.BooleanField("is a bot", default=False)

    @property
    def unique_name(self):
        return f"{self.name}#{self.discriminator}"


class Message(models.Model):
    discord_id = models.CharField("discord id", max_length=255, unique=True)
    timestamp_sent = models.DateTimeField("timestamp sent")
    timestamp_edited = models.DateTimeField(
        "timestamp edited", null=True, default=None
    )
    content = models.TextField("content")
    channel = models.ForeignKey("Channel", on_delete=models.PROTECT, to_field="discord_id")
    author = models.ForeignKey("Author", on_delete=models.PROTECT,to_field="discord_id")
