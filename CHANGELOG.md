# Changelog

## Before version `0.0.1`

#todo

## Version `0.1.1`

Added basic error handling to `/assets/<symbol>`: request error (not 200 OK), invalid symbol and symbol not found. Also ran `autopep8`.

## Version `0.1.0`

`/assets/<symbol>` returns asset `<symbol>`'s (e.g. PETR3) current price - no template yet, just testing the API.

It calls HG Brasil Finance API's [stock prices endpoint](https://hgbrasil.com/apis/cotacao-acao/b3-brasil-bolsa-balcao-b3sa3). Its [free plan](https://hgbrasil.com/apis/planos) is enough for development (15-60 min delay from live market data, max. 400 requests/day). Using `requests` library as the HTTP client - no timeout or throttling yet #todo.

The API key is stored in an environment variable as per the 12-factor app methodology's [factor III - config](https://12factor.net/config). I'm using different keys for development and the deploy on Heroku.

Only the "happy path" is implemented so far - no request or response error treament yet; the API has no timeout or throttling yet either #todo. No tests yet.
