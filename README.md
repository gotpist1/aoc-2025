# Advent of Code 2025

Python solutions for [Advent of Code 2025](https://adventofcode.com/2025)

## Setup

Install dependencies:
```bash
pipenv install
```

## Running Solutions

To run a day's solution:
```bash
cd day1
pipenv run python day1.py
```

Or with example input:
```bash
cd day1
pipenv run python day1.py example.txt
```

## Creating New Days

Use the template generator:
```bash
pipenv run python create_day.py <day_number>
```

This creates a new folder with:
- `day<N>.py` - Solution template
- `input.txt` - Your puzzle input
- `example.txt` - Example from problem description

## Structure

Each day has its own folder:
```
day1/
  day1.py       # Solution code
  input.txt     # Puzzle input
  example.txt   # Example input for testing
```

## Tips

- Always test with the example input first
- Use `example.txt` to verify your solution logic
- Paste your actual puzzle input into `input.txt`
- Common utilities you might need: itertools, collections, re, numpy

