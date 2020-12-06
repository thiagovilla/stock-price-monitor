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

- Python 3.8.2
- Django 3.1
- SSR web app - initally, then SPA + DRF web service

## Architecture

Price service - fetches stock prices every X rate

Alert service - checks current prices and sends buy/sell alerts

#todo and the web app?

## Roadmap

- Add other stock exchanges (e.g. NASDAQ, JPX etc.) 
- Send push notifications
- SPA/DRF/PWA?

## Creative Process

Legend: ⤨ denotes a choice.

### Version `0.0.0`

I first watched [this crash course](https://www.youtube.com/playlist?list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO) on YouTube and read [this guide](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django) on MDN to get a hang of Django. I needed to learn how to code in Python/Django what I already did in Node/Express: routes, models, views, controllers, access control etc. Additionally, I also wanted to know how to schedule jobs and send email for the price monitor and buy/sell alert services respectively.

Next I considered whether to develop the app as a traditional server-side rendered (SSR) web app that serves HTML (built in Django) or a modern [JAM stack](https://jamstack.org) single-page application (SPA) coupled with a web service that serves *data* (built in Django REST Framework). While the latter [scales better](https://jamstack.org/why-jamstack), the former is **easier to iterate** ⤨. (I did add the SPA/DRF version to the roadmap, though.) Either way, I chose to follow the [twelve-factor](https://12factor.net) methodology.

#todo expand these topics:

- Data entry (price fetch) most critical component at this point - find API else web scraper
- Also considering a time series DB for the stock prices - classic application of TSDBs 

### Version `0.1.0`

## Notes

- The most critical points (so far) is finding a stock prices public API
- It clearly involves running periodic jobs - will it require CRON? Hope not :D
- "Creative process" section likely to grow too large, consider moving to own file

To do:

- Changelog
