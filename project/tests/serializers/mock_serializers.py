from project.models import Tag, Project


def serialize_tag(tag: Tag):

    return {
        'id': str(tag.id),
        'name': tag.name,
    }


def serialize_project(project: Project):
    return {
        'id': project.id.hex,
        'name': project.name,
        'description': project.description,
        'live_url': project.live_url,
        'source_url': project.source_url,
        'demo_url': project.demo_url,
        'tags': [
            serialize_tag(tag)
            for tag in list(project.tags.all())
        ]
    }
