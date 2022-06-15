from mocker_library.services import UserService

def test_get_all_users(mocker):
    users_expects = mocker.Mock()
    user_service_dao = mocker.Mock(
        get_all_users=mocker.Mock(return_value=users_expects)
    )
    service = UserService(user_service_dao)
    users = service.get_all_users()

    assert users_expects == users


def test_create_user(mocker):
    user_expect = mocker.Mock()
    user_service_dao = mocker.Mock(
        create=mocker.Mock(return_value=user_expect)
    )
    service = UserService(user_service_dao)
    user = service.create({})

    assert user_expect == user
