from django.contrib.auth.models import Group, Permission

from laboratory.models import OrganizationUserManagement, Laboratory

laboratory_permissions_remove = []
laboratory_permissions_add = []

def load_permissions_list():

    global laboratory_permissions_add
    global laboratory_permissions_remove
    laboratory_codes = ["change_laboratory", "view_laboratory", "delete_laboratory"]

    for code in laboratory_codes:
        permission = Permission.objects.filter(codename=code)
        if permission:
            laboratory_permissions_remove.append(permission.first())
            if not code == "view_laboratory":
                laboratory_permissions_add.append(permission.first())


def validate_organization_laboratory(organization_structure_list):
    laboratories_list = Laboratory.objects.filter(organization__pk__in=organization_structure_list)

    if laboratories_list:
        return True
    return False

def manage_laboratory_permissions(user, organization_user_management_list):

    global laboratory_permissions_add
    global laboratory_permissions_remove
    view_laboratory_per = Permission.objects.filter(codename="view_laboratory")
    administrator_group = Group.objects.filter(name="Laboratory Administrator")
    groups = organization_user_management_list.values_list("group", flat=True)
    add_laboratory_per = Permission.objects.filter(codename="add_laboratory")
    organization_structure_list = OrganizationUserManagement.objects.filter(users=user).values_list("organization", flat=True)

    if laboratory_permissions_remove:
        user.user_permissions.remove(*laboratory_permissions_remove)

    if validate_organization_laboratory(organization_structure_list):
        if view_laboratory_per:
            user.user_permissions.add(view_laboratory_per.first())

        if administrator_group:
            if administrator_group.first().pk in groups:
                if laboratory_permissions_add:
                    user.user_permissions.add(*laboratory_permissions_add)

    if administrator_group:
        if administrator_group.first().pk in groups:
            if add_laboratory_per:
                user.user_permissions.add(add_laboratory_per.first())


class SetUserPermissions:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        user = request.user

        if user.is_authenticated:
            load_permissions_list()
            user.user_permissions.remove(*user.user_permissions.all())
            organization_user_management_list = OrganizationUserManagement.objects.filter(users=user)

            if organization_user_management_list:
                for organization in organization_user_management_list:
                    user.user_permissions.add(*organization.group.permissions.all())

            manage_laboratory_permissions(user, organization_user_management_list)


        response = self.get_response(request)

        return response