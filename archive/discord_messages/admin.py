from django.contrib import admin
from .models import Guild, Category, Channel, Author, Message
# Register your models here.


@admin.register(Guild)
class GuildAdmin(admin.ModelAdmin):
    
    list_display = (
        "discord_id",
        "name",        
    )
    search_fields = ("name",)




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    
    list_display = (
        "server_id",
        "name",        
    )
    search_fields = ("name",)


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    
    list_display = (
        "discord_id",
        "name",
        "guild",
    )
    list_filter = (
        "guild",
    )
    search_fields = (
        "discord_id", "name"
    )

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = (
        "unique_name",
        "discord_id",
    )
    search_fields = (
        "discord_id", "unique_name"
    )

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass
    # list_display = (
    #     "channel", "timestamp_sent", "timestamp_edited", "author"
    # )