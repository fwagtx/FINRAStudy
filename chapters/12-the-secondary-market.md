# Chapter 12: The Secondary Market

> Where existing securities trade. Heavy on definitions: agent vs. principal, market makers and specialists/DMMs, the exchanges and OTC, the Securities Exchange Act of 1934, and — most tested — the order types (market, limit, stop, stop-limit) and where they're placed relative to the current price.

---

## 12.1 Agency vs. principal capacity

Every broker-dealer transaction is done in one of two capacities, and the capacity must be disclosed on the customer's **trade confirmation**.

| | **Agency (broker)** | **Principal (dealer)** |
|---|---|---|
| Role | Matches a buyer and seller; acts on **behalf of** the customer | Trades **with** the customer from its **own inventory** |
| Compensation | **Commission** | **Markup** (when selling to the customer) or **markdown** (when buying from the customer) — built into the price |
| Risk | None (no inventory) | Takes a position; bears market risk |
| Disclosure on confirm | Amount of commission; name of the other party available on request | That it acted as principal; markup/markdown amount (now required for most retail corporate/agency/muni bond trades) |

A firm may **not** act as both broker and dealer on the **same trade** (charging a commission *and* a markup is prohibited). The term "broker-dealer" simply means a firm licensed to do either.

- **Riskless principal** — the dealer buys a security to fill a customer order it already has in hand, then resells it to the customer at a markup; treated like an agency trade for disclosure purposes.
- **Markups and markdowns** must be fair and reasonable. FINRA's **5% policy** is a guideline, not a hard cap, considering: type of security, availability, price, dollar amount, disclosure, pattern of markups, and the nature of the firm's business. It applies to secondary market trades, **not** to new issues (prospectus offerings) or mutual funds (where the sales charge is set by the prospectus), and not to securities sold at a stated price from a prospectus.
- **Proceeds transaction** — when a customer sells one security and uses the proceeds to buy another, the firm must treat the two trades as one for markup purposes (not two separate 5%s).

**Market maker.** A dealer that stands ready to buy and sell a specific security at its quoted **bid** and **ask**, providing liquidity. Market makers are principals. On the NYSE, the market maker with special obligations is the **designated market maker (DMM)**; on Nasdaq, multiple competing market makers quote each stock.

---

## 12.2 Roles

| Participant | Function |
|---|---|
| **Retail and institutional investors** | Buyers and sellers of securities. Institutions (mutual funds, pensions, insurers, hedge funds) dominate trading volume. |
| **Broker-dealers** | Execute customer orders (as agent or principal), carry accounts, provide research and advice; must be registered with the SEC and be FINRA members. |
| **Introducing broker** | Takes customer orders and handles the relationship but doesn't hold customer assets; it "introduces" accounts to a… |
| **Clearing (carrying) firm** | Holds customer funds and securities, settles trades, sends confirmations and statements, extends margin. |
| **Market makers / DMMs** | Provide continuous two-sided quotes; DMMs on the NYSE also maintain a fair and orderly market, run the opening/closing auctions, and act as agent for orders left with them (the "book"). |
| **Floor brokers** | NYSE members who execute orders on the floor for their firm's customers or other firms. |
| **Exchanges / ATSs / ECNs** | Venues where orders meet. **Electronic communication networks (ECNs)** match buy and sell orders electronically without a dealer, often used by institutions (the "fourth market") and for after-hours trading. **Dark pools** are private ATSs where large block trades execute without displaying quotes. |
| **Clearing agencies** | **National Securities Clearing Corporation (NSCC)** nets and guarantees trades; **Depository Trust Company (DTC)** holds securities in book-entry form; together they form **DTCC**. **OCC** clears options. |
| **Transfer agents / registrars** | Record ownership changes and ensure share counts. |
| **Custodians / prime brokers** | Hold assets for institutions; prime brokers provide consolidated services to hedge funds. |
| **Regulators** | SEC (oversight), FINRA (member firms and reps), the exchanges themselves (SROs), MSRB (muni rules), state regulators. |
| **Investment advisers** | Give advice for a fee; fiduciaries; registered with the SEC (≥ $100 million AUM) or state. |

**Self-regulatory organizations (SROs).** Membership organizations that regulate their members under SEC oversight: **FINRA**, the exchanges (NYSE, Nasdaq, Cboe), and the **MSRB** (makes rules but doesn't enforce). FINRA is the largest; nearly every broker-dealer must be a member.

---

## 12.3 Bid & ask

A **quote** has two sides:

- **Bid** — the highest price a buyer (market maker) is willing to **pay**. A customer **sells** at the bid.
- **Ask (offer)** — the lowest price a seller (market maker) is willing to **accept**. A customer **buys** at the ask.
- **Spread** = ask − bid. The market maker's profit margin; narrower spreads mean a more liquid security.
- **Size** — the number of shares (in round lots of 100) bid for and offered. "40.10 – 40.15, 10 × 5" means bid $40.10 for 1,000 shares, ask $40.15 for 500 shares.
- **Inside market / NBBO** — the **highest bid and lowest ask** across all market makers and venues; this is the **National Best Bid and Offer**, which firms must use to achieve best execution (Reg NMS order protection rule).

**Types of quotes.**

| Quote type | Meaning |
|---|---|
| **Firm quote** | The dealer must honor it for at least the displayed size (normally 100 shares). Market makers' published quotes are firm. |
| **Subject quote** | Subject to confirmation; not firm. |
| **Nominal quote** | For informational purposes only; must be labeled as such. |
| **Workout quote** | An approximate price for a large/illiquid order the dealer needs time to "work out." |
| **Backing away** | A market maker refusing to honor its firm quote — a violation. |

**Price increments.** Stocks priced $1.00 and above quote in **pennies** ($0.01); sub-$1 stocks can quote in $0.0001. Round lot = **100 shares**; odd lot = fewer than 100.

**Reading a stock table.** Last price, net change from the prior close, high/low, volume; 52-week high/low; dividend and yield; P/E.

---

## 12.4 The markets

The secondary market is traditionally described as four markets:

| Market | Description |
|---|---|
| **First market** | Exchange-listed securities traded **on the exchange** (NYSE, Nasdaq). An auction market with a central order flow. |
| **Second market** | **Unlisted** securities traded **OTC** (OTC Markets Group's OTCQX, OTCQB, Pink). A negotiated dealer market. |
| **Third market** | **Exchange-listed** securities traded **OTC** by non-exchange-member broker-dealers/market makers. |
| **Fourth market** | **Institutions trading directly with each other** without a broker-dealer, through ECNs/ATSs; large blocks. |

### 12.4.1 The New York Stock Exchange

- The largest stock exchange by market cap; a **listed, auction-style** market combining electronic matching with a physical floor. Companies must meet **listing requirements** (earnings, market cap, share price, number of shareholders, corporate governance) and can be **delisted** if they fall short (e.g., share price below $1 for 30 days).
- **Designated market makers (DMMs)** — assigned to each listed stock; obligated to maintain a **fair and orderly market**, supply liquidity when there's an imbalance (buying when others want to sell, and vice versa), set the opening and closing prices, and handle orders left on their book. They act as both dealers (for their own account) and agents (for the book).
- **Floor brokers** execute orders for their firms' customers.
- **Supplemental liquidity providers (SLPs)** add quotes electronically.
- Trading hours: **9:30 am – 4:00 pm ET**; pre-market and after-hours sessions via ECNs.
- **Circuit breakers (market-wide):** based on the S&P 500's decline from the prior close — **Level 1: 7%** → 15-minute halt; **Level 2: 13%** → 15-minute halt (neither applies after 3:25 pm); **Level 3: 20%** → trading halts for the rest of the day. Individual stocks are also subject to the **Limit Up–Limit Down (LULD)** mechanism which pauses trading for 5 minutes if the price moves outside a band.
- **Trading halts** can be imposed for pending news (regulatory halt) or order imbalances.

### 12.4.2 NASDAQ

- Began in 1971 as an electronic quotation system for OTC stocks; now a registered **exchange** with its own listing standards (Global Select, Global, and Capital markets). Home to many technology companies.
- A **dealer (negotiated) market** with **multiple competing market makers** for each stock (no single DMM) and electronic order matching. Market makers must maintain **firm two-sided quotes** during the trading day.
- **Market maker quote levels**: Level 1 (inside bid/ask — what retail sees), Level 2 (every market maker's quotes and size — subscribers and professionals), Level 3 (market makers entering/updating their quotes).
- Trade reporting for Nasdaq-listed and OTC equities goes through FINRA's **trade reporting facilities (TRFs)** and **ORF** within **10 seconds** of execution.
- Nasdaq-listed stocks are also traded OTC by third-market makers and on ECNs.

### 12.4.3 Other OTC markets

- **OTC Markets Group** (formerly the Pink Sheets): quotes for **unlisted** stocks. Tiers: **OTCQX** (best — companies meeting financial standards), **OTCQB** (venture market — must be current in reporting), **Pink Open Market** (anything, including shells and delinquent filers; most "penny stocks" live here), and the **Grey Market** (no quotes at all).
- **OTC Bulletin Board (OTCBB)** — a FINRA-run quotation service for SEC-reporting unlisted companies; now effectively defunct.
- **OTC equity trades** are reported to FINRA's **ORF** (OTC Reporting Facility).
- **Bonds** (corporate, muni, government) trade almost entirely OTC — see Chapters 4–6. Corporate bond trades report to **TRACE**; munis to **RTRS/EMMA**.
- The OTC market is a **negotiated** market: prices are set by negotiation between dealers rather than by a central auction.

### 12.4.4 Chicago Board Options Exchange

- The **Cboe** was founded in 1973 as the first listed options exchange and remains the largest. It lists equity options, index options (SPX, VIX), and options on ETFs.
- Options exchanges use **market makers** and **order book officials** (or electronic equivalents) rather than DMMs; the **Options Clearing Corporation (OCC)** issues and clears every listed option.
- Options trade 9:30 am–4:00 pm ET (some index options until 4:15 pm). The Cboe is also a major equities exchange operator (Cboe BZX, EDGX).
- Other options exchanges: NYSE Arca, NYSE American, Nasdaq PHLX, ISE, BOX, MIAX. Listed options are **fungible** across exchanges because the OCC guarantees them.

**Other exchanges/markets to recognize:** NYSE American (smaller companies), NYSE Arca (ETFs), the **CME Group** (futures and commodities — Chicago Mercantile Exchange, CBOT, NYMEX), regional exchanges, and foreign exchanges (London, Tokyo, Hong Kong).

---

## 12.5 The Securities Exchange Act of 1934

The **"People Act"** or **"Exchange Act."** Where the 1933 Act regulates new issues, the 1934 Act regulates the **secondary market** and the people in it. Key provisions:

- **Created the Securities and Exchange Commission (SEC)** — five commissioners appointed by the President for staggered 5-year terms; no more than three from one party. The SEC enforces all federal securities laws.
- **Registration of broker-dealers** with the SEC and requirement to join an SRO (FINRA). Registration of exchanges, transfer agents, clearing agencies, and associated persons (through FINRA).
- **Registration of exchanges** and recognition of SROs.
- **Periodic reporting by public companies:** **10-K** (annual, audited), **10-Q** (quarterly), **8-K** (material events within 4 business days), proxy statements. These "reporting companies" are those with listed securities or with ≥ $10 million in assets and 2,000+ holders.
- **Proxy rules** — regulate solicitation of shareholder votes (Chapter 15).
- **Insider reporting (Section 16)** — officers, directors and 10%+ holders report trades (Forms 3, 4 within 2 business days, 5) and must disgorge **short-swing profits** (buy/sell within 6 months); may not short their company's stock. **Schedule 13D** must be filed within **5 business days** by anyone acquiring **more than 5%** of a company's equity with intent to influence control; passive investors file 13G.
- **Anti-fraud and anti-manipulation (Section 10(b), Rule 10b-5)** — prohibits any manipulative or deceptive device in connection with buying or selling **any** security (listed or not, exempt or not). This is the basis for **insider trading** prosecutions.
- **Margin regulation** — gives the **Federal Reserve** authority to set margin requirements (**Regulation T**, 50%).
- **Net capital rules** for broker-dealers (financial responsibility) and the **customer protection rule** (segregation of customer assets).
- **Trading rules** — short sale regulation (Reg SHO), prohibition of wash trades and matched orders, rules on trading halts and circuit breakers.
- **Records and reports** — broker-dealers must keep books and records (Rules 17a-3, 17a-4) and file annual audited financials (FOCUS reports).
- Later amendments: the **Maloney Act of 1938** authorized the NASD (now FINRA); the **Securities Investor Protection Act of 1970** created SIPC; the **Insider Trading and Securities Fraud Enforcement Act of 1988** set penalties; **Sarbanes-Oxley (2002)** added CEO/CFO certification of financials and auditor independence; **Dodd-Frank (2010)** reformed derivatives and created the CFPB and FSOC; **Regulation NMS (2005)** created the order protection rule and the NBBO framework.

**Regulation SHO (short sales).** Orders must be marked long or short; a "locate" is required before a short sale; **threshold securities** with persistent fails must be closed out; a **short sale circuit breaker (Rule 201)** restricts short selling at or below the best bid for the rest of the day and the next day when a stock falls **10%** from the prior close.

---

## 12.6 Customer orders

Customer orders instruct the broker how to execute. Know each type, its purpose, and its drawbacks.

### 12.6.1 Market orders

**Execute immediately at the best available price.** Guaranteed **execution**, not price. A market order to buy fills at the current ask; to sell, at the current bid. Most common order type. Risk: in a fast-moving or illiquid market, the fill may be far from the last quote (slippage). Market orders cannot be placed with price conditions and are always "day" orders in practice.

### 12.6.2 Limit orders

**Execute only at the limit price or better.** Guaranteed **price** (if filled), not execution.

- **Buy limit** — placed **below** the current market; fills at the limit or lower. "Buy 100 XYZ at 48 limit" when XYZ is 50.
- **Sell limit** — placed **above** the current market; fills at the limit or higher. "Sell 100 XYZ at 52 limit" when XYZ is 50.

Risks: the order may never fill if the market doesn't reach the price, or may be only partially filled, or may be "stuck" behind other orders at the same price (priority is price, then time). Limit orders on the book contribute to displayed liquidity.

### 12.6.3 Stop orders

A **stop (stop-loss) order** becomes a **market order** when the stock trades at or through the **stop price**. Used mainly to **protect** a position or to enter a position on a breakout.

- **Sell stop** — placed **below** the current market. Protects a **long** position against a decline (or limits the loss). "Sell 100 XYZ at 45 stop" when XYZ is 50: if XYZ trades at 45 or lower, the order is **triggered (elected)** and becomes a market order to sell, filling at the next price — which may be lower than 45.
- **Buy stop** — placed **above** the current market. Protects a **short** position against a rise, or buys a stock once it "breaks out" above resistance. "Buy 100 XYZ at 55 stop."

Two steps: **trigger** (a trade at or through the stop price) and **execution** (the next trade, at whatever price). Stop orders guarantee neither price nor (in a gap) a fill near the stop. In a sharp decline, a sell stop at 45 can execute at 40. Stop orders can accelerate declines (cascading stops).

### 12.6.4 Stop limit orders

A **stop-limit order** becomes a **limit order** (not a market order) once the stop price is triggered. "Sell 100 XYZ at 45 stop, 44 limit": when XYZ trades at 45 or below, a sell limit order at 44 is entered — it will execute only at 44 or higher. Advantage: price control after the trigger. Disadvantage: if the stock gaps through the limit, the order **may never execute**, leaving the investor unprotected (the exact thing a stop-loss was supposed to prevent). The stop and limit prices can be the same.

### 12.6.5 Summary of the order types

| Order | Placed where (relative to market) | Becomes | Guarantees | Typical use |
|---|---|---|---|---|
| **Market** | — | Executes now | Execution | Get in/out immediately |
| **Buy limit** | **Below** market | — | Price | Buy cheaper |
| **Sell limit** | **Above** market | — | Price | Sell higher (take profit) |
| **Buy stop** | **Above** market | Market order when triggered | Neither | Protect a short; buy a breakout |
| **Sell stop** | **Below** market | Market order when triggered | Neither | Protect a long (stop-loss) |
| **Buy stop-limit** | Above | Limit order when triggered | Price (if filled) | Protect short with price control |
| **Sell stop-limit** | Below | Limit order when triggered | Price (if filled) | Protect long with price control |

Memory aid — **BLiSS / SLoBS**: **B**uy **Li**mits and **S**ell **S**tops go **below** the market; **S**ell **L**imits and **B**uy **S**tops go **above**. Orders below the market are reduced on the ex-dividend date; orders above are not.

### 12.6.6 Additional order specifications

| Qualifier | Meaning |
|---|---|
| **Day order** | Expires at the end of the trading day if not filled (the default). |
| **Good-till-cancelled (GTC) / open order** | Stays on the book until filled or cancelled (firms typically require renewal, e.g., quarterly). |
| **Immediate-or-cancel (IOC)** | Execute whatever portion is immediately available; cancel the rest. |
| **Fill-or-kill (FOK)** | Execute the **entire** order immediately or cancel it entirely. |
| **All-or-none (AON)** | Entire order must be filled, but it can wait (no immediacy requirement). |
| **At-the-open / market-on-open** | Execute at or near the opening price; must be in before the open. |
| **At-the-close / market-on-close (MOC)** | Execute at or near the closing price. |
| **Not-held (NH)** | Gives the floor broker discretion over **time and price** only (not over security, action or amount) — not considered a discretionary order requiring written authority. |
| **Do-not-reduce (DNR)** | Open orders below the market (buy limits, sell stops) are normally **reduced by the dividend amount on the ex-date**; DNR prevents this. |
| **Discretionary** | The rep decides the security, action (buy/sell) or amount — requires **written authorization** from the customer and principal approval of each order (Chapter 13). Deciding only time/price is not discretion. |
| **Solicited vs. unsolicited** | Whether the rep recommended the trade; unsolicited orders must be marked and carry less suitability obligation. |
| **Long / short marking** | Every sell order marked long or short (Reg SHO). |

### 12.6.7 Customer order rules

- **Best execution (FINRA Rule 5310).** Firms must use **reasonable diligence** to get the customer the **most favorable terms reasonably available** — price, speed, likelihood of execution — regardless of any payment for order flow the firm receives. Routing to a market with an inferior price is a violation.
- **Payment for order flow** — compensation a firm receives for routing orders to a particular market maker; permitted but must be disclosed (on confirms and in SEC Rule 606 quarterly reports), and cannot override best execution.
- **Order ticket (memorandum)** requirements: account number, security, buy/sell, long/short, size, order type and limits, solicited/unsolicited, discretionary status, time received and time executed, rep ID. Prepared **before** the order is entered. Records retained **3 years**.
- **Trade confirmation** sent at or before **completion of the transaction (settlement)** showing details including capacity, price, commission/markup (Chapter 13).
- **Front-running** — trading ahead of a customer's (or research report's) pending order — prohibited (FINRA Rule 5270).
- **Trading ahead of customer limit orders (Manning rule / Rule 5320)** — a firm holding a customer limit order may not trade for its own account at that price or better without filling the customer first.
- **Order protection (Reg NMS Rule 611)** — a trading center may not execute at a price worse than a better **protected quote** displayed elsewhere ("trade-through").
- **Error correction** — execution errors are handled through the firm's error account with principal approval; reps cannot guarantee a customer against loss or take errors into their own accounts.
- **Prohibited:** marking the close, wash trades, matched orders, spoofing, front-running, interpositioning (inserting an unnecessary third party between the firm and the best market), and backing away (Chapter 15).
- **Regulation SHO marking** — every sell order marked "long" or "short"; locate required for shorts.
- **Trading restrictions during distributions (Reg M)** and **blackout periods** for insiders.

---

## Chapter 12 quick review

- **Agent = commission; principal = markup/markdown.** Never both on one trade. Capacity disclosed on the confirm. 5% policy is a guideline for secondary trades (not new issues or funds).
- Bid = what dealer pays (customer sells); ask = what dealer charges (customer buys); spread = profit. Firm quotes must be honored; backing away is a violation.
- First market = exchange; second = OTC unlisted; third = listed traded OTC; fourth = institution-to-institution via ECNs.
- NYSE: auction, DMMs maintain fair/orderly market. Nasdaq: dealer market, competing market makers, Level 1/2/3. OTC tiers: OTCQX, OTCQB, Pink. Cboe: largest options exchange; OCC clears.
- Circuit breakers: S&P 500 down 7% and 13% → 15-min halt (not after 3:25); 20% → close for the day.
- 1934 Act: created SEC; registers BDs, exchanges, SROs; 10-K/10-Q/8-K; proxy rules; insider (Section 16) and 13D (> 5%); Rule 10b-5 anti-fraud; Fed sets margin (Reg T); Reg SHO.
- **Orders:** market (execution guaranteed), limit (price guaranteed; buy limit below, sell limit above), stop (becomes market when triggered; sell stop below to protect long, buy stop above to protect short), stop-limit (becomes limit — may not execute).
- BLiSS/SLoBS. Orders below the market are reduced on the ex-date unless DNR.
- Day vs. GTC; IOC, FOK, AON; not-held = time/price discretion only; discretionary = written authorization.
- Best execution regardless of payment for order flow; no front-running; Manning rule; order tickets kept 3 years.
