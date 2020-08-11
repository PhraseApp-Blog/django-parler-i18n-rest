from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from parler.models import TranslatableModel, TranslatedFields

class Post(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_("Title"), max_length=200, unique=True),
        content = models.TextField(_("Content"), blank=True)
    )
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title
