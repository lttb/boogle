import random
import re

from .._utils import compose

config = {
    'fallbackMessage': 'Я не в курсе :('
}

# we need to remove users' names and other stuff
clearRe = re.compile(r'(\w+:)|Рейтинг@Mail.ru.*')
whitespaceRe = re.compile(r'\s+')

# clear unrelative results
blankRe = re.compile(r'задал вопрос в категории')


processAnswer = compose(
    lambda x: x.strip(),
    lambda x: re.sub(whitespaceRe, ' ', x),
    lambda x: re.sub(clearRe, '', x)
)


def getAnswer(items, key): return compose(
    processAnswer,
    random.choice,
    lambda x: [elem[key] for elem in x if not re.search(blankRe, elem[key])]
)(items)
