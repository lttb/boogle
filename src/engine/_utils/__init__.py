import functools
import urllib.request
import json


def compose(*funcs):
    return lambda x: functools.reduce(lambda v, f: f(v), reversed(funcs), x)


def Req(config):
    def req(q):
        params = urllib.parse.urlencode({
            **config['params'],
            'q': q
        })

        req = urllib.request.Request(
            url=config['url'] + '?%s' % params,
        )

        res = urllib.request.urlopen(req)

        return json.loads(res.read().decode('utf8'))

    return req
