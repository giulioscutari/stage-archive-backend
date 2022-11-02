from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.pagination import PageNumberPagination
from discord_messages.models import Message, Author, Guild, Category, Channel
from discord_messages.serializers import (
    MessageSerializer,
    AuthorSerializer,
    CategorySerializer,
    GuildSerializer,
    ChannelSerializer,
)

class PaginationSettings(PageNumberPagination):
    page_size = 200
    max_page_size = 200

class ChannelViewSet(ReadOnlyModelViewSet):

    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class MessageViewSet(ReadOnlyModelViewSet):

    serializer_class = MessageSerializer
    pagination_class = PaginationSettings

    def get_queryset(self):
        channel = self.request.query_params.get('channel')
        return Message.objects.filter(channel__pk=channel).order_by("timestamp_sent")


class AuthorViewSet(ReadOnlyModelViewSet):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CategoryViewSet(ReadOnlyModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GuildViewSet(ReadOnlyModelViewSet):

    queryset = Guild.objects.all()
    serializer_class = GuildSerializer
