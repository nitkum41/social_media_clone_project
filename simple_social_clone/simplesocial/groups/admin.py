from django.contrib import admin
from . import models
# Register your models here.


#to view the admin page we use this inline function
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
