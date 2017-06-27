from IO import OUT, IN
from bot import Bot


config = {
    'name': 'Boogle',
    'exit': 'bye'
}


# perform message
def message(name, text=''):
    return '%(name)s: %(text)s' % locals()


def main():
    OUT.put('Hi! My name is %(name)s.' % config)
    OUT.put('U can try 2 talk w/ me & ask me anything u want\n')

    name = IN.put("What's yr name?\n")
    OUT.put('\nNice 2 meet u, %(name)s' % locals())
    OUT.put('Please type "bye" to finish our talk\n')

    bot = Bot(IN.args)

    while True:
        q = IN.put(message(name))

        if q == config['exit']:
            break

        OUT.put(message(config['name'], bot.answer(q)))

    OUT.put(message(config['name'], 'bye!'))


if __name__ == '__main__':
    main()
