from erp_villa_alemana_escolares_tecnologicos.apps.users.models import User


def test_user_get_absolute_url(user: User):
    assert user.get_absolute_url() == f"/users/{user.username}/"
