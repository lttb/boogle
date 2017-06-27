from cfg import cfg
from ._common import config, getAnswer
from .._utils import Req


req = Req({
    'url': 'https://www.googleapis.com/customsearch/v1',
    'params': {
        ** dict(cfg.items('google')),
        ** dict(cfg.items('google.cs'))
    }
})


def ask(q):
    res = req(q)

    if 'items' not in res:
        return config['fallbackMessage']

    return getAnswer(res['items'], 'snippet')
