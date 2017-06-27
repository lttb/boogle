from cfg import cfg
from ._common import config, getAnswer
from .._utils import Req


req = Req({
    'url': 'https://www.googleapis.com/customsearch/v1element',
    'params': {
        ** dict(cfg.items('google')),
        ** dict(cfg.items('google.cse'))
    }
})


def ask(q):
    res = req(q)

    if 'results' not in res:
        return config['fallbackMessage']

    return getAnswer(res['results'], 'contentNoFormatting')
