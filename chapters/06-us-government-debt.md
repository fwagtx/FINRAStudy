# Chapter 6: US Government Debt (and the Economy)

> Two big topics live here: (1) Treasury and agency securities, and (2) the Federal Reserve, monetary/fiscal policy and economic indicators. Section 1 of the FINRA outline ("Knowledge of Capital Markets," 16%) draws heavily on 6.5.

---

## 6.1 Foundations

The US Treasury borrows to fund the federal deficit by issuing securities that are backed by the **full faith and credit of the United States** — considered to have **no credit (default) risk**, which makes them the benchmark "risk-free rate" against which all other yields are measured. They still carry **interest-rate risk**, **inflation risk** and (for coupon-bearing issues) **reinvestment risk**.

**Tax treatment (memorize).** Interest on US Treasury and most agency securities is **taxable at the federal level but exempt from state and local income tax**. (Exactly the opposite of municipal bonds.) Exception: Ginnie Mae, Fannie Mae and Freddie Mac mortgage-backed interest is taxable at **all** levels.

**How Treasuries are sold.** At regularly scheduled **Treasury auctions** conducted by the Fed on behalf of the Treasury:

- **Competitive bids** (from primary dealers and institutions) specify the yield they'll accept.
- **Non-competitive bids** (typically individuals, through TreasuryDirect or brokers) accept whatever yield the auction sets and are always filled first.
- Treasuries are issued in **book-entry** form only (no certificates).
- Minimum denomination is **$100**.

**Quotes.** Treasury notes and bonds are quoted in **1/32nds** of a point. "99.08" or "99-08" = 99 8/32 = 99.25% of par = $992.50. T-bills are quoted on a **discount yield** basis (annualized discount from par), so for bills a **higher** quoted number means a **lower** price.

**Settlement:** T+1 (regular way), through the Federal Reserve's book-entry system. Accrued interest on Treasuries uses **actual days / 365**.

---

## 6.2 Treasury products

| Security | Maturity | Interest | How sold | Notes |
|---|---|---|---|---|
| **Treasury bills (T-bills)** | 4, 8, 13, 17, 26, 52 weeks (≤ 1 year) | None — sold at a **discount**, mature at par | Weekly/monthly auctions | Money-market instrument; quoted on discount yield; most liquid security in the world |
| **Treasury notes (T-notes)** | **2–10 years** (2, 3, 5, 7, 10) | Semiannual coupon | Auction | Quoted in 1/32nds |
| **Treasury bonds (T-bonds)** | **20–30 years** | Semiannual coupon | Auction | Quoted in 1/32nds; some old issues callable |
| **TIPS** (Treasury Inflation-Protected Securities) | 5, 10, 30 years | Fixed coupon **rate** on a principal that adjusts with CPI | Auction | Protects against inflation; principal increase is taxed annually as income (phantom income); at maturity you receive the greater of adjusted or original principal |
| **STRIPS** (Separate Trading of Registered Interest and Principal of Securities) | Various | **Zero-coupon** — each coupon and the principal are stripped and sold separately at a discount | Created by dealers from Treasuries | Backed directly by the Treasury; no reinvestment risk; most interest-rate-sensitive; accreted discount taxed annually |
| **Treasury receipts** (CATS, TIGRs, etc.) | Various | Zero-coupon | Created by broker-dealers | Collateralized by Treasuries held in trust but **not direct obligations** of the Treasury (slightly less safe than STRIPS) |
| **Floating-rate notes (FRNs)** | 2 years | Rate resets weekly to the 13-week T-bill auction rate | Auction | Minimal interest-rate risk |
| **Savings bonds (Series EE, I)** | Up to 30 years | EE: fixed rate; I: fixed + inflation component | TreasuryDirect | **Non-negotiable** (can't be sold, only redeemed); interest is tax-deferred until redemption; may be federally tax-free if used for qualified education expenses |

**TIPS example.** $1,000 TIPS with a 2% coupon. CPI rises 3% in year one → principal becomes $1,030; the coupon is 2% × $1,030 = $20.60. If inflation continues, both principal and dollar interest keep rising. In deflation the principal falls (but never below the original at maturity).

**Which Treasury has the most interest-rate risk?** Long-term STRIPS (long maturity + zero coupon). **Least?** T-bills and FRNs.

---

## 6.3 Federal agency products

Federal agencies and **government-sponsored enterprises (GSEs)** issue debt to support specific sectors (housing, agriculture, education). Agency securities generally yield slightly more than Treasuries. Interest is federally taxable; state tax treatment varies.

**Direct government backing vs. GSE.**

- **Ginnie Mae (GNMA — Government National Mortgage Association)** — part of HUD. Its **mortgage-backed pass-through certificates** are the **only** agency securities backed by the **full faith and credit of the US government**. Interest is taxable at **federal, state and local** levels. Minimum $25,000 (pools), pay **monthly** interest and principal.
- **Fannie Mae (FNMA)** and **Freddie Mac (FHLMC)** — publicly traded GSEs (in federal conservatorship since 2008) that buy mortgages from lenders and issue mortgage-backed securities. Not legally backed by the government ("implied" backing). Taxable at all levels.
- **Federal Farm Credit Banks**, **Federal Home Loan Banks** — GSEs issuing notes and bonds to support agriculture and housing. Interest exempt from state/local tax.
- **Sallie Mae (SLM)** — formerly a GSE for student loans, now private.
- **Tennessee Valley Authority (TVA)** — issues bonds backed by its power revenues.

**Mortgage-backed securities (MBS) — key concepts.**

- A **pass-through** collects mortgage payments from a pool of homeowners and passes principal and interest through to investors **monthly**. Each payment is part interest (taxable) and part return of principal (not taxable).
- **Prepayment risk** — when rates **fall**, homeowners refinance, returning principal early that must be reinvested at lower rates. **Extension risk** — when rates **rise**, prepayments slow and the security's life extends. Because of this, MBS cash flows and maturities are uncertain; the "average life" is an estimate.
- **Collateralized mortgage obligations (CMOs)** — MBS pools carved into **tranches** with different maturities and priorities to redistribute prepayment risk. Sequential-pay tranches get principal in order; **planned amortization class (PAC)** tranches have the most predictable cash flow (prepayment risk shifted to "companion/support" tranches); **Z-tranches** accrue like zeros. CMOs pay interest monthly, are taxable at all levels, and are **complex** — FINRA requires specific disclosure and suitability review; they must not be compared to Treasuries or CDs in communications. Minimum denomination typically $1,000.
- **Collateralized debt obligations (CDOs)** and **asset-backed securities (ABS)** — similar structures backed by other loans (auto loans, credit cards, corporate debt).

---

## 6.4 The market

**Primary dealers** — a group of large banks and broker-dealers approved by the Fed to bid at every Treasury auction and to trade directly with the Fed in open-market operations.

**Secondary market.** Treasuries trade OTC in an enormous, extremely liquid dealer market; spreads are tiny (fractions of a 32nd). Prices are published daily. Agency securities trade similarly but less liquidly.

**Settlement.** T+1 regular way; same-day cash settlement is common for Treasuries. Delivery via Fed book-entry.

**Treasury yields as benchmarks.** The 10-year Treasury yield is the benchmark for mortgage rates and corporate bonds; the 3-month T-bill rate is the "risk-free rate" in financial models. The **spread** between a corporate bond and the Treasury of the same maturity reflects credit risk.

**The yield curve** (Treasuries define it): normal, flat, inverted — see Chapter 3. The Fed influences the **short** end directly; the long end reflects market expectations for growth and inflation.

---

## 6.5 The economy, the Fed and policy

### 6.5.1 Monetary policy

**Monetary policy** is controlled by the **Federal Reserve** (the Fed) — the US central bank, independent of Congress and the President in day-to-day operations. Its dual mandate: **stable prices (control inflation)** and **maximum employment**. The **Federal Open Market Committee (FOMC)** — 12 members (7 governors + NY Fed president + 4 rotating regional presidents) — meets roughly every 6 weeks (8 times a year) to set policy.

- **Easy (expansionary, accommodative) money policy** — Fed increases the money supply, lowers interest rates → stimulates borrowing, spending, growth; risk of inflation. Used during recessions.
- **Tight (contractionary, restrictive) money policy** — Fed decreases the money supply, raises rates → slows the economy to fight inflation. Risk of recession.

**Money supply measures.** **M1** = currency in circulation + checking/demand deposits (+ savings deposits since 2020). **M2** = M1 + small time deposits + retail money market funds. **M3** adds large time deposits and institutional funds.

### 6.5.2 Rates

| Rate | What it is | Who sets it |
|---|---|---|
| **Federal funds rate** | Rate banks charge each other for **overnight** loans of excess reserves held at the Fed. The most sensitive, closely watched indicator of Fed policy. | The market, but the **FOMC sets a target range** and manages it via open-market operations |
| **Discount rate** | Rate the Fed charges **member banks** for short-term loans directly from the Fed's "discount window" | **The Fed** (directly) |
| **Prime rate** | Rate commercial banks charge their **most creditworthy corporate customers**; benchmark for many consumer loans | Banks (typically fed funds + 3%) |
| **Broker call (call money) rate** | Rate banks charge broker-dealers on loans used to finance customer margin accounts | Banks; usually slightly above fed funds |
| **SOFR** | Secured Overnight Financing Rate — the replacement for LIBOR as the benchmark for floating-rate products | Published by the NY Fed from repo transactions |

Rough ordering from lowest to highest: fed funds ≈ discount rate < broker call < prime.

**Interest-rate effects.** Rising rates: bond prices fall, borrowing costs rise, stock valuations tend to fall (especially growth stocks and rate-sensitive sectors like utilities), the dollar tends to strengthen. Falling rates: the reverse.

### 6.5.3 Tools of the Federal Reserve

| Tool | To ease (stimulate) | To tighten (fight inflation) | Notes |
|---|---|---|---|
| **Open-market operations (FOMC)** | **Buys** Treasuries from primary dealers → adds reserves/money to the system → rates fall | **Sells** Treasuries → drains money → rates rise | **Most frequently used** and most flexible tool; repos (temporary buying) and reverse repos (temporary selling) are the day-to-day versions |
| **Discount rate** | Lower | Raise | Signal of Fed intent |
| **Reserve requirements** | Lower (banks can lend more) | Raise | Most powerful but **least used** (reserve ratio has been 0% since 2020) |
| **Interest on reserve balances** | Lower | Raise | Modern primary tool for steering fed funds within the target range |
| **Margin requirements (Reg T)** | — | — | The Fed sets them (50%), but they are rarely changed and not really used as a policy tool |

**Quantitative easing (QE)** — large-scale purchases of long-term Treasuries and MBS to push long rates down when short rates are already near zero. **Quantitative tightening (QT)** — letting holdings run off.

**Memory aid:** when the Fed **buys**, it pumps money in (easy). When the Fed **sells**, it soaks money up (tight). "Buy = Bigger money supply."

### 6.5.4 Economic factors

**The business cycle.** Four phases: **expansion** (recovery) → **peak** → **contraction** (recession) → **trough**, then repeat.

- **Recession** — commonly defined as **two consecutive quarters of declining GDP** (officially declared by the NBER).
- **Depression** — a severe, prolonged recession (often described as 6+ quarters of decline or a very deep fall in GDP).

**Key measures.**

- **Gross domestic product (GDP)** — total value of goods and services produced *within* the US, regardless of who owns the producer. (GNP = output of US-owned entities anywhere.) Reported quarterly, adjusted for inflation as "real GDP."
- **Consumer Price Index (CPI)** — the main measure of inflation (prices of a basket of consumer goods). The **Producer Price Index (PPI)** measures wholesale prices and tends to lead CPI.
- **Inflation** — general rise in prices; erodes purchasing power; hurts fixed-income investors most. **Deflation** — falling prices. **Stagflation** — stagnant growth plus high inflation.
- **Unemployment rate** — lagging indicator.

**Economic indicators** (classified by timing relative to the cycle).

| Type | Examples |
|---|---|
| **Leading** (change *before* the economy) | **Stock market (S&P 500)**, building permits/housing starts, new orders for durable goods, initial unemployment claims, money supply (M2), average weekly hours in manufacturing, consumer expectations, yield curve/spread |
| **Coincident** (move *with* the economy) | GDP, industrial production, personal income, nonfarm payrolls/employment, manufacturing & trade sales |
| **Lagging** (change *after*) | **Unemployment rate**, average duration of unemployment, CPI/inflation, prime rate, corporate profits, consumer debt levels, inventories-to-sales ratio |

**Economic theories (know the one-liners).**

- **Keynesian** — government spending and taxation (fiscal policy) drive demand; government should spend during downturns.
- **Monetarist** (Milton Friedman) — the money supply is what matters; the Fed should grow it steadily.
- **Supply-side** — cut taxes and regulation to encourage production; growth will follow.

**International factors.**

- **Balance of payments / balance of trade** — exports minus imports. A **trade deficit** (imports > exports) tends to weaken the dollar over time.
- **Currency effects**: a **weak dollar** helps US exporters (their goods are cheaper abroad) and hurts importers and US consumers of foreign goods; a **strong dollar** does the opposite. Foreign investors holding US bonds gain when the dollar strengthens.
- **Exchange rates** are set in the foreign-exchange (forex) market; higher US interest rates tend to attract foreign capital and strengthen the dollar.

### 6.5.5 Fiscal policy

**Fiscal policy** is the government's use of **taxation and spending**, set by **Congress and the President** (not the Fed). It's rooted in Keynesian economics.

- **Expansionary fiscal policy** — cut taxes, increase government spending → stimulates demand; increases the budget deficit; can cause inflation.
- **Contractionary fiscal policy** — raise taxes, cut spending → slows the economy; reduces the deficit.
- Fiscal policy is **slower** to implement than monetary policy (requires legislation) but can target specific groups.
- Large deficits mean more Treasury issuance, which can push interest rates up ("crowding out" private borrowing).

**Monetary vs. fiscal — the comparison the exam wants:**

| | Monetary policy | Fiscal policy |
|---|---|---|
| Who | Federal Reserve (FOMC) | Congress & President |
| Tools | Open-market ops, discount rate, reserve requirements | Taxes, government spending |
| Speed | Fast | Slow |
| Theory | Monetarist | Keynesian |

---

## Chapter 6 quick review

- Treasuries: no credit risk; interest **federally taxable, state/local exempt**; book-entry; $100 minimum; T+1; actual/365 accrual; notes/bonds quoted in 1/32nds.
- Bills ≤ 1 yr (discount); notes 2–10 yrs; bonds 20–30 yrs; TIPS adjust principal for CPI; STRIPS = Treasury zeros; receipts = dealer-created zeros; savings bonds non-negotiable.
- **Ginnie Mae = only agency with full US backing**; MBS pay monthly, taxed at all levels; prepayment risk when rates fall, extension risk when rates rise; CMOs split into tranches (PAC = most predictable).
- Fed = monetary policy (FOMC, 8 meetings/yr). Tools: open-market ops (most used — buy to ease, sell to tighten), discount rate, reserve requirements (least used), interest on reserves.
- Rates: fed funds (overnight bank-to-bank, Fed targets), discount (Fed to banks), prime (banks to best customers), broker call (banks to BDs for margin).
- Recession = 2 consecutive quarters of negative GDP. Leading indicators: stock market, housing starts, M2, new orders, jobless claims. Lagging: unemployment rate, CPI, prime rate.
- Weak dollar helps exporters; strong dollar helps importers.
- Fiscal policy = Congress/President, taxes & spending, Keynesian, slow.
