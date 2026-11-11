# Chapter 3: Debt Securities (Bond Fundamentals)

> **In one line:** A bond is a loan with a fixed coupon, so its price moves opposite to interest rates — and every yield, risk and feature follows from that.

## The big ideas

1. **Rates up, prices down** — the fixed coupon becomes less attractive as rates rise; long maturities and low coupons swing the most (zeros most of all).
2. **Discount bonds earn a bonus at maturity, premium bonds give some back** — which fixes the order of nominal, current, YTM and YTC yields.
3. **Who controls the option?** — a call helps the issuer (higher coupon, exercised when rates fall); a put helps the investor (lower coupon, exercised when rates rise).
4. **Bondholders are creditors** — no vote, but paid before all stockholders; credit ratings measure the chance they won't be paid.
5. **Match the risk to the need** — rising rates → short/floating/puttable; known future lump sum → zero-coupon; maximum safety → Treasuries.

## Must-know facts

### Basics and quotes
- **Par** — $1,000; **coupon** fixed, usually paid semiannually (5% = $25 every six months).
- **Indenture** — the contract, enforced by a **trustee**; required by the **Trust Indenture Act of 1939** for corporate issues over $50 million.
- **Term bond** — one maturity date, quoted on **price**. **Serial bond** — staggered maturities (munis), quoted on **yield (basis)**.
- **Quotes** — % of par; 1 point = $10. Corporates/munis in **1/8ths**; Treasuries in **1/32nds** (101.24 = 101 24/32 = $1,017.50).
- **Accrued interest** — buyer pays seller from last coupon **up to but not including settlement**. Corporate/muni **30/360**; government **actual/365**. Defaulted bonds and zeros trade **flat**.
- **Form** — registered/book-entry today; **bearer** bonds no longer issued (since 1982).

### Ratings and risks
- **Investment grade** — AAA, AA, A, **BBB** (S&P/Fitch) = Aaa, Aa, A, **Baa** (Moody's). Below = junk/high-yield.
- **Interest-rate risk** — worst for long-term, low-coupon bonds.
- **Reinvestment risk** — worst for callable, high-coupon bonds when rates fall; **zeros have none**.
- **Inflation risk** — worst for long-term fixed bonds.
- **Credit spread** — corporate minus Treasury yield; **widens** when defaults are feared, narrows in good times.

### Features
- **Callable** — higher coupon; called when rates fall. **Sinking fund** retires bonds over time. **Pre-refunded** bonds are backed by escrowed Treasuries — very safe.
- **Puttable** — investor sells back at par; lower coupon; put when rates rise.
- **Convertible** — exchange into common; lower coupon; **anti-dilution** adjusts for splits.
- **Zero-coupon** — deep discount, matures at par; most rate-sensitive; annual accretion taxed as **phantom income** (not for muni zeros) → good in tax-deferred accounts.
- **Floating-rate** — coupon resets; price stays near par.

### Trading
- **Mostly OTC** — dealer bid/ask; markups must be fair; FINRA **5% policy** is a guideline, not a rule.
- **Reporting** — corporates to **TRACE** within 15 minutes; munis to **MSRB** (RTRS/EMMA).
- **Issuance** — corporates need a prospectus ('33 Act); munis are exempt and use an **official statement**; Treasuries sold at auction.
- **Yield to worst** — confirmation of a callable bond must show the lowest yield.

### Yield relationships

| Bond at | Yield order |
|---|---|
| **Discount** | Nominal < CY < YTM < YTC |
| **Par** | All equal |
| **Premium** | Nominal > CY > YTM > YTC |

### Yield curve and strategies
- **Normal** — long > short (typical). **Flat** — roughly equal. **Inverted** — short > long; recession signal.
- **Ladder** — staggered maturities. **Barbell** — short + long only. **Bullet** — all mature together.

## Numbers to memorize

| What | Number |
|---|---|
| Par value | $1,000 |
| 1 point | $10 (1% of par) |
| 1/8 point | $1.25 |
| 1 basis point | 0.01% (100 bp = 1%) |
| Coupon payments | Semiannual |
| Corporate/muni day count | 30/360 |
| Government day count | Actual/365 |
| Settlement (corporate, muni, Treasury) | T+1 |
| TRACE reporting | Within 15 minutes |
| Lowest investment grade | BBB / Baa |
| Trust Indenture Act threshold | Over $50 million |
| Markup guideline | 5% |

## Formulas

```
Dollar price = Quote (% of par) × $10
```
98 1/8 → 98.125 × $10 = $981.25.

```
Current yield = Annual interest ÷ Market price
```
6% bond at $900 → $60 ÷ $900 = 6.67%.

```
Accrued interest = Par × Coupon × Days ÷ 360   (count to the day BEFORE settlement)
```
6% bond, last coupon Jan 1, settles Mar 16 → 30 + 30 + 15 = 75 days → $60 × 75/360 = $12.50.

```
YTM ≈ [Annual interest + (Par − Price) ÷ Years] ÷ [(Par + Price) ÷ 2]
```
6%, 10 years, price $900 → ($60 + $10) ÷ $950 ≈ 7.37%.

```
Conversion ratio = Par ÷ Conversion price;  Bond parity = Stock price × Ratio
```
$1,000 ÷ $40 = 25 shares; stock at $44 → parity $1,100.

## Exam traps

- **Trap:** Rising rates raise bond prices → **Truth:** rates and prices move inversely; yields and rates move together.
- **Trap:** A high-coupon or short bond is most rate-sensitive → **Truth:** long maturity, low coupon (zeros) swing most.
- **Trap:** For a premium bond, YTM is the lowest yield → **Truth:** YTC is lowest, and dealers quote yield to worst.
- **Trap:** Zeros are tax-free until maturity → **Truth:** the yearly accretion is taxed as phantom income (except muni zeros).
- **Trap:** Puttable bonds pay more because of the extra feature → **Truth:** a put helps the investor, so the coupon is **lower**.
- **Trap:** BB is the lowest investment grade → **Truth:** BBB/Baa is; BB/Ba is junk.
- **Trap:** Accrued interest counts through settlement date → **Truth:** up to but not including settlement.
- **Trap:** Treasury 98.16 means $981.60 → **Truth:** 16/32 → 98.5% = $985.00.
- **Trap:** An inverted curve signals expansion → **Truth:** short above long is a classic recession warning.

## Memory hooks

- **See-saw** — rates on one end, prices on the other.
- **"Discount climbs, premium declines"** — reading left to right N, CY, YTM, YTC.
- **Call = Company's choice; Put = Purchaser's protection.**
- **Zeros: zero coupons, zero reinvestment risk, max rate risk.**
