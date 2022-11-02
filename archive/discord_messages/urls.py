from rest_framework.routers import SimpleRouter

from .views import (
    MessageViewSet,
    AuthorViewSet,
    GuildViewSet,
    ChannelViewSet,
    CategoryViewSet,
)


router = SimpleRouter()

router.register("authors", AuthorViewSet)
router.register("categories", CategoryViewSet)
router.register("channels", ChannelViewSet)
router.register("guilds", GuildViewSet)
router.register("messages", MessageViewSet, basename="messages")

urlpatterns = router.urls