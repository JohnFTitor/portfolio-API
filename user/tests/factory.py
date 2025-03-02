from user import models


def user(
    username='test',
    email='test@email.com',
    password='password',
    **kwargs,
):
    save = kwargs.pop('save', False)

    user = models.User(
        username=username,
        email=email,
        **kwargs,
    )

    user.set_password(password)

    if save:
        user.save()

    return user
