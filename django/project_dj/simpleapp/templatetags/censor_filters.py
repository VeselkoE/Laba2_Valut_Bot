from django import template
import re

register = template.Library()

bad_words = ['редиска', 'дурак', 'злодей']


def censor_word(word):
    if len(word) <= 2:
        return word
    return word[0] + '*' * (len(word) - 2) + word[-1]


@register.filter()
def censor(value):
    def replace(match):
        word = match.group()
        lower_word = word.lower()
        if lower_word in bad_words:
            return censor_word(word)
        return word

    pattern = re.compile(r'\b\w+\b', re.UNICODE)
    return pattern.sub(replace, value)
