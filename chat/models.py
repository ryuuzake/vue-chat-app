from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Chat(models.Model):

    users = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=_("User"))

    class Meta:
        verbose_name = _("chat")
        verbose_name_plural = _("chats")

    def __str__(self):
        return f"Chat : {self.pk}"

    def get_absolute_url(self):
        return reverse("chat_detail", kwargs={"pk": self.pk})


class Message(models.Model):

    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("To User"), on_delete=models.CASCADE, related_name="+")
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("From User"), on_delete=models.CASCADE, related_name="+")
    status = models.BooleanField(_("Status"), default=False)
    inclusion_date = models.DateTimeField(_("Inclusion Date"), auto_now_add=True)
    message = models.TextField(_("Message"))
    chat = models.ForeignKey("chat.Chat", verbose_name=_("Chat"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("message")
        verbose_name_plural = _("messages")

    def __str__(self):
        return f"Message {self.pk} from Chat {self.chat.pk}"

    def get_absolute_url(self):
        return reverse("message_detail", kwargs={"pk": self.pk})
