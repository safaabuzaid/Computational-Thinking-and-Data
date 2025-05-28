# Hangman Game 🔤

This mini-project implements a variation of the classic word game Hangman, where the computer selects a word at random and the user attempts to guess it letter by letter within a limited number of attempts.

## Project Overview

- The program loads a large word list from a file.
- A secret word is chosen at random.
- The player guesses one letter per round.
- After each guess, the player is told whether the letter exists in the word, and is shown:
  - Current guessed state of the word.
  - Available letters not yet guessed.
  - Remaining number of guesses.
- The game ends either when the user successfully guesses the full word or uses all allowed guesses.

## Skills Practiced

- Working with files (words.txt)
- Functions and helper function design
- Loops and conditionals
- User input validation
- String manipulation
- Game state tracking

## 📂 Files

- ps3_hangman.py: Main implementation file.
- hangmanTests.py: unit test file.
- words.txt: Word list used to randomly choose the target word.
