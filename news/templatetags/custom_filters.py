from django import template


register = template.Library()

bad_words = [
    'слово'
]


@register.filter()
def censor(value):
    for words in bad_words:
        value = value.replace(words, ('*' * len(words)))
    return value
