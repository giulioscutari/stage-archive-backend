from django.core.management.base import BaseCommand
import json, bulk_sync
from discord_messages.models import Guild, Category, Channel, Author, Message
class Command(BaseCommand):

    help = "Import messages from a JSON file."

    def add_arguments(self, parser):
        parser.add_argument("filepath", type=str)

    def handle(self, *args, **options):
        data = json.load(open(options["filepath"],'r'))
        guild, _ = Guild.objects.get_or_create(
            discord_id=data["guild"]["id"],
            name=data["guild"]["name"],
            icon_url=data["guild"]["iconUrl"]
        )
        category = None
        channel_data = data["channel"]
        if "category" in channel_data.keys():
            category_data = data["channel"]
            category, _ = Category.objects.get_or_create(
                discord_id = category_data["categoryId"],
                name = category_data["category"],
                guild=guild, 
            )
        channel, _  = Channel.objects.get_or_create(
            discord_id=data["channel"]["id"],
            name=data["channel"]["name"],
            topic=data["channel"]["topic"],
            guild=guild,
            category=category if category else None
        )
        authors = [m["author"] for m in data["messages"]]
        authors = list({v["id"]:v for v in authors}.values())
        Author.objects.bulk_create(Author(
                    discord_id=a["id"],
                    name=a["name"],
                    discriminator=a["discriminator"],
                    avatar_url=a["avatarUrl"],
                    color=a["color"],
                    is_bot=a["isBot"],
                ) for a in authors)
        Message.objects.bulk_create(
            Message(
                discord_id=m["id"],
                channel=channel,
                timestamp_sent= m["timestamp"],
                timestamp_edited=m["timestampEdited"],
                content=m["content"],
                author_id=m["author"]["id"]
                ) for m in data["messages"]
            )