# Chapter 12: The Secondary Market

> **In one line:** Existing securities trade between investors through broker-dealers acting as agent or principal, on exchanges or OTC, under the 1934 Act — and the customer controls execution through the order type.

## The big ideas

1. **Capacity sets the pay** — agent earns a commission, principal a markup/markdown; never both on one trade.
2. **Customers trade at the dealer's worse side** — buy at the ask, sell at the bid; the spread is the dealer's profit.
3. **Where the security is listed vs. where it trades** — this defines the first, second, third and fourth markets.
4. **The 1934 Act governs trading after issuance** — it created the SEC and regulates firms, exchanges, insiders, reporting and margin.
5. **Order type trades certainty of fill for certainty of price** — market guarantees execution, limit guarantees price; stops only trigger.

## Must-know facts

### Capacity and markups
| | Agent (broker) | Principal (dealer) |
|---|---|---|
| Trades | For the customer | From own inventory |
| Paid by | Commission | Markup / markdown |
| Risk | None | Market risk |

- **Capacity** — always disclosed on the confirmation.
- **5% policy** — a guideline, not a cap; applies to secondary trades, not to new issues or mutual funds.
- **Proceeds transaction** — sell-and-buy with the proceeds counts as one trade for markup purposes.

### Quotes
- **Bid** — dealer buys; customer sells. **Ask (offer)** — dealer sells; customer buys.
- **Size** — round lots of 100: "6 × 3" = bid for 600, offer 300.
- **NBBO / inside market** — highest bid and lowest ask anywhere; basis of best execution.
- **Firm quote** — must be honored for displayed size; refusing = **backing away**. **Nominal** — informational only. **Workout** — approximate, for large/illiquid blocks.

### Markets and venues
| Market | What trades | Where |
|---|---|---|
| First | Listed | On the exchange |
| Second | Unlisted | OTC |
| Third | Listed | OTC by non-members |
| Fourth | Any | Institution-to-institution via ECNs |

- **NYSE** — auction market; **DMM** keeps a fair and orderly market, sets opening/closing prices, handles the book.
- **Nasdaq** — exchange with competing market makers (no DMM). Level 1 = inside quote; Level 2 = every market maker's quote; Level 3 = market makers enter quotes.
- **OTC Markets** — OTCQX (top), OTCQB (venture), Pink (anything). Corporate bond trades report to **TRACE**.
- **Cboe** — largest options exchange; **OCC** issues and guarantees all listed options, making them fungible.
- **SROs** — FINRA, exchanges, MSRB (MSRB writes rules but doesn't enforce).
- **Circuit breakers** (S&P 500 vs. prior close) — 7% and 13%: 15-minute halt, only before 3:25 pm; 20%: closed for the day. **LULD** — 5-minute pause for one stock.

### Securities Exchange Act of 1934
- **Created the SEC** — 5 commissioners, 5-year staggered terms, ≤ 3 from one party.
- **Registers** BDs, exchanges, SROs; requires 10-K, 10-Q, 8-K (4 business days).
- **Section 16** — insiders report trades and return short-swing (6-month) profits.
- **Schedule 13D** — > 5% with intent to influence control, within 5 business days (13G if passive).
- **Rule 10b-5** — anti-fraud for any security; basis of insider trading cases.
- **Fed sets margin** — Regulation T (50%).
- **Reg SHO** — mark long/short; locate before shorting; Rule 201 restricts shorts at or below the bid after a 10% drop (rest of day + next day).

### Orders
| Order | Placed | When triggered | Guarantees | Use |
|---|---|---|---|---|
| Market | — | Fills now | Execution | Immediacy |
| Buy limit | Below | — | Price | Buy cheaper |
| Sell limit | Above | — | Price | Take profit |
| Buy stop | Above | Market order | Neither | Protect short |
| Sell stop | Below | Market order | Neither | Protect long |
| Stop-limit | As stop | Limit order | Price, if filled | May never fill |

- **Stop trigger** — a trade at or through the stop price; executes at the next price.
- **Ex-date** — orders below the market are reduced by the dividend unless **DNR**.
- **Qualifiers** — **FOK**: all, immediately, or cancel; **IOC**: fill what you can now, cancel rest; **AON**: all, but can wait; **GTC**: open until filled/cancelled.
- **Not-held** — time and price discretion only; no written authority needed. **Discretionary** (security, action or amount) — written authorization.

### Order handling
- **Best execution (5310)** — most favorable terms reasonably available; payment for order flow (allowed if disclosed) never overrides it.
- **Front-running** — trading ahead of a customer's block order; prohibited.
- **Manning rule (5320)** — can't trade ahead of a customer limit order at that price or better.
- **Order tickets** — kept 3 years.

## Numbers to memorize

| What | Number |
|---|---|
| Markup guideline | 5% (not a cap) |
| Round lot | 100 shares |
| NYSE hours | 9:30 am – 4:00 pm ET |
| Circuit breaker Level 1 / 2 | 7% / 13% → 15-minute halt (before 3:25 pm) |
| Circuit breaker Level 3 | 20% → closed for the day |
| LULD pause | 5 minutes |
| SEC commissioners | 5; 5-year terms; ≤ 3 one party |
| Form 8-K | 4 business days |
| Schedule 13D | > 5%, within 5 business days |
| Short-swing profit window | 6 months |
| Reg T | 50% |
| Reg SHO Rule 201 | 10% drop from prior close |
| Order ticket retention | 3 years |

## Formulas

```
Spread = Ask − Bid
```
Quote 40.10–40.25 → spread $0.15; a market buy pays $40.25.

```
Order reduced on ex-date = Order price − Dividend (buy limits, sell stops only)
```
Sell stop at 45, $0.60 dividend → 44.40 (unless DNR).

## Exam traps

- **Trap:** A sell stop is placed above the market → **Truth:** sell stops go below to protect a long (BLiSS).
- **Trap:** A stop-limit guarantees the investor gets out → **Truth:** it becomes a limit order and may never fill on a gap down.
- **Trap:** A stop executes at the stop price → **Truth:** it becomes a market order at the next trade price.
- **Trap:** The 5% policy is a hard cap and covers new issues → **Truth:** a guideline for secondary trades only.
- **Trap:** Listed stock traded OTC is the second market → **Truth:** that's the third market.
- **Trap:** Not-held orders need written discretionary authority → **Truth:** time/price discretion needs none.
- **Trap:** A 7% drop at 3:40 pm halts trading → **Truth:** Levels 1–2 don't apply after 3:25; only 20% stops trading.

## Memory hooks

- **BLiSS** — Buy Limits and Sell Stops go below; everything else (sell limits, buy stops) above.
- **"The dealer always wins the spread"** — you buy high (ask), sell low (bid).
- **"Stops start, limits lock."** A stop starts a market order; a limit locks the price.
- **"7–13–20."** Halt, halt, home.
