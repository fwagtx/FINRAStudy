# Chapter 9: Options

> Options are tested at a basic level on the SIE — definitions, the four basic positions (max gain/loss/breakeven), simple hedging and income strategies, and index option basics. You don't need advanced spreads/straddles. Learn the four-position table cold.

---

## 9.1 Fundamentals

An **option** is a contract giving the buyer the **right** (not the obligation) to buy or sell a specific amount of an underlying asset at a set price within a set period. The seller (writer) takes on the **obligation** to fulfill the contract if the buyer exercises. Options are **derivatives** — their value derives from the underlying security.

**Two types of contracts.**

- **Call** — the right to **buy** the underlying at the strike price. Buyers of calls are **bullish**.
- **Put** — the right to **sell** the underlying at the strike price. Buyers of puts are **bearish**.

**Two sides of every contract.**

- **Buyer (holder, long)** — pays the **premium**; has rights; risk is limited to the premium paid.
- **Seller (writer, short)** — receives the premium; has obligations; takes on risk in exchange for income.

**Contract terms (standard equity option).**

| Term | Meaning |
|---|---|
| **Underlying** | The stock (e.g., XYZ) |
| **Contract size** | **100 shares** per contract |
| **Strike (exercise) price** | The price at which the stock is bought/sold if exercised |
| **Expiration** | Standard monthly options expire on the **third Friday** of the month (trading stops at 4:00 pm ET that day; exercise cut-off 5:30 pm ET). Weeklies and LEAPS (up to 39 months) also exist. |
| **Premium** | The price of the option, quoted per share; multiply by 100 for the contract cost. A premium of 3 = $300. |
| **Style** | **American** (exercise any time before expiration — all equity options) vs. **European** (exercise only at expiration — most index options) |

**Reading an option:** "Buy 1 XYZ Jan 50 call @ 3" = the buyer pays $300 for the right to buy 100 shares of XYZ at $50 any time until the January expiration.

**The four basic positions and market sentiment.**

| Position | Sentiment | Right/obligation |
|---|---|---|
| Long call | Bullish | Right to buy |
| Short call | Bearish (or neutral) | Obligation to sell |
| Long put | Bearish | Right to sell |
| Short put | Bullish (or neutral) | Obligation to buy |

**Why use options?** Speculation with leverage (control 100 shares for a small premium), **hedging** an existing position (insurance), and generating **income** (writing options). Options are a **zero-sum game** — the buyer's gain is the writer's loss and vice versa.

---

## 9.2 Contracts and the market

### 9.2.1 Issuance & the market

- Listed options are **issued and guaranteed by the Options Clearing Corporation (OCC)**, which stands between every buyer and seller, eliminating counterparty risk. The OCC sets standardized terms (strikes, expirations). There is no "issuer" in the corporate sense — the OCC creates contracts as buyers and sellers are matched.
- Options trade on exchanges, chiefly the **Cboe (Chicago Board Options Exchange)**, plus NYSE Arca, Nasdaq PHLX, ISE and others. Options are **not** registered under the 1933 Act with a traditional prospectus; instead, investors must receive the **Options Disclosure Document (ODD)** — *Characteristics and Risks of Standardized Options* — at or before account approval.
- **Settlement of option trades: T+1** (regular way). Exercise of an equity option results in a stock transaction that settles **T+1** as well.
- Options are **wasting assets** — their time value declines as expiration approaches and they are worthless if they expire out of the money.
- Open interest = number of contracts outstanding.

### 9.2.2 Options contracts

**In, at, out of the money** — depends only on the strike vs. the stock price (premium is ignored).

| | Call | Put |
|---|---|---|
| **In the money (ITM)** | Stock price **above** strike | Stock price **below** strike |
| **At the money** | Stock = strike | Stock = strike |
| **Out of the money (OTM)** | Stock price below strike | Stock price above strike |

Mnemonic: **Call Up, Put Down** — a call is in the money when the stock is up above the strike; a put is in the money when the stock is down below the strike.

**Intrinsic value** = the amount by which the option is in the money (never negative).

- Call intrinsic value = stock price − strike (if positive).
- Put intrinsic value = strike − stock price (if positive).

**Time value** = premium − intrinsic value. Reflects the time remaining and the stock's volatility. At expiration, time value is zero and the option is worth exactly its intrinsic value.

**Example.** XYZ is at $54. An XYZ 50 call trades at 6. Intrinsic value = 54 − 50 = 4; time value = 6 − 4 = **2**. An XYZ 50 put trading at 1 has intrinsic value 0 (out of the money) and time value 1.

**Factors that increase a premium:** more time to expiration, higher volatility of the underlying, deeper in the money. For calls, higher interest rates and lower dividends; for puts, the opposite.

### 9.2.3 Premiums & exercise

**Three ways to close an option position.**

1. **Let it expire** — buyer loses the premium; writer keeps it. Most common for OTM options.
2. **Closing transaction** — buyer sells the option (**closing sale**); writer buys it back (**closing purchase**). Most common way to realize a profit.
3. **Exercise** — buyer exercises the right; the OCC assigns a writer (randomly, and the firm then assigns a customer by random selection, first-in-first-out or another fair method — never on a "largest position" basis). The buyer/holder is the **only** party who can exercise.

**Automatic exercise.** The OCC automatically exercises equity options that are in the money by **$0.01 or more** at expiration unless the holder instructs otherwise.

**Exercise mechanics.** Exercising a call: the holder pays strike × 100 and receives 100 shares; the assigned writer delivers the shares. Exercising a put: the holder delivers 100 shares and receives strike × 100; the assigned writer must buy. Stock delivered from an exercise settles T+1.

**Tax basics.** Premiums are capital in nature. A buyer who lets an option expire has a capital loss equal to the premium; a writer whose option expires has a short-term capital gain. When a call is exercised, the premium adjusts the stock's cost (buyer's cost basis = strike + premium; writer's sale proceeds = strike + premium). When a put is exercised, the buyer's sale proceeds = strike − premium; the writer's cost basis = strike − premium.

### 9.2.4 Stock split & dividend adjustments

The OCC adjusts option contracts for corporate actions so neither side is harmed.

- **Even forward splits (2:1, 3:1, etc.)** — the **number of contracts** is multiplied and the **strike** is divided. 1 XYZ 60 call after a 2:1 split → **2 XYZ 30 calls**, each still for 100 shares.
- **Uneven splits (3:2, 5:4) and stock dividends** — the number of contracts stays the same, the **number of shares per contract** increases and the strike is reduced proportionally. 1 XYZ 60 call after a 3:2 split → 1 XYZ 40 call covering **150 shares**.
- **Reverse splits** — shares per contract decrease, strike increases.
- **Cash dividends** — **no adjustment** for ordinary cash dividends (only for unusually large/special dividends). The stock price drops by the dividend on the ex-date, which hurts call holders and helps put holders.

The total value of the position (contracts × shares × strike) is unchanged by any adjustment.

---

## 9.3 Strategies

For each of the four basic positions, know: sentiment, maximum gain, maximum loss, and breakeven. Premiums are per share; multiply by 100 for dollar totals.

### 9.3.1 Long calls

Buy a call → **bullish**. Right to buy at the strike.

- **Maximum loss:** the premium paid.
- **Maximum gain:** unlimited (stock can rise forever).
- **Breakeven:** strike + premium.
- Profits when the stock rises above the breakeven by expiration.

**Example.** Buy 1 ABC Mar 40 call @ 2. Max loss $200. Breakeven $42. If ABC rises to $50 and the holder exercises and sells the stock: buy at 40, sell at 50 = $1,000 gain − $200 premium = **$800 profit**. Used for leveraged speculation or to lock in a purchase price.

### 9.3.2 Short calls

Write (sell) a call → **bearish/neutral**. Obligation to sell at the strike if assigned.

- **Maximum gain:** the premium received.
- **Maximum loss:** **unlimited** if **uncovered (naked)** — the writer may have to buy stock at any price to deliver. (If **covered** — the writer owns the stock — the risk is the downside of the stock, cushioned by the premium.)
- **Breakeven:** strike + premium (same as the long call; the writer profits below it).

Naked call writing is the **riskiest** basic option strategy and requires a margin account and the highest level of option approval.

### 9.3.3 Long puts

Buy a put → **bearish**. Right to sell at the strike.

- **Maximum loss:** the premium.
- **Maximum gain:** strike − premium (stock can only fall to zero).
- **Breakeven:** strike − premium.

**Example.** Buy 1 XYZ Jun 50 put @ 3. Max loss $300. Breakeven $47. Max gain $4,700 (if XYZ goes to 0). A long put is the alternative to selling short with limited risk.

### 9.3.4 Short puts

Write a put → **bullish/neutral**. Obligation to buy at the strike if assigned.

- **Maximum gain:** the premium.
- **Maximum loss:** strike − premium (stock can fall to zero and the writer must still buy at the strike).
- **Breakeven:** strike − premium.

A short put is "covered" if the writer has cash equal to the strike (cash-secured put) or is short the stock. Some investors write puts to buy a stock they like at a lower effective price.

### Summary table (memorize)

| Position | Sentiment | Max gain | Max loss | Breakeven |
|---|---|---|---|---|
| **Long call** | Bullish | Unlimited | Premium | Strike + premium |
| **Short call** | Bearish | Premium | Unlimited (naked) | Strike + premium |
| **Long put** | Bearish | Strike − premium | Premium | Strike − premium |
| **Short put** | Bullish | Premium | Strike − premium | Strike − premium |

Rules of thumb: **Calls → add** the premium to the strike for breakeven; **puts → subtract**. Buyers' max loss = premium; writers' max gain = premium. The buyer's max gain is the writer's max loss.

### 9.3.5 Hedging strategies

Options as **insurance** for a stock position.

- **Protective put (married put):** own stock + **buy a put**. Protects against a decline — the put locks in a minimum sale price (the strike). Cost: the premium. Maximum loss = (stock cost − strike) + premium; upside unlimited (minus the premium). The best hedge for a long stock position. Breakeven = stock cost + premium.
- **Protective call:** short stock + **buy a call**. Protects a short seller against a rise — caps the repurchase price at the strike. Max loss = (strike − short sale price) + premium. The best hedge for a short stock position.

**Example.** An investor bought XYZ at $50 and buys an XYZ 45 put @ 2. Worst case: she puts the stock at 45, losing $5/share plus the $2 premium = max loss **$700**. Breakeven = $52.

### 9.3.6 Income strategies

- **Covered call:** own stock + **write a call**. The writer collects premium income and is willing to sell the stock at the strike. Appropriate for a **neutral to mildly bullish** outlook on stock already owned. It is the **most conservative option strategy** and the one most commonly permitted in retirement accounts and basic-level option accounts.
  - Max gain = (strike − stock cost) + premium.
  - Max loss = stock cost − premium (stock goes to zero).
  - Breakeven = stock cost − premium.
  - Downside: upside above the strike is **given up** (the stock gets called away).
- **Covered put:** short stock + write a put. Income on a short position; rare.
- **Cash-secured put:** write a put while holding cash to buy the stock if assigned — a way to earn income while waiting to buy a stock at a lower price.

**Example.** Investor owns 100 XYZ bought at $48, writes an XYZ 50 call @ 3. Max gain = (50 − 48) + 3 = $5 × 100 = **$500**. Breakeven = 48 − 3 = **$45**. Max loss = $4,500.

### 9.3.7 Index options

Options on a stock index (S&P 500 — SPX, S&P 100 — OEX, Nasdaq-100 — NDX, Russell 2000, VIX) rather than a single stock.

- **Cash settled** — no stock changes hands. On exercise, the ITM amount × the multiplier (**$100**) is paid in cash the next business day (T+1).
- Most broad-based index options are **European style** (exercisable only at expiration); some (OEX) are American.
- Settlement value is typically based on the index's **closing** value on the exercise day (or the opening value for a.m.-settled options).
- Used to **hedge a diversified portfolio** (buy index puts) or to speculate on the overall market without picking stocks.
- Index options have the same max gain/loss rules as equity options; a broad-based index put is the classic portfolio hedge.
- Trade mostly on the Cboe; broad-based index options get favorable 60/40 tax treatment (60% long-term, 40% short-term) regardless of holding period.

**Example.** An investor with a $500,000 diversified portfolio buys S&P 500 puts to protect against a market drop. If the index falls 10%, the puts gain roughly enough to offset the portfolio's loss (minus the premium paid).

**Other option types (just recognize):** **LEAPS** (long-term, up to 39 months), **foreign currency options** (hedge exchange-rate risk; the OCC issues them too), **interest rate/yield-based options**, options on ETFs (physically settled like equity options).

---

## Chapter 9 quick review

- Call = right to buy; put = right to sell. Buyer pays premium and has rights; writer receives premium and has obligations. 100 shares per contract; premium × 100 = cost.
- Expiration: third Friday; equity options American style; index options usually European and **cash settled** ($100 multiplier).
- OCC issues/guarantees all listed options; ODD must be delivered before approval; options trades settle T+1.
- ITM: call when stock > strike; put when stock < strike. Intrinsic value = ITM amount; time value = premium − intrinsic.
- Auto-exercise at $0.01 ITM. Assignment random/FIFO, never largest first.
- Even splits: more contracts, lower strike. Uneven splits/stock dividends: more shares per contract. Cash dividends: no adjustment.
- The four-position table: buyers risk the premium; naked call writers face unlimited loss; put writers' max loss = strike − premium. Calls add premium for breakeven, puts subtract.
- Hedges: long stock → buy put; short stock → buy call. Income: long stock → write call (covered call = most conservative, caps upside).
- Index options hedge whole portfolios; cash settled next business day.
