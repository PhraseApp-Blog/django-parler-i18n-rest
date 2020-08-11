from django.contrib import admin
from parler.admin import TranslatableAdmin
from blog.models import Post

class PostAdmin(TranslatableAdmin):
    list_display = ('title', 'content')
    fieldsets = (
        (None, {
            'fields': ('title', 'content'),
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.author_id = request.user.id
        super().save_model(request, obj, form, change)

admin.site.register(Post, PostAdmin)
# Register your models here.
