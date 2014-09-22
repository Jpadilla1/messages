from django.conf.urls import patterns

from rest_framework import routers

from .views import MessageViewSet, WebhookReceiverView

router = routers.DefaultRouter()
router.register(r'messages', MessageViewSet)

urlpatterns = router.urls

urlpatterns += patterns(
    '',
    (r'^webhook/$', WebhookReceiverView.as_view())
)
