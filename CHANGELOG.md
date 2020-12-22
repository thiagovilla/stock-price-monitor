# Changelog

## Version `0.3.2

Updated the `clock` process to read the `update_prices` job interval from `UPDATE_PRICES_INTERVAL` or default to `P0DT1H` (one hour). This is an improvement from the previous fixed interval; the requirement, however, is to read it from a user-defined value - #todo.

## Version `0.3.1`

Refactored out the `lower_limit` and `upper_limit` fields from the old `Asset` model into a new `TrackedAsset` model. `Asset` and `TrackedAsset` have a 1:N relationship. Also added a new `last_modified` field to the _new_ `Asset` model.

Updated the `sendalerts` custom command accordingly. Now each asset is updated only once, solving an issue from [`0.2.0`](#version-020).

## Version `0.3.0`

Created a [Redis Queue](https://python-rq.org/) worker to process the `updateprices` and `sendalerts` custom commands as background jobs - partially implemented in [`0.3.2`](#version-032).

Created an `update_prices` job that loads Django's ORM from an external script with [`django.setup()`](https://docs.djangoproject.com/en/3.1/ref/applications/#django.setup) - inspired by [this post](https://stackoverflow.com/a/58780891/7441775) on Stack Overflow.

~Created a _temporary_ custom command `updateprices2` to enqueue the `update_prices` job, which will run in a separate worker process~ removed in [`0.3.2`](#version-032).

## Version `0.2.1`

Installed dependencies and set up settings to use Postgres as the default database and serve static files directly from Gunicorn in production.

This was needed to test `updateprices` and `sendalerts` on the Heroku deploy. Note: I'm violating [factor X - dev/prod parity](https://12factor.net/dev-prod-parity) by using SQLite in development and Postgres in production - will fix that soon with Docker #todo.

## Version `0.2.0`

Added Django custom commands `updateprices` and `sendalerts`. Added `current_price` attribute to Asset model.

The `updateprices` command calls the stock prices API and updates the current price for each asset. ~Duplicate assets are updated twice - group or unlink "asset" and "tracked asset" models (1:N relationship)~ fixed/implemented in [`0.3.1`](#version-031).

The `sendalerts` command iterate through each tracked asset and either skips it if its price is within the lower (buy) and upper (sell) limits or sends a buy/sell email. The current console email backend is meant for development only - load config from env var #todo. Also, it is necessary to link the tracked asset and user models in order to get their email address #todo.

## Version `0.1.1`

Added basic error handling to `/assets/<symbol>`: request error (not 200 OK), invalid symbol, and symbol not found. Also ran `autopep8`.

## Version `0.1.0`

`/assets/<symbol>` returns asset `<symbol>`'s (e.g. PETR3) current price - no template yet, just testing the API.

It calls HG Brasil Finance API's [stock prices endpoint](https://hgbrasil.com/apis/cotacao-acao/b3-brasil-bolsa-balcao-b3sa3). Its [free plan](https://hgbrasil.com/apis/planos) is enough for development (15-60 min delay from live market data, max. 400 requests/day). Using `requests` library as the HTTP client - no timeout or throttling yet #todo.

The API key is stored in an environment variable as per the 12-factor app methodology's [factor III - config](https://12factor.net/config). I'm using different keys for development and the deploy on Heroku.

Only the "happy path" is implemented so far - no request or response error treament yet - implemented in [`0.1.1`](#version-011); the API has no timeout or throttling yet either #todo. No tests yet #todo.

## Before version `0.0.1`

#todo
