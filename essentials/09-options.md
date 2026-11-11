# Chapter 9: Options

> **In one line:** Buyers pay a premium for rights and risk only that premium, writers collect it and take on obligations — master the four positions and their gain, loss and breakeven.

## The big ideas

1. **Buyers have rights, writers have obligations.** The buyer's max loss is the premium; the writer's max gain is the premium; only the holder can exercise.
2. **Calls add, puts subtract.** Every breakeven is strike + premium for calls and strike − premium for puts, whichever side you're on.
3. **Sentiment follows the right.** Long call and short put are bullish; long put and short call are bearish.
4. **Hedge the opposite way.** Long stock → buy a put; short stock → buy a call; own stock and want income → write a covered call.

## Must-know facts

### Contract basics
- **Call** — right to buy; **put** — right to sell.
- **Contract** — 100 shares; premium × 100 = dollar cost (premium 3 = $300).
- **Expiration** — third Friday of the month.
- **American style** — exercise anytime (equity options); **European** — only at expiration (most index options).
- **OCC** — issues and guarantees listed options; no counterparty risk.
- **ODD** — *Characteristics and Risks of Standardized Options*, delivered at or before account approval.
- **Settlement** — trades and exercised stock settle T+1.
- **Wasting asset** — time value decays to zero at expiration.

### Moneyness and value

| | Call | Put |
|---|---|---|
| In the money | Stock > strike | Stock < strike |
| Out of the money | Stock < strike | Stock > strike |

- **Intrinsic value** — the in-the-money amount, never negative.
- **Time value** — premium − intrinsic value.
- **Premium rises with** — more time, more volatility, deeper in the money.

### Exercise and closing
- **Assignment** — random or FIFO, never by largest position.
- **Automatic exercise** — at $0.01 or more ITM at expiration.
- **Taxes** — exercised call: buyer's basis = strike + premium; exercised put: buyer's proceeds = strike − premium.

### Corporate action adjustments
- **Even split (2:1)** — more contracts, lower strike: 1 × 60 call → 2 × 30 calls.
- **Uneven split (3:2) / stock dividend** — same contracts, more shares: 1 × 60 call → 1 × 40 call for 150 shares.
- **Reverse split** — fewer shares per contract, higher strike.
- **Ordinary cash dividend** — no adjustment.

### The four positions

| Position | Sentiment | Max gain | Max loss | Breakeven |
|---|---|---|---|---|
| Long call | Bullish | Unlimited | Premium | Strike + premium |
| Short call | Bearish | Premium | Unlimited (naked) | Strike + premium |
| Long put | Bearish | Strike − premium | Premium | Strike − premium |
| Short put | Bullish | Premium | Strike − premium | Strike − premium |

- **Naked call** — riskiest basic strategy; highest approval level. **Cash-secured put** — writer holds cash equal to the strike.

### Strategies
- **Protective put** — long stock + long put; best hedge for long stock.
- **Protective call** — short stock + long call; best hedge for short stock.
- **Covered call** — long stock + short call; income, neutral to mildly bullish; most conservative; caps upside.
- **Index options** — cash settled, $100 multiplier, usually European; buy index puts to hedge a diversified portfolio.
- **LEAPS** — long-term options up to 39 months.

## Numbers to memorize

| What | Number |
|---|---|
| Shares per contract / multiplier | 100 |
| Expiration | Third Friday |
| Last trading / exercise cut-off | 4:00 pm / 5:30 pm ET |
| Automatic exercise | $0.01 ITM |
| Option and exercise settlement | T+1 |
| Index option cash settlement | Next business day |
| LEAPS maximum | 39 months |
| Broad-based index option tax | 60% long-term / 40% short-term |

## Formulas

```
Call intrinsic = Stock − Strike;  Put intrinsic = Strike − Stock;  Time value = Premium − Intrinsic
```
Stock 54, 50 call @ 6: intrinsic 4, time value 2.

```
Breakeven: Calls = Strike + Premium;  Puts = Strike − Premium
```
50 put @ 3 → breakeven 47.

```
Protective put: Max loss = (Cost − Strike) + Premium;  Breakeven = Cost + Premium
```
Stock at 50, 45 put @ 2: max loss $700; breakeven 52.

```
Covered call: Max gain = (Strike − Cost) + Premium;  Breakeven = Cost − Premium
```
Stock at 48, 50 call @ 3: max gain $500; breakeven 45.

```
Index option payout = ITM points × $100
```
SPX 5,800 put, index 5,740: 60 × $100 = $6,000.

## Exam traps

- **Trap:** The writer can exercise → **Truth:** only the holder exercises; the writer is assigned.
- **Trap:** A short put's breakeven is strike + premium → **Truth:** puts always subtract.
- **Trap:** The short put's max loss is unlimited → **Truth:** strike − premium (stock stops at zero); naked *calls* are unlimited.
- **Trap:** Premium decides in or out of the money → **Truth:** only strike vs. stock price.
- **Trap:** A 3:2 split gives more contracts → **Truth:** uneven splits add shares per contract; even splits add contracts.
- **Trap:** Options adjust for regular cash dividends → **Truth:** no adjustment.
- **Trap:** Index option exercise delivers stock → **Truth:** cash settled.
- **Trap:** Covered call protects against a decline → **Truth:** premium only cushions it; buy a put for protection.

## Memory hooks

- **Call Up, Put Down** — calls ITM above strike, puts ITM below.
- **Calls add, puts subtract** — for every breakeven.
- **Hedge with the opposite** — long stock buys a put, short stock buys a call.
