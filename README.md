# Stock Price Monitor

Monitors stock prices and sends a buy/sell warning when its price crosses a configurable lower/upper threshold.

⚠️ *Warning*: this is a portfolio project and therefore has limited features.

# Goal

This project's goal is for me to learn and later showcase my skills in Python & Django.

# Features

Automatically fetches stock prices from a public source at a customizable rate - #todo what range?

Web UI to browse price history, choose assets to track and setup lower/upper price thresholdd.

Sends an email every time a tracked stock's price crosses the lower (buy) or upper (sell) threshold.

# Stack

- Python 3.7
- Django 3.1
- <abbr title="Server-Side Rendering">SSR</abbr> web app - at least initially?

# Architecture

Price service - fetches stock prices every X rate

Alert service - checks current prices and sends buy/sell alerts

#todo and the web app?

# Roadmap

- Add other stock exchanges (e.g. NASDAQ, JPX etc.) 
- Send push notifications

To do:

- Creative process
- Changelog
