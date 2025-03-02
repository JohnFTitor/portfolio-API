from project import models


def tag(
    name='test',
    **kwargs,
):
    save = kwargs.pop('save', False)

    tag = models.Tag(
        name=name,
        **kwargs,
    )

    if save:
        tag.save()

    return tag


def project(
    name='Test',
    description='testing description',
    **kwargs,
):
    save = kwargs.pop('save', False)

    project = models.Project(
        name=name,
        description=description,
        **kwargs,
    )

    if save:
        project.save()

    return project
