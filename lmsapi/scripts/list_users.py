from api_user.models import LmsUsers


def run():
    users = LmsUsers.objects.filter(deleted=0)
    for user in users:
        print(user.name)
