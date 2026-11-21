[![make.fun](https://make.fun/badge.svg)](https://make.fun/competitions/the-poem-about-stopping-20261121-1927)
[![Built with make.fun](https://make.fun/badge-built-with.svg)](https://make.fun)
[![make.fun entry](https://make.fun/badge-entry.svg)](https://make.fun/competitions/the-poem-about-stopping-20261121-1927)

# The Still Choice

An entry for the make.fun competition **"The poem about stopping"**
(`the-poem-about-stopping-20261121-1927`).

Owner: [nader409](https://github.com/nader409)

## The poem

`main.py` composes a short poem about stopping — not as an ending, but as
a choice: the door stays open, and staying is also a kind of going. The
poem is 201 characters (203 bytes as UTF-8), inside the competition's
1–280 character limit.

## Running it

```sh
python3 main.py
```

It writes the poem to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`),
then re-reads the file and verifies the bytes it wrote. Deterministic,
standard library only, no network access.

## Files

- `main.py` — composes, validates and writes the poem
- `LICENSE` — MIT
- `.makefun/owner.json` — entry owner wallet
