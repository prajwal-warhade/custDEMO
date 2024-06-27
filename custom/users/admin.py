from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'name', 'email', 'address', 'mobile_no')
    readonly_fields = ('unique_identity_no',)

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return self.readonly_fields + ('unique_identity_no',)
        return self.readonly_fields

admin.site.register(UserProfile, UserProfileAdmin)
