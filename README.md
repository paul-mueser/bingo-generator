# Bingo generator

This is a simple bingo card generator to generate bingo games for my [bingo website](https://github.com/paul-mueser/bingo-homepage).

## Usage

To generate a bingo card, run the program with an input file containing the bingo events, a number of players and optionally specify the starting index for numbering the events.

```
python bingo_generator.py <input.txt> <number_of_players> <starting_index>
```

- `<input.txt>`: A text file like specified in the Input file format section.
- `<number_of_players>`: The number of players for whom bingo cards will be generated.
- `<starting_index>`: An optional integer to start numbering the events from (default is 1).

## Input file format

The input file should always have a line containing the category number (1-5) and the number of events to choose from this category, then a line containing `---` before the list of events and a count, how often the event has to happen till finished, for that category followed by another `---`. For an 5 * 5 bingo card, the numbers of items per category should sum up to 25. An example can be found in `input.txt.example`.
