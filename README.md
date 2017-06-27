# Boogle Bot

Boogle gives you an answer via Google search results.

## Dialog example

```
Artur: как дела?
Boogle: Как дела? Нормально. Кот спит без задних ног, я - жарю окорочка. живодер!!!
Artur: кто станет следующим президентом сша?
Boogle: Там только один вменяемый кандидат - МакКейн, он и будет президентом США. Мне тоже не нравиться, что он говорит про нас, ...
Artur: какой твой любимый цвет?
Boogle: Мой любимый цвет зеленый, я думаю это цвет жизни... Но еще мне
нравиться черный цвет, мне он идет!
```

## Installation

This bot was written with Python 3.

```sh
git clone https://github.com/lttb/boogle
```

## Usage

To run bot from CLI with default engine run this command:

```sh
make
```

### Options

You can pass supported engine via `e` arg:

```sh
make e={engine}
```

For example:
```sh
make e=google.cs
```

Supported engines:
  - google.cs (Google Custom Search)
  - google.cse (Google Custom Search Element)


### Config

You need to set up config file `.cfg` with API keys to use this bot in the root:

*.cfg*:
```ini
[google]
cx = {cx key for your Custom Search} # optional

[google.cs]
key = {CS API key} # required for 'google.cs' engine

[google.cse]
key = {CSE API key} # required for 'google.cse' engine
```

## License

MIT, Kenzhaev Artur
