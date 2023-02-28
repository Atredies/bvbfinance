# Download market data from BVB (Stock Market in Romania)

<table border=1 cellpadding=10><tr><td>

#### \*\*\* IMPORTANT LEGAL DISCLAIMER \*\*\*

---

bvbfinance is **not** affiliated, endorsed, or vetted by BVB. It's
an open-source tool that uses BVBs publicly available website, and is
intended for research and educational purposes.

**You should refer to BVB's terms of use**
([here](https://bvb.ro/Regulations/LegalFramework/BvbRegulations#)
---

## Quick Start

### The Ticker module

The `Ticker` module, which allows you to access ticker data in a more Pythonic way:

```python
import bvbfinance as bvb

tlv = bvb.Ticker("TLV")

# get stock info
tlv.info

# get historical market data
hist = tlv.history(period="max")

# show actions (dividends, splits)
tlv.actions

# show dividends
tlv.dividends

# show splits
tlv.splits

# show share count
tlv.shares

# show income statement
tlv.income_stmt
tlv.quarterly_income_stmt

# show balance sheet
tlv.balance_sheet
tlv.quarterly_balance_sheet

# show cash flow statement
tlv.cashflow
tlv.quarterly_cashflow

# show major holders
tlv.major_holders

# show institutional holders
tlv.institutional_holders

# show mutualfund holders
tlv.mutualfund_holders

# show earnings
tlv.earnings
tlv.quarterly_earnings

# show sustainability
tlv.sustainability

# show analysts recommendations
tlv.recommendations
tlv.recommendations_summary
# show analysts other work
tlv.analyst_price_target
mfst.revenue_forecasts
mfst.earnings_forecasts
mfst.earnings_trend

# show next event (earnings, etc)
tlv.calendar

# show all earnings dates
tlv.earnings_dates

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
tlv.isin

# show options expirations
tlv.options

# show news
tlv.news

# get option chain for specific expiration
opt = tlv.option_chain('YYYY-MM-DD')
# data available via: opt.calls, opt.puts
```