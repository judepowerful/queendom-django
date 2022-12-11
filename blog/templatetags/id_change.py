from django import template

register = template.Library()

@register.filter
def to_splider_id(value):
    return "splider" + value

@register.filter
def users_liked(post, email):
    return post.filter(email=email).exists()