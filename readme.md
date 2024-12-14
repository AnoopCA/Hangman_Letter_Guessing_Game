# Hangman Game with FastText AI

## Description

This project implements an automated Hangman game, leveraging FastText for intelligent word guessing. The goal is to create an AI player capable of playing Hangman by predicting the most probable letters in a word based on patterns and similarity scores.

The AI enhances the gameplay experience by utilizing pre-trained word vectors and a probabilistic approach to guess letters in a masked word.

---

## Features

- **FastText Integration**: Uses pre-trained FastText word embeddings for letter prediction.
- **Automated Gameplay**: Simulates Hangman games with system-generated words and AI guesses.
- **Word Pattern Matching**: Identifies potential words from a dataset based on masked word patterns.
- **Performance Tracking**: Keeps track of correct guesses and tries used during the game.

---

## Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - `fasttext`: For word embeddings and similarity calculations.
  - `re`: For regular expressions in word pattern matching.
  - `random`: For word selection and randomness.
  - `string`: For handling characters.
  - `collections.Counter`: For frequency analysis of predicted letters.

---

## Data

- **Dataset**: A text file containing 250,000 English words is used as the source for game words.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AnoopCA/Hangman_Letter_Guessing_Game.git
   ```
