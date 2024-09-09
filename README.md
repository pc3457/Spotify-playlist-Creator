# Spotify Playlist Generator from Billboard Top 100

This Python project allows users to generate a Spotify playlist based on the Billboard Top 100 songs for a specific date. The program scrapes the Billboard Top 100 chart for a given date and adds the songs found to a private Spotify playlist.

## Features

- **Web scraping:** Scrapes Billboard's Hot 100 chart for a user-specified date using `BeautifulSoup`.
- **Spotify integration:** Creates a new Spotify playlist with the top 100 songs from that date.
- **Track matching:** Searches for songs on Spotify based on the scraped data.

## Requirements

To run this project, you will need the following dependencies:

- **Python 3.x**
- **requests** for making HTTP requests to the Billboard website
- **BeautifulSoup** from `bs4` for web scraping
- **spotipy** for interacting with the Spotify API

You can install these dependencies using the following command:

```bash
pip install requests beautifulsoup4 spotipy
