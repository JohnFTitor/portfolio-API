from project.models import Tag

def serialize_tag(tag: Tag):
  
  return {
    'id': str(tag.id),
    'name': tag.name,
  }
