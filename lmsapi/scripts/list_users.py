from api_user.models import LmsUsers


def run():
    users = LmsUsers.objects.all()
    for user in users:
        print(user.name)
