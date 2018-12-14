from django.contrib import admin
from .models import *
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class FilmsAdmin(admin.ModelAdmin):
    pass

class InfoAdmin(admin.ModelAdmin):
    pass

class ReplyAdmin(admin.ModelAdmin):
    pass

admin.site.register(User,UserAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Films,FilmsAdmin)
admin.site.register(Info,InfoAdmin)
admin.site.register(Reply,ReplyAdmin)
