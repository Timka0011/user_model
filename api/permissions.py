from rest_framework import permissions


class StaffUserPermessions(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        print(user.get_all_permissions())
        if user.is_staff:
            if user.has_perm("article.view_article"):
                return True
            return False
        return False
    
    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        return False
        
