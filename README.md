# Fake News Finder

![The Don](Borowitz-Trump.gif)

This Python-based application uses web scraping to extract the most recent headlines from 3 specific online news agencies: Forbes, Ars Technica and The Atlantic. The main focus of this project was on backend-functionality, thus, the GUI is extremely simple. It offers the latest details on the headline story, a brief excerpt from the story, as well as the date-time of publishing. Additionally, you can follow the links offered to be directed to the article webpage to view the full details of the article. Once the user has read the article, they are free to use the truth scale in order to rate the 'truthfulness' of the specific article. This rating is then saved in an SQLite Database.

## Table of Contents

[Features](#features)

[Requirements](#requirements)

[Installation](#installation)

## Features
- Retrieve and display the latest headline stories from Forbes, Ars Technica and The Atlantic
- View brief details of headline story, date-time of publishing and an excerpt from the article
- Redirects to the article source if desired
- Rate the truthfulness of each article on a 1-10 scale
- Truth rating is then saved into an SQLite Database

## Requirements
- Python 3.x
- tkinter library
- urllib library
- re library
- webbrowser library
- sqlite3 library

## Installation
Installation is extremely simple as the program mainly relies on a few Python libraries
1. Clone the repository:

```bash
  git clone https://github.com/theaustingelatt/first-year-projects.git
```
2. Navigate to the project directory:

```bash
cd first-year-projects
```
3. Install Required Libraries (or just rely on the imports in the code)
```bash
pip install tkinter urllib re webbrowser sqlite3
```
