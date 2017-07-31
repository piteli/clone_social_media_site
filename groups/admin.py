from django.contrib import admin
from. import models

admin.site.register(models.Group)


class GroupMemberInline(admin.TabularInLine):
    model = models.GroupMember
