# Chapter 10: Taxes

> **In one line:** Tax depends on what kind of income it is (interest, dividend, gain), who issued the security, and how long you held it — and losses can only offset income in the right bucket.

## The big ideas

1. **Character decides the rate** — qualified dividends and long-term gains get 0/15/20%; interest, ordinary dividends and short-term gains are taxed as ordinary income.
2. **The issuer decides the exemption** — Treasuries skip state tax, munis skip federal tax, and corporate/MBS interest is taxed everywhere.
3. **Nothing is taxed until it is realized** — appreciation, stock dividends and splits only change basis; the sale is the taxable event.
4. **Basis is the whole game** — commissions, reinvested distributions, return of capital, gifts, inheritances and wash sales all work by moving cost basis.
5. **Three income buckets don't mix** — passive losses offset only passive income; earned income alone funds an IRA.

## Must-know facts

### Dividends
- **Cash dividends** — taxable in the year paid, even if reinvested.
- **Qualified dividends** — US (or qualifying foreign) corporations, held 60+ days around the ex-date → LTCG rates.
- **Ordinary dividends** — REITs, money market funds, bond funds, fund short-term gain distributions → ordinary rates.
- **Stock dividends/splits** — not taxed; same total basis spread over more shares.
- **Fund LTCG distributions** — long-term regardless of how long the fund shares were held.
- **Dividends-received deduction** — corporations exclude 50% (65% if 20%+ owned) of domestic dividends; why corporations favor preferred.

### Interest
| Source | Federal | State |
|---|---|---|
| Corporate bonds, CDs, money market | Taxable | Taxable |
| Treasuries, FHLB, Farm Credit | Taxable | **Exempt** |
| GNMA, FNMA, FHLMC | Taxable | Taxable |
| Munis | **Exempt** (private activity → AMT) | Exempt in-state; territories exempt everywhere |

- **OID / zero-coupon accretion** — corporate and Treasury zeros: taxed yearly with no cash received (phantom income); basis rises. Muni OID accretion: tax-exempt.
- **Market discount** — taxed as ordinary income at sale/maturity, even on munis.
- **Muni premium** — must be amortized; the amortization is not deductible.
- **EE/I savings bonds** — tax-deferred until redemption; can be tax-free for qualified education.

### Capital gains and losses
- **Short-term** — held 1 year or less → ordinary rates. **Long-term** — more than 1 year.
- **Holding period** — starts the day after trade date; trade date (not settlement) sets the tax year.
- **Netting** — net ST, net LT, then net together; excess loss deducts $3,000/yr against ordinary income; rest carries forward indefinitely.
- **Wash sale** — loss disallowed if substantially identical security (same stock, its calls, convertibles, same fund) bought 30 days before or after; disallowed loss is added to the new basis. Never applies to gains or to a different company.
- **Lot ID** — FIFO is the IRS default; specific ID is most flexible; average cost for mutual funds.
- **Return of capital** — not taxed when received; lowers basis.

| | Gift | Inheritance |
|---|---|---|
| Basis | Donor's (carryover); for a loss, lower of donor basis or FMV at gift | FMV at date of death (step-up) |
| Holding period | Donor's carries over | Always long-term |

### Income types and other rules
| Bucket | Examples | Key rule |
|---|---|---|
| Earned | Wages, bonuses, self-employment | Only income eligible for IRA contributions |
| Portfolio | Interest, dividends, capital gains | Capital losses offset gains + $3,000 |
| Passive | Limited partnerships/DPPs, passive rentals | Passive losses offset only passive income |

- **Progressive tax** — higher marginal rates at higher income. **Effective rate** = total tax ÷ income. Sales tax is regressive.
- **AMT** — adds back private activity muni interest; AMT payers avoid those bonds.
- **Backup withholding** — 24% if no TIN (W-9).
- **Tax-deferred vs. tax-free** — deferred = taxed later (traditional IRA, annuity); free = never (qualified Roth, muni interest).

## Numbers to memorize

| What | Number |
|---|---|
| LTCG / qualified dividend rates | 0%, 15%, 20% |
| Long-term holding period | More than 1 year |
| Qualified dividend holding requirement | More than 60 days |
| Net capital loss vs. ordinary income | $3,000/yr ($1,500 married filing separately) |
| Wash sale window | 30 days before or after (61 days) |
| Annual gift exclusion (2026) | $19,000 per recipient; $38,000 per couple |
| Backup withholding | 24% |
| Dividends-received deduction | 50% (65% if 20%+ owned) |
| Index options/futures | 60% long-term / 40% short-term |
| Collectibles LTCG max | 28% |

## Formulas

```
Gain (loss) = Net sale proceeds − Cost basis (price + commissions)
```
Buy 100 at $30 + $20 commission ($3,020 basis); sell at $40 − $20 ($3,980) → $960 gain.

```
Wash sale new basis = Purchase price of new shares + Disallowed loss
```
Sell at a $500 loss, rebuy 100 at $28 within 30 days → basis $2,800 + $500 = $3,300.

```
Effective tax rate = Total tax ÷ Total taxable income
```
$18,000 tax on $120,000 → 15%.

## Exam traps

- **Trap:** Reinvested dividends aren't taxed → **Truth:** they are taxed in the year paid.
- **Trap:** Buying the stock's call options after a loss sale avoids the wash sale → **Truth:** options are substantially identical; loss disallowed.
- **Trap:** A wash-sale loss is gone forever → **Truth:** it is added to the new shares' basis.
- **Trap:** Gifted stock gets a stepped-up basis → **Truth:** gifts carry over the donor's basis; only inheritances step up.
- **Trap:** Inherited stock sold a month later is short-term → **Truth:** inherited property is always long-term.
- **Trap:** GNMA interest is state tax-free like Treasuries → **Truth:** GNMA/FNMA/FHLMC are taxed at every level.
- **Trap:** Zeros pay no cash, so no tax until maturity → **Truth:** corporate/Treasury accretion is taxed annually.
- **Trap:** LP losses can offset salary → **Truth:** passive losses offset only passive income.

## Memory hooks

- **"T-bills skip the State; Munis skip the Feds; Mortgages pay Both."**
- **"Gift = Given basis; Death = Date-of-death."**
- **"Wash = 30 + 30."** One month on each side of the loss sale.
- **"Three grand, then carry."** $3,000 loss deduction, rest carries forward.
- **"Long = longer than a year"** — exactly one year is still short-term.
