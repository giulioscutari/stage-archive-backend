from email.policy import default
from enum import unique
from django.db import models

# Create your models here.


class Guild(models.Model):
    discord_id = models.CharField("discord id", max_length=18, unique=True)
    name = models.CharField("server name", max_length=100)
    icon_url = models.CharField("icon url", max_length=100)


class Category(models.Model):
    server_id = models.IntegerField("server id")
    name = models.CharField("category name", max_length=100)


class Channel(models.Model):
    discord_id = models.CharField("discord id", max_length=18, unique=True)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    name = models.CharField("channel name", max_length=100)
    topic = models.TextField("channel topic")
    guild = models.ForeignKey("Guild", on_delete=models.SET_NULL, null=True)


class Author(models.Model):
    discord_id = models.CharField("discord id", max_length=18, unique=True)
    name = models.CharField("author name", max_length=100)
    discriminator = models.CharField("discriminator", max_length=4)
    avatar_url = models.CharField("avatar url", max_length=100)
    color = models.CharField("name color", max_length=7)
    is_bot = models.BooleanField("is a bot", default=False)

    @property
    def unique_name(self):
        return f"{self.name}#{self.discriminator}"


class Message(models.Model):
    discord_id = models.CharField("discord id", max_length=18, unique=True)
    timestamp_sent = models.DateTimeField("timestamp sent")
    timestamp_edited = models.DateTimeField(
        "timestamp edited", blank=True, default=None
    )
    content = models.TextField("content")
    channel = models.ForeignKey('Channel',on_delete=models.PROTECT)
    author = models.ForeignKey("Author",on_delete=models.PROTECT)

