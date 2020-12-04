# Stock Price Monitor

Monitors stock prices and sends a buy/sell warning when its price crosses a configurable lower/upper threshold.

⚠️ *Warning*: this is a portfolio project and therefore has limited features.

## Goal

This project's goal is for me to learn and later showcase my skills in Python & Django.

## Features

Automatically fetches stock prices from a public source at a customizable rate - #todo what range?

Web UI to browse price history, choose assets to track and setup lower/upper price thresholdd.

Sends an email every time a tracked stock's price crosses the lower (buy) or upper (sell) threshold.

## Stack

- Python 3.7
- Django 3.1
- SSR web app - initally, then SPA + DRF web service

## Architecture

Price service - fetches stock prices every X rate

Alert service - checks current prices and sends buy/sell alerts

#todo and the web app?

## Creative Process

Expand these topics:

- 1st watched [this](https://www.youtube.com/playlist?list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO) Django crash course and read through MDN's Django [guides](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)
- Then considered SSR web app w/ Django or SPA + web service w/ Django REST Framework - pros and cons
- Decided for web app w/ Django for MVP and then move to SPA + web service to showcase skills
- Data entry (price fetch) most critical component at this point - find API else web scraper
- Also considering a time series DB for the stock prices - classic application of TSDBs 

## Roadmap

- Add other stock exchanges (e.g. NASDAQ, JPX etc.) 
- Send push notifications

## Notes

- It'd be really cool if this was a [12-factor app](https://12factor.net/)
- The most critical points (so far) is finding a stock prices public API
- It clearly involves running periodic jobs - will it require CRON? Hope not :D

To do:

- Creative process
- Changelog
