# SIE Practice Question Bank

162 original questions, grouped by chapter. Answers and explanations follow each question. The same questions power the quizzes and timed exams in `app/index.html`; the machine-readable source is `question-bank.json` (fields: `ch` chapter, `sec` section, `fs` FINRA outline section 1–4, `q`, `o` options, `a` answer index, `e` explanation).


---

## Chapter 1: Common stock

**Q1** (§1.1 · FINRA section 2) — A corporation's charter authorizes 10 million shares. It has sold 6 million shares to the public and later repurchased 1 million of them, which it holds as treasury stock. How many shares are outstanding?

- A. 10 million
- B. 6 million
- C. 5 million
- D. 4 million

<details><summary>Answer</summary>

**C.** Outstanding = issued − treasury = 6M − 1M = 5 million. Treasury stock carries no vote and receives no dividends.

</details>

**Q2** (§1.2.2 · FINRA section 2) — An investor owns 200 shares of a company that is electing four directors. Under cumulative voting, the investor may cast:

- A. 200 votes for each of the four seats
- B. 800 votes total, allocated in any way
- C. 50 votes for each seat
- D. 800 votes, but no more than 200 for any one candidate

<details><summary>Answer</summary>

**B.** Cumulative voting gives shares × seats = 800 votes that can be distributed in any way, including all on one candidate. This benefits small shareholders. Statutory voting would be 200 votes per seat.

</details>

**Q3** (§1.2.4 · FINRA section 2) — Which of the following is TRUE of a warrant compared to a stock right?

- A. A warrant is short-term and its exercise price is below market at issuance
- B. A warrant is long-term and its exercise price is above market at issuance
- C. Warrants are issued only to existing shareholders under preemptive rights
- D. Warrants cannot be traded separately from the bond they accompany

<details><summary>Answer</summary>

**B.** Warrants are long-term (often years), issued with an exercise price above the current market, and typically attached to bond or preferred offerings as sweeteners. Rights are short-term, priced below market, and given to existing shareholders.

</details>

**Q4** (§1.3.3 · FINRA section 3) — A customer buys 100 shares of a listed stock on Tuesday, June 3. Under regular-way settlement, the trade settles on:

- A. Tuesday, June 3
- B. Wednesday, June 4
- C. Thursday, June 5
- D. Friday, June 6

<details><summary>Answer</summary>

**B.** Corporate securities settle T+1 — one business day after the trade date. Wednesday, June 4. The Reg T payment deadline would be S+2 (Friday).

</details>

**Q5** (§1.3.4 · FINRA section 2) — A company declares a $0.50 dividend payable to holders of record on Thursday, March 20. To receive the dividend, an investor must purchase the stock no later than:

- A. Tuesday, March 18
- B. Wednesday, March 19
- C. Thursday, March 20
- D. Friday, March 21

<details><summary>Answer</summary>

**B.** Under T+1 settlement the ex-dividend date is the same day as the record date (March 20). To be a holder of record, the purchase must settle by March 20, so the trade must occur by March 19 — the last day before the ex-date.

</details>

**Q6** (§1.3.5 · FINRA section 2) — The maximum potential loss for an investor who sells a stock short is:

- A. The sale proceeds
- B. The margin deposit
- C. Unlimited
- D. The current market value minus the margin deposit

<details><summary>Answer</summary>

**C.** A short seller must eventually buy the stock back, and there is no ceiling on how high a stock can rise, so the loss potential is unlimited. Maximum gain is the sale proceeds (stock goes to zero).

</details>

**Q7** (§1.3.6 · FINRA section 2) — An investor holding an American Depositary Receipt is exposed to all of the following EXCEPT:

- A. Currency risk
- B. Market risk of the foreign company's stock
- C. Having to receive dividends in a foreign currency
- D. Political risk in the foreign country

<details><summary>Answer</summary>

**C.** ADRs are priced in US dollars and pay dividends in US dollars (converted by the depositary bank). The holder still bears currency risk because the conversion rate affects the dollar value.

</details>

**Q8** (§1.2.5 · FINRA section 2) — An investor owns 300 shares of XYZ at $90. XYZ announces a 3-for-2 stock split. After the split the investor will own:

- A. 450 shares at $60
- B. 200 shares at $135
- C. 450 shares at $90
- D. 600 shares at $45

<details><summary>Answer</summary>

**A.** 3-for-2: shares × 3/2 = 450; price × 2/3 = $60. Total value stays $27,000. Ownership percentage is unchanged.

</details>

**Q9** (§1.5 · FINRA section 2) — A company has net income of $8 million, pays $2 million in preferred dividends, and has 3 million common shares outstanding. Its stock trades at $40. The P/E ratio is:

- A. 15
- B. 20
- C. 13.3
- D. 12

<details><summary>Answer</summary>

**B.** EPS = ($8M − $2M) ÷ 3M = $2.00. P/E = $40 ÷ $2 = 20.

</details>

**Q10** (§1.3.7 · FINRA section 3) — A tender offer for a company's shares must remain open for at least:

- A. 10 business days
- B. 20 business days
- C. 30 calendar days
- D. 45 calendar days

<details><summary>Answer</summary>

**B.** SEC rules require tender offers to stay open at least 20 business days. Investors may only tender shares they actually own (net long).

</details>


---

## Chapter 2: Preferred stock

**Q11** (§2.2 · FINRA section 2) — A corporation has $6 cumulative preferred stock outstanding. It paid no preferred dividends in the last two years. Before paying a common dividend this year, it must pay preferred holders:

- A. $6
- B. $12
- C. $18
- D. Nothing — the missed dividends are forfeited

<details><summary>Answer</summary>

**C.** Cumulative preferred accumulates dividends in arrears: two missed years ($12) plus the current year ($6) = $18 per share must be paid before any common dividend.

</details>

**Q12** (§2.1 · FINRA section 2) — When market interest rates rise, the price of a fixed-rate preferred stock will most likely:

- A. Rise
- B. Fall
- C. Stay the same
- D. Rise only if the issuer is highly rated

<details><summary>Answer</summary>

**B.** Preferred pays a fixed dividend, so like a bond its price moves inversely to interest rates. Adjustable-rate preferred is the exception because its dividend resets.

</details>

**Q13** (§2.2 · FINRA section 2) — Which type of preferred stock would an issuer most likely redeem when interest rates fall?

- A. Cumulative
- B. Participating
- C. Callable
- D. Convertible

<details><summary>Answer</summary>

**C.** Issuers call preferred (and bonds) when rates fall so they can reissue at a lower dividend rate. Investors are compensated with a higher stated dividend on callable issues.

</details>

**Q14** (§2.2 · FINRA section 2) — A $100 par preferred stock is convertible at $20 per common share. If the preferred is trading at $110, the parity price of the common stock is:

- A. $20
- B. $22
- C. $25
- D. $5.50

<details><summary>Answer</summary>

**B.** Conversion ratio = $100 ÷ $20 = 5 shares. Parity for the common = $110 ÷ 5 = $22.

</details>

**Q15** (§2.3 · FINRA section 2) — Which investor would benefit MOST from the tax treatment of preferred stock dividends?

- A. A corporation investing excess cash
- B. An individual in the lowest tax bracket
- C. A traditional IRA
- D. A municipal pension fund

<details><summary>Answer</summary>

**A.** Corporations can exclude a large portion of dividends received from other domestic corporations (the dividends-received deduction), making preferred especially attractive to corporate investors.

</details>

**Q16** (§2.2 · FINRA section 2) — Which type of preferred stock has the LEAST interest-rate risk?

- A. Straight preferred
- B. Cumulative preferred
- C. Adjustable-rate preferred
- D. Callable preferred

<details><summary>Answer</summary>

**C.** Because the dividend on adjustable-rate preferred resets with market rates, its price stays close to par and it is far less sensitive to rate changes.

</details>

**Q17** (§2.1 · FINRA section 2) — Compared with common stockholders, preferred stockholders generally have:

- A. Greater voting rights and greater growth potential
- B. Priority in dividends and liquidation but usually no voting rights
- C. Preemptive rights and a maturity date
- D. A legal right to receive dividends each year

<details><summary>Answer</summary>

**B.** Preferred is 'preferred' for dividends and in liquidation (after creditors, before common). It generally has no voting rights, no maturity, and dividends are still not a legal obligation.

</details>

**Q18** (§2.2 · FINRA section 2) — Which feature allows preferred stockholders to receive more than the stated dividend in a very profitable year?

- A. Cumulative
- B. Participating
- C. Convertible
- D. Callable

<details><summary>Answer</summary>

**B.** Participating preferred receives its fixed dividend plus a share of additional dividends when the company does well.

</details>

**Q19** (§2.1 · FINRA section 2) — A 7% preferred stock with a $100 par value is trading at $87.50. Its current yield is:

- A. 7.0%
- B. 8.0%
- C. 6.1%
- D. 8.75%

<details><summary>Answer</summary>

**B.** Annual dividend = 7% × $100 = $7. Current yield = $7 ÷ $87.50 = 8.0%.

</details>

**Q20** (§2.2 · FINRA section 2) — Convertible preferred stock typically pays a dividend that is _____ than non-convertible preferred from the same issuer because _____.

- A. higher; it carries call risk
- B. lower; the conversion feature benefits the investor
- C. higher; it is subordinate to convertible bonds
- D. lower; it has no liquidation preference

<details><summary>Answer</summary>

**B.** Investor-friendly features (convertibility, cumulative, participating) let the issuer pay a lower dividend; issuer-friendly features (callability) require a higher dividend.

</details>


---

## Chapter 3: Debt securities

**Q21** (§3.1 · FINRA section 2) — A corporate bond is quoted at 102 3/8. The dollar price is:

- A. $1,020.38
- B. $1,023.75
- C. $1,002.375
- D. $1,023.00

<details><summary>Answer</summary>

**B.** 102 3/8 = 102.375% of $1,000 par = $1,023.75. Corporates are quoted in eighths; each point is $10.

</details>

**Q22** (§3.5 · FINRA section 2) — A bond with a 5% coupon is trading at $1,100. Which of the following correctly ranks its yields from highest to lowest?

- A. YTC, YTM, CY, nominal
- B. Nominal, CY, YTM, YTC
- C. CY, nominal, YTM, YTC
- D. YTM, YTC, CY, nominal

<details><summary>Answer</summary>

**B.** For a premium bond, nominal > current yield > YTM > YTC. The investor paid more than par and loses the premium, so the 'all-in' yields are lower than the coupon.

</details>

**Q23** (§3.1 · FINRA section 2) — Which bond would experience the GREATEST price decline if interest rates rise 1%?

- A. A 2-year 6% bond
- B. A 10-year 6% bond
- C. A 30-year 6% bond
- D. A 30-year zero-coupon bond

<details><summary>Answer</summary>

**D.** Price volatility increases with longer maturity and lower coupon. A long-term zero-coupon bond has the highest duration and is the most sensitive to rate changes.

</details>

**Q24** (§3.1 · FINRA section 2) — The lowest rating that is still considered investment grade is:

- A. A
- B. BBB
- C. BB
- D. B

<details><summary>Answer</summary>

**B.** BBB (S&P/Fitch) or Baa (Moody's) is the lowest investment-grade tier. Anything below is speculative/high-yield ('junk').

</details>

**Q25** (§3.4 · FINRA section 2) — An investor wants to accumulate exactly $50,000 for a child's college tuition in 12 years and does not want reinvestment risk. The most appropriate investment is:

- A. A 12-year 5% corporate bond
- B. A 12-year zero-coupon bond
- C. A bond mutual fund
- D. A 12-year callable municipal bond

<details><summary>Answer</summary>

**B.** Zero-coupon bonds pay no interim interest, so there is nothing to reinvest; the investor locks in a known maturity value. The annual accretion is taxed unless it's a muni or held in a tax-deferred account.

</details>

**Q26** (§3.4 · FINRA section 2) — An investor who owns a puttable bond would most likely exercise the put when:

- A. Interest rates fall
- B. Interest rates rise
- C. The issuer's credit rating is upgraded
- D. The bond trades at a premium

<details><summary>Answer</summary>

**B.** A put lets the holder sell the bond back at par. When rates rise, bond prices fall, so the holder puts the bond at par and reinvests at the higher rates.

</details>

**Q27** (§3.1 · FINRA section 2) — A corporate bond pays interest on January 1 and July 1. A trade settles on April 16. How many days of accrued interest does the buyer owe the seller?

- A. 105
- B. 106
- C. 104
- D. 107

<details><summary>Answer</summary>

**A.** Corporate bonds use 30/360: January (30) + February (30) + March (30) + April 1–15 (15) = 105 days. Accrued interest runs up to but not including settlement.

</details>

**Q28** (§3.5 · FINRA section 1) — An inverted yield curve exists when:

- A. Long-term rates exceed short-term rates
- B. Short-term rates exceed long-term rates
- C. Corporate yields exceed Treasury yields
- D. All maturities yield approximately the same

<details><summary>Answer</summary>

**B.** An inverted (negative) yield curve has short-term yields above long-term yields, usually from Fed tightening, and historically signals a coming recession.

</details>

**Q29** (§3.4 · FINRA section 2) — Which of the following is TRUE about a callable bond compared to a non-callable bond from the same issuer?

- A. It pays a lower coupon
- B. It is most likely to be called when rates rise
- C. It pays a higher coupon to compensate for call risk
- D. Its yield to call is always higher than its yield to maturity

<details><summary>Answer</summary>

**C.** Callability benefits the issuer (called when rates fall), so investors demand a higher coupon. For a premium bond YTC is lower than YTM.

</details>

**Q30** (§3.3 · FINRA section 1) — Corporate bond transactions must be reported to:

- A. EMMA
- B. TRACE
- C. The Consolidated Tape
- D. RTRS

<details><summary>Answer</summary>

**B.** FINRA's TRACE (Trade Reporting and Compliance Engine) captures corporate bond trades. Municipal trades go to the MSRB's RTRS, displayed on EMMA.

</details>


---

## Chapter 4: Corporate debt

**Q31** (§4.1 · FINRA section 2) — Commercial paper is issued with a maximum maturity of 270 days primarily because:

- A. Banks will not guarantee longer paper
- B. Debt of 270 days or less is exempt from SEC registration
- C. The Fed limits corporate borrowing beyond 270 days
- D. Money market funds cannot buy longer maturities

<details><summary>Answer</summary>

**B.** The Securities Act of 1933 exempts short-term debt with a maturity of 270 days or less from registration, so issuers cap commercial paper at 270 days.

</details>

**Q32** (§4.2 · FINRA section 2) — A bond secured by rolling stock such as railcars or aircraft is known as a(n):

- A. Mortgage bond
- B. Collateral trust bond
- C. Equipment trust certificate
- D. Debenture

<details><summary>Answer</summary>

**C.** Equipment trust certificates are backed by movable equipment held by a trustee; mortgage bonds by real property; collateral trust bonds by securities; debentures are unsecured.

</details>

**Q33** (§4.3 · FINRA section 2) — A $1,000 bond is convertible at $40. The common stock is trading at $45. The parity price of the bond is:

- A. $1,000
- B. $1,125
- C. $1,111
- D. $900

<details><summary>Answer</summary>

**B.** Conversion ratio = 1,000 ÷ 40 = 25 shares. Parity = 25 × $45 = $1,125.

</details>

**Q34** (§4.4 · FINRA section 2) — In a corporate liquidation, which claim is paid FIRST?

- A. Subordinated debentures
- B. Preferred stock
- C. Secured bonds
- D. General creditors

<details><summary>Answer</summary>

**C.** Order: secured creditors → general (unsecured) creditors → subordinated debentures → preferred → common.

</details>

**Q35** (§4.1 · FINRA section 2) — A banker's acceptance is most commonly used to finance:

- A. Corporate payroll
- B. Import and export transactions
- C. Municipal construction projects
- D. Margin lending to broker-dealers

<details><summary>Answer</summary>

**B.** BAs are bank-guaranteed time drafts used in international trade; they trade at a discount with maturities up to 270 days.

</details>

**Q36** (§4.7 · FINRA section 2) — A US corporation issues dollar-denominated bonds in London that are not registered with the SEC. These are:

- A. Yankee bonds
- B. Eurodollar bonds
- C. Treasury receipts
- D. Brady bonds

<details><summary>Answer</summary>

**B.** Eurodollar bonds are USD-denominated bonds issued outside the US; they're unregistered and usually pay interest annually. A Yankee bond is a foreign issuer's dollar bond sold and registered in the US.

</details>

**Q37** (§4.2 · FINRA section 2) — Which corporate bond trades 'flat' (without accrued interest)?

- A. A first-mortgage bond
- B. An income (adjustment) bond
- C. A convertible debenture
- D. An equipment trust certificate

<details><summary>Answer</summary>

**B.** Income bonds pay interest only if the company earns enough, so they trade flat. Bonds in default also trade flat.

</details>

**Q38** (§4.6 · FINRA section 2) — A negotiable certificate of deposit differs from a regular bank CD in that it:

- A. Is not FDIC insured
- B. Can be sold in the secondary market before maturity
- C. Has a minimum denomination of $1,000
- D. Pays interest monthly

<details><summary>Answer</summary>

**B.** Negotiable (jumbo) CDs are $100,000+ and can be traded before maturity, so there's no early-withdrawal penalty but the holder faces interest-rate risk. FDIC coverage still applies up to $250,000.

</details>

**Q39** (§4.3 · FINRA section 2) — A corporation would most likely force conversion of its convertible bonds by:

- A. Lowering the conversion price
- B. Calling the bonds when the stock is trading above parity
- C. Suspending interest payments
- D. Issuing additional common stock

<details><summary>Answer</summary>

**B.** If the bond is called at a price below its conversion value, holders will convert rather than accept the call price — eliminating the issuer's debt.

</details>

**Q40** (§4.2 · FINRA section 2) — Interest paid on corporate bonds is attractive to the issuing corporation compared with dividends on stock because:

- A. Interest is tax-deductible to the corporation; dividends are not
- B. Interest payments are optional
- C. Bondholders have voting rights
- D. Interest is tax-free to the bondholder

<details><summary>Answer</summary>

**A.** Interest expense reduces taxable income; dividends are paid from after-tax profits. This makes debt a cheaper source of capital, but it adds leverage and a fixed obligation.

</details>


---

## Chapter 5: Municipal debt

**Q41** (§5.1 · FINRA section 2) — An investor in the 35% federal tax bracket is comparing a municipal bond yielding 4.2% with a corporate bond. The corporate bond must yield at least approximately:

- A. 5.67%
- B. 6.46%
- C. 2.73%
- D. 4.20%

<details><summary>Answer</summary>

**B.** Tax-equivalent yield = 4.2% ÷ (1 − 0.35) = 4.2% ÷ 0.65 = 6.46%.

</details>

**Q42** (§5.2 · FINRA section 2) — Which of the following is TRUE of general obligation bonds but NOT revenue bonds?

- A. They are backed by user fees from a specific project
- B. They are usually subject to voter approval and statutory debt limits
- C. They require a feasibility study
- D. They are exempt from federal taxation

<details><summary>Answer</summary>

**B.** G.O. bonds pledge the issuer's taxing power, so they typically need voter approval and are subject to debt limits. Revenue bonds rely on a project's revenue and a feasibility study.

</details>

**Q43** (§5.4 · FINRA section 2) — A municipality issues short-term notes to be repaid from the proceeds of a long-term bond issue it plans to sell next year. These are:

- A. Tax anticipation notes
- B. Revenue anticipation notes
- C. Bond anticipation notes
- D. Grant anticipation notes

<details><summary>Answer</summary>

**C.** BANs are interim financing paid off by a future bond sale. TANs come from future taxes; RANs from future non-tax revenue; GANs from expected grants.

</details>

**Q44** (§5.1 · FINRA section 2) — Interest from which of the following municipal bonds may be subject to the alternative minimum tax?

- A. General obligation bonds
- B. Public housing authority bonds
- C. Private activity (industrial development) bonds
- D. Pre-refunded bonds

<details><summary>Answer</summary>

**C.** Private activity bonds — those that primarily benefit a private entity, such as industrial development bonds — are AMT preference items.

</details>

**Q45** (§5.5 · FINRA section 4) — The MSRB's authority is best described as:

- A. Making and enforcing rules for municipal issuers
- B. Making rules for municipal dealers, which are enforced by FINRA, the SEC and bank regulators
- C. Registering municipal securities with the SEC
- D. Insuring municipal bonds against default

<details><summary>Answer</summary>

**B.** The MSRB writes rules for broker-dealers, bank dealers and municipal advisors but has no enforcement power and no jurisdiction over issuers.

</details>

**Q46** (§5.5 · FINRA section 4) — Under MSRB Rule G-37, a municipal finance professional who contributes $500 to the campaign of a mayoral candidate for whom she is entitled to vote will cause her firm to be:

- A. Fined $500
- B. Banned from negotiated underwriting with that issuer for two years
- C. Required to disclose the contribution on EMMA only
- D. Unaffected, because she can vote for the candidate

<details><summary>Answer</summary>

**B.** The de minimis exception is $250 per election for candidates the MFP can vote for. A $500 contribution exceeds it and triggers the two-year ban on negotiated business with that issuer.

</details>

**Q47** (§5.6 · FINRA section 2) — Which account is LEAST appropriate for municipal bonds?

- A. A taxable brokerage account of a high-income investor
- B. A corporate cash management account
- C. A traditional IRA
- D. A joint account of a retired couple in a high bracket

<details><summary>Answer</summary>

**C.** Muni interest is already tax-exempt; inside a tax-deferred IRA the benefit is wasted and withdrawals become taxable ordinary income. Munis yield less than taxable bonds, so the investor loses.

</details>

**Q48** (§5.3 · FINRA section 2) — A revenue bond's debt service coverage ratio of 1.8 means:

- A. Debt service is 1.8 times net revenue
- B. Net revenue is 1.8 times the annual principal and interest
- C. The bond is rated 1.8 notches above investment grade
- D. The issuer may borrow 1.8 times its current debt

<details><summary>Answer</summary>

**B.** Coverage ratio = net revenue available ÷ annual debt service. 1.8 means revenue covers debt service 1.8 times — higher is safer.

</details>

**Q49** (§5.1 · FINRA section 2) — A resident of Texas buys a bond issued by the Commonwealth of Puerto Rico. The interest is:

- A. Subject to federal tax but exempt from Texas tax
- B. Exempt from federal tax only
- C. Exempt from federal, state and local taxes
- D. Fully taxable

<details><summary>Answer</summary>

**C.** Bonds of US territories (Puerto Rico, Guam, USVI) are triple tax-exempt for investors in every state.

</details>

**Q50** (§5.5 · FINRA section 1) — A municipal G.O. bond issue is most commonly awarded through:

- A. A negotiated underwriting
- B. A competitive bid based on the lowest net interest cost
- C. A best-efforts offering
- D. A private placement under Regulation D

<details><summary>Answer</summary>

**B.** G.O. issues typically publish a notice of sale and award the bonds to the syndicate with the lowest NIC/TIC. Revenue bonds are usually negotiated.

</details>


---

## Chapter 6: US government debt

**Q51** (§6.1 · FINRA section 2) — Interest earned on US Treasury notes is:

- A. Exempt from federal tax, taxable at the state level
- B. Taxable at the federal level, exempt from state and local tax
- C. Exempt at all levels
- D. Taxable at all levels

<details><summary>Answer</summary>

**B.** Treasury interest is subject to federal income tax but exempt from state and local tax — the opposite of municipal bonds.

</details>

**Q52** (§6.2 · FINRA section 2) — A Treasury note is quoted at 98.24. Its dollar price is:

- A. $982.40
- B. $987.50
- C. $982.75
- D. $998.24

<details><summary>Answer</summary>

**B.** Treasury notes and bonds are quoted in 32nds: 98.24 = 98 24/32 = 98.75% of $1,000 = $987.50.

</details>

**Q53** (§6.3 · FINRA section 2) — Which agency's mortgage-backed securities are backed by the full faith and credit of the US government?

- A. Fannie Mae
- B. Freddie Mac
- C. Ginnie Mae
- D. Federal Home Loan Banks

<details><summary>Answer</summary>

**C.** Only GNMA pass-throughs carry the direct full-faith-and-credit backing of the US government. Fannie and Freddie are GSEs with implied support.

</details>

**Q54** (§6.3 · FINRA section 2) — The holder of a mortgage-backed pass-through certificate is most exposed to prepayment risk when:

- A. Interest rates rise
- B. Interest rates fall
- C. Housing prices fall
- D. The Fed sells Treasuries

<details><summary>Answer</summary>

**B.** When rates fall, homeowners refinance, returning principal early that must be reinvested at lower rates. Rising rates cause extension risk instead.

</details>

**Q55** (§6.5.3 · FINRA section 1) — To stimulate a slowing economy, the Federal Open Market Committee would most likely:

- A. Sell Treasury securities
- B. Raise the discount rate
- C. Buy Treasury securities
- D. Raise reserve requirements

<details><summary>Answer</summary>

**C.** Buying securities injects money into the banking system, increasing reserves and pushing interest rates down (easy money). Selling, raising rates or raising reserve requirements tighten.

</details>

**Q56** (§6.5.2 · FINRA section 1) — The rate that banks charge each other for overnight loans of excess reserves is the:

- A. Discount rate
- B. Prime rate
- C. Federal funds rate
- D. Broker call rate

<details><summary>Answer</summary>

**C.** The fed funds rate is bank-to-bank overnight. The discount rate is what the Fed charges banks; prime is what banks charge top customers; broker call is what banks charge broker-dealers for margin loans.

</details>

**Q57** (§6.5.4 · FINRA section 1) — Which of the following is considered a LEADING economic indicator?

- A. The unemployment rate
- B. The Consumer Price Index
- C. Building permits
- D. Corporate profits

<details><summary>Answer</summary>

**C.** Building permits/housing starts, the stock market, M2, new orders and initial jobless claims lead the economy. Unemployment rate, CPI and corporate profits lag.

</details>

**Q58** (§6.5.5 · FINRA section 1) — Fiscal policy is set by:

- A. The Federal Reserve Board
- B. The Federal Open Market Committee
- C. Congress and the President
- D. The Treasury Department acting alone

<details><summary>Answer</summary>

**C.** Fiscal policy — taxation and government spending — comes from Congress and the President. The Fed controls monetary policy.

</details>

**Q59** (§6.2 · FINRA section 2) — An investor concerned about inflation who wants a Treasury security whose principal adjusts with the CPI should buy:

- A. Treasury STRIPS
- B. Treasury bills
- C. TIPS
- D. Series EE bonds

<details><summary>Answer</summary>

**C.** Treasury Inflation-Protected Securities adjust principal with CPI; the fixed coupon rate is applied to the adjusted principal.

</details>

**Q60** (§6.5.4 · FINRA section 1) — A weakening US dollar would most directly benefit:

- A. US importers
- B. US consumers buying foreign goods
- C. US exporters
- D. Foreign investors holding US bonds

<details><summary>Answer</summary>

**C.** A weak dollar makes US goods cheaper abroad, helping exporters; it hurts importers and consumers of foreign goods, and reduces the home-currency value of US assets held by foreigners.

</details>


---

## Chapter 7: Investment companies

**Q61** (§7.3.3 · FINRA section 2) — A mutual fund has a NAV of $18.60 and a sales charge of 7%. Its public offering price is:

- A. $19.90
- B. $20.00
- C. $19.30
- D. $17.30

<details><summary>Answer</summary>

**B.** POP = NAV ÷ (1 − 0.07) = 18.60 ÷ 0.93 = $20.00. The sales charge is a percentage of the POP.

</details>

**Q62** (§7.3.3 · FINRA section 3) — A customer signs a letter of intent to invest $50,000 in a fund family over the next 13 months. Which statement is TRUE?

- A. The letter may be backdated up to 90 days to include a prior purchase
- B. Appreciation in the account counts toward the $50,000
- C. The reduced sales charge applies only after $50,000 has been invested
- D. The customer is legally obligated to complete the purchases

<details><summary>Answer</summary>

**A.** An LOI can be backdated 90 days, gives the reduced charge immediately, counts only new money (not appreciation), and is not binding — unmet LOIs trigger a retroactive charge on escrowed shares.

</details>

**Q63** (§7.3.5 · FINRA section 3) — A customer wants to invest $750,000 in a mutual fund and hold it for 15 years. The MOST suitable share class is:

- A. Class A
- B. Class B
- C. Class C
- D. Class B, converting to A later

<details><summary>Answer</summary>

**A.** Large amounts qualify for breakpoints (possibly a 0% load at $1 million) and long holding periods favor the low 12b-1 fee of Class A. Class B has no breakpoints; Class C's level load never converts.

</details>

**Q64** (§7.3.6 · FINRA section 2) — Under Subchapter M, a regulated investment company avoids tax on income distributed to shareholders if it distributes at least:

- A. 50% of net investment income
- B. 75% of net investment income
- C. 90% of net investment income
- D. 100% of net investment income

<details><summary>Answer</summary>

**C.** The 90% conduit rule: distribute at least 90% of net investment income and the fund is taxed only on what it retains.

</details>

**Q65** (§7.4 · FINRA section 2) — Which of the following is TRUE of a closed-end fund but NOT an open-end fund?

- A. It is priced at NAV plus a sales charge
- B. It may trade at a discount to NAV
- C. It continuously issues new shares
- D. It must redeem shares within seven days

<details><summary>Answer</summary>

**B.** Closed-end funds trade in the secondary market at prices set by supply and demand, so they can trade above or below NAV. They don't issue new shares continuously or redeem shares.

</details>

**Q66** (§7.5.2 · FINRA section 2) — A leveraged ETF that seeks 3× the daily return of an index is LEAST suitable for:

- A. A day trader
- B. A buy-and-hold retirement investor
- C. A hedge fund
- D. A sophisticated speculator with a one-day outlook

<details><summary>Answer</summary>

**B.** Leveraged and inverse ETFs reset daily; over longer periods compounding causes returns to diverge from 3× the index, especially in volatile markets. They're designed for short-term trading.

</details>

**Q67** (§7.5.3 · FINRA section 2) — An exchange-traded note differs from an ETF in that the ETN holder:

- A. Receives dividends from the underlying stocks
- B. Bears the credit risk of the issuing bank
- C. Can only redeem through the fund
- D. Pays a front-end sales charge

<details><summary>Answer</summary>

**B.** An ETN is an unsecured debt obligation of a bank; there is no portfolio. If the bank fails, the ETN can become worthless regardless of the index.

</details>

**Q68** (§7.6 · FINRA section 2) — A unit investment trust differs from a mutual fund in that a UIT:

- A. Has a board of directors
- B. Has a fixed, unmanaged portfolio and no investment adviser
- C. Issues shares that trade on an exchange
- D. Cannot hold bonds

<details><summary>Answer</summary>

**B.** UITs hold a fixed portfolio with no active management or board; units are redeemable, and the trust terminates on a set date.

</details>

**Q69** (§7.7 · FINRA section 2) — A fund has a beta of 1.3. If the market rises 10%, the fund would be expected to:

- A. Rise about 13%
- B. Rise about 7.7%
- C. Rise about 10%
- D. Fall about 3%

<details><summary>Answer</summary>

**A.** Beta measures movement relative to the market (beta 1.0). A beta of 1.3 implies about 1.3 × 10% = 13%.

</details>

**Q70** (§7.3.4 · FINRA section 3) — A mutual fund shareholder elects to reinvest all dividends and capital gains distributions. For tax purposes, the distributions are:

- A. Not taxable until shares are sold
- B. Taxable in the year received and added to cost basis
- C. Taxable only if taken in cash
- D. Taxed as long-term gains regardless of type

<details><summary>Answer</summary>

**B.** Distributions are taxable whether reinvested or not; reinvested amounts increase the investor's cost basis to avoid double taxation on sale.

</details>

**Q71** (§7.1 · FINRA section 2) — A diversified management company must have at least 75% of its assets invested such that no more than ___ is in any one issuer and it owns no more than ___ of any issuer's voting securities.

- A. 10%; 5%
- B. 5%; 10%
- C. 25%; 10%
- D. 5%; 25%

<details><summary>Answer</summary>

**B.** The 75-5-10 test: 75% of assets diversified, no more than 5% in one issuer, no more than 10% of an issuer's voting shares.

</details>

**Q72** (§7.3.3 · FINRA section 3) — A registered representative recommends that a customer invest $24,000 in Fund X and $24,000 in Fund Y, from two different fund families, when each family offers a breakpoint at $25,000. This is:

- A. Appropriate diversification
- B. A prohibited breakpoint sale
- C. Acceptable if the customer signs a waiver
- D. Acceptable because each purchase is below the breakpoint

<details><summary>Answer</summary>

**B.** Splitting purchases to keep each below a breakpoint (or selling just under one) to earn higher commissions is a prohibited breakpoint sale.

</details>


---

## Chapter 8: Alternative pooled investments

**Q73** (§8.1 · FINRA section 2) — Which of the following is TRUE of a real estate investment trust?

- A. It passes through both income and losses to shareholders
- B. It must distribute at least 90% of its taxable income to avoid corporate tax
- C. It is regulated under the Investment Company Act of 1940
- D. Its dividends are always taxed as qualified dividends

<details><summary>Answer</summary>

**B.** REITs distribute 90%+ of income and hold 75%+ in real estate to avoid corporate tax. They pass through income but NOT losses, are not 1940 Act companies, and dividends are generally ordinary income.

</details>

**Q74** (§8.2 · FINRA section 2) — Hedge funds are typically offered as:

- A. Registered public offerings with a prospectus
- B. Private placements under Regulation D to accredited investors
- C. Exchange-listed closed-end funds
- D. Unit investment trusts

<details><summary>Answer</summary>

**B.** Hedge funds are privately offered limited partnerships sold under Reg D to accredited investors, exempt from the 1940 Act, with lock-ups and limited disclosure.

</details>

**Q75** (§8.3 · FINRA section 2) — In a limited partnership, which party has unlimited personal liability for the partnership's debts?

- A. The limited partners
- B. The general partner
- C. The subscription agent
- D. All partners equally

<details><summary>Answer</summary>

**B.** The general partner manages the business and has unlimited liability; limited partners are liable only for their investment as long as they stay passive.

</details>

**Q76** (§8.3 · FINRA section 2) — The most significant risk of investing in a direct participation program is generally:

- A. Interest-rate risk
- B. Lack of liquidity
- C. Currency risk
- D. Reinvestment risk

<details><summary>Answer</summary>

**B.** DPP interests have no real secondary market; transfers usually need GP approval and holding periods are long. Illiquidity is the primary risk.

</details>

**Q77** (§8.3 · FINRA section 3) — Losses from a limited partnership may be used by an investor to offset:

- A. Wages and salary
- B. Interest and dividends
- C. Income from other passive activities
- D. Capital gains on stock

<details><summary>Answer</summary>

**C.** DPP losses are passive losses, which may offset only passive income (other DPPs, rental activities), never earned or portfolio income.

</details>

**Q78** (§8.3 · FINRA section 2) — Which oil and gas program carries the HIGHEST risk?

- A. Income program
- B. Developmental program
- C. Exploratory (wildcat) program
- D. Combination program

<details><summary>Answer</summary>

**C.** Exploratory programs drill in unproven areas — the highest chance of dry holes but the largest potential reward. Income programs buy producing wells (lowest risk).

</details>

**Q79** (§8.2 · FINRA section 2) — The 'high-water mark' in a hedge fund refers to:

- A. The maximum leverage the fund may use
- B. The level above which performance fees are charged only on new gains
- C. The minimum investment required
- D. The lock-up period

<details><summary>Answer</summary>

**B.** With a high-water mark, the manager earns the incentive fee only when the fund's value exceeds its previous peak, preventing fees on recovered losses.

</details>

**Q80** (§8.1 · FINRA section 2) — A non-traded REIT compared to an exchange-listed REIT generally has:

- A. Greater liquidity and lower fees
- B. Less liquidity and higher upfront fees
- C. The same liquidity but better tax treatment
- D. No SEC registration

<details><summary>Answer</summary>

**B.** Non-traded REITs are SEC-registered but don't trade on exchanges; redemption programs are limited, and upfront commissions and fees are high.

</details>


---

## Chapter 9: Options

**Q81** (§9.3.1 · FINRA section 2) — An investor buys 1 ABC Jun 50 call at 4. The breakeven point and maximum loss are:

- A. $46; $400
- B. $54; $400
- C. $54; unlimited
- D. $50; $4

<details><summary>Answer</summary>

**B.** Call breakeven = strike + premium = 54. Maximum loss for any option buyer = premium = 4 × 100 = $400. Maximum gain is unlimited.

</details>

**Q82** (§9.3.2 · FINRA section 2) — The maximum potential loss for the writer of an uncovered (naked) call is:

- A. The premium received
- B. The strike price minus the premium
- C. The strike price plus the premium
- D. Unlimited

<details><summary>Answer</summary>

**D.** A naked call writer must deliver stock they don't own; since a stock can rise without limit, the loss is unlimited. This is the riskiest basic option position.

</details>

**Q83** (§9.2.2 · FINRA section 2) — XYZ stock is trading at $62. An XYZ 55 put is trading at 1. Which statement is TRUE?

- A. The put is in the money by 7 points
- B. The put has 1 point of intrinsic value
- C. The put has no intrinsic value and 1 point of time value
- D. The put is at the money

<details><summary>Answer</summary>

**C.** A put is in the money only when the stock is below the strike. At $62 vs. a 55 strike, the put is out of the money; the entire premium is time value.

</details>

**Q84** (§9.3.5 · FINRA section 2) — An investor who is long 100 shares of stock wants to protect against a decline while keeping unlimited upside. The BEST strategy is to:

- A. Write a call
- B. Buy a call
- C. Buy a put
- D. Write a put

<details><summary>Answer</summary>

**C.** A protective put locks in a minimum sale price (the strike) at the cost of the premium while leaving the upside intact. Writing a call provides only limited downside protection and caps the upside.

</details>

**Q85** (§9.3.6 · FINRA section 2) — An investor owns 100 shares of ABC purchased at $42 and writes 1 ABC 45 call at 2. Maximum gain is:

- A. $200
- B. $300
- C. $500
- D. Unlimited

<details><summary>Answer</summary>

**C.** Covered call max gain = (strike − cost) + premium = (45 − 42) + 2 = 5 points = $500. The stock is called away at 45.

</details>

**Q86** (§9.2.4 · FINRA section 2) — An investor holds 1 XYZ 80 call. XYZ declares a 2-for-1 stock split. After adjustment the investor holds:

- A. 1 XYZ 40 call for 200 shares
- B. 2 XYZ 40 calls for 100 shares each
- C. 2 XYZ 80 calls for 100 shares each
- D. 1 XYZ 80 call for 200 shares

<details><summary>Answer</summary>

**B.** Even splits multiply the number of contracts and divide the strike; each contract still covers 100 shares. Uneven splits instead change the shares per contract.

</details>

**Q87** (§9.3.7 · FINRA section 2) — Which of the following is TRUE of broad-based index options?

- A. Exercise results in delivery of the underlying stocks
- B. They are settled in cash
- C. They are always American style
- D. They settle T+2

<details><summary>Answer</summary>

**B.** Index options settle in cash (the in-the-money amount × $100) the next business day; most are European style.

</details>

**Q88** (§9.2.1 · FINRA section 1) — Listed options are issued and guaranteed by:

- A. The Cboe
- B. FINRA
- C. The Options Clearing Corporation
- D. The underlying corporation

<details><summary>Answer</summary>

**C.** The OCC is the issuer and guarantor of all listed options, standing between every buyer and seller.

</details>

**Q89** (§9.3.4 · FINRA section 2) — An investor writes 1 DEF 30 put at 3. The maximum loss is:

- A. $300
- B. $2,700
- C. $3,000
- D. Unlimited

<details><summary>Answer</summary>

**B.** Put writer max loss = (strike − premium) × 100 = (30 − 3) × 100 = $2,700; the stock can only fall to zero.

</details>

**Q90** (§9.3.3 · FINRA section 2) — An investor who is bearish on a stock but wants limited risk should:

- A. Sell the stock short
- B. Buy a put
- C. Write a call
- D. Write a put

<details><summary>Answer</summary>

**B.** A long put profits from a decline with loss limited to the premium. Short sales and naked calls have unlimited risk; writing a put is bullish.

</details>


---

## Chapter 10: Taxes

**Q91** (§10.3 · FINRA section 3) — An investor has $12,000 in long-term capital gains and $20,000 in short-term capital losses this year. The investor may:

- A. Deduct $8,000 against ordinary income this year
- B. Deduct $3,000 against ordinary income and carry forward $5,000
- C. Deduct $20,000 against ordinary income
- D. Carry forward the entire $8,000

<details><summary>Answer</summary>

**B.** Net loss = $8,000. Up to $3,000 of net capital loss is deductible against ordinary income each year; the remaining $5,000 carries forward.

</details>

**Q92** (§10.3 · FINRA section 3) — An investor sells XYZ at a loss on March 10 and buys XYZ call options on March 25. For tax purposes:

- A. The loss is fully deductible
- B. The loss is disallowed under the wash sale rule
- C. The loss is deductible only against gains in XYZ
- D. The loss is converted to a long-term loss

<details><summary>Answer</summary>

**B.** Buying the same or a substantially identical security — including options or convertibles on it — within 30 days before or after a loss sale is a wash sale; the loss is added to the new position's basis.

</details>

**Q93** (§10.3 · FINRA section 3) — A father gives his daughter 100 shares of stock he bought at $20 when it is worth $50. She sells it a month later for $55. Her taxable gain is:

- A. $500 short-term
- B. $3,500 short-term
- C. $3,500 long-term (if the father held it more than a year)
- D. $0 — gifts are not taxable to the recipient

<details><summary>Answer</summary>

**C.** Gifted securities carry over the donor's basis ($20) and holding period. Gain = $55 − $20 = $35 × 100 = $3,500, long-term if the combined holding period exceeds a year.

</details>

**Q94** (§10.3 · FINRA section 3) — An investor inherits stock that the deceased bought for $10,000 and that was worth $40,000 on the date of death. The investor's cost basis is:

- A. $10,000
- B. $40,000
- C. $25,000
- D. $0

<details><summary>Answer</summary>

**B.** Inherited securities receive a stepped-up basis to the fair market value at death, and the holding period is automatically long-term.

</details>

**Q95** (§10.2 · FINRA section 3) — The annual accretion on a corporate zero-coupon bond held in a taxable account is:

- A. Not taxable until maturity
- B. Taxed each year as interest income even though no cash is received
- C. Taxed as a capital gain at maturity
- D. Exempt from federal tax

<details><summary>Answer</summary>

**B.** Original issue discount accretes annually and is taxed as 'phantom' interest income. Municipal zeros are the exception (tax-exempt). Hold corporate zeros in tax-deferred accounts.

</details>

**Q96** (§10.1 · FINRA section 3) — Qualified dividends are taxed at:

- A. Ordinary income rates
- B. The long-term capital gains rates
- C. A flat 28%
- D. The investor's state rate only

<details><summary>Answer</summary>

**B.** Qualified dividends (from US corporations, with the holding period met) are taxed at the 0/15/20% long-term capital gains rates. REIT and money-market dividends are ordinary.

</details>

**Q97** (§10.4 · FINRA section 3) — Which type of income is required for an individual to make an IRA contribution?

- A. Portfolio income
- B. Passive income
- C. Earned income
- D. Any taxable income

<details><summary>Answer</summary>

**C.** IRA contributions require earned income (wages, salary, self-employment). Interest, dividends, capital gains, pensions and rental income don't qualify.

</details>

**Q98** (§10.3 · FINRA section 3) — A long-term capital gain requires a holding period of:

- A. At least 6 months
- B. At least one year
- C. More than one year
- D. More than 18 months

<details><summary>Answer</summary>

**C.** More than one year (one year and a day). One year or less is short-term, taxed as ordinary income.

</details>

**Q99** (§10.4 · FINRA section 3) — A customer refuses to provide a Social Security number when opening an account. The firm must:

- A. Refuse all trading
- B. Apply backup withholding of 24% on dividends, interest and sale proceeds
- C. Report the customer to the SEC
- D. Close the account within 30 days

<details><summary>Answer</summary>

**B.** Without a taxpayer ID (Form W-9), the IRS requires backup withholding at 24%.

</details>

**Q100** (§10.3 · FINRA section 3) — If an investor who bought shares at several different prices does not specify which shares to sell, the IRS assumes:

- A. Average cost
- B. Highest cost first
- C. First-in, first-out
- D. Last-in, first-out

<details><summary>Answer</summary>

**C.** FIFO is the default; specific identification lets the investor choose lots; average cost is allowed for mutual funds.

</details>


---

## Chapter 11: The primary market

**Q101** (§11.2 · FINRA section 1) — In a firm commitment underwriting, the underwriters act as:

- A. Agents, earning a commission with no risk
- B. Principals, buying the issue from the issuer and bearing the risk of unsold shares
- C. Brokers for the issuer under an escrow arrangement
- D. Trustees under the Trust Indenture Act

<details><summary>Answer</summary>

**B.** Firm commitment = underwriters buy the entire issue and resell it; unsold shares are their problem. Best efforts = agents; issuer bears the risk.

</details>

**Q102** (§11.4.1 · FINRA section 1) — During the cooling-off period, an underwriter may:

- A. Accept orders and payment from customers
- B. Distribute a preliminary prospectus and take indications of interest
- C. Send sales literature highlighting the offering
- D. Guarantee allocations to favored customers

<details><summary>Answer</summary>

**B.** During the cooling-off period (at least 20 days) the red herring may be distributed, tombstone ads run, and non-binding indications of interest collected. No sales, orders, money or sales literature.

</details>

**Q103** (§11.4.3 · FINRA section 1) — When the SEC declares a registration statement effective, it means the SEC:

- A. Has approved the security as a sound investment
- B. Has verified the accuracy of all statements in the prospectus
- C. Has found the registration statement complete
- D. Guarantees the offering price

<details><summary>Answer</summary>

**C.** The SEC reviews for completeness only; it never approves or passes on the merits or accuracy. Saying the SEC 'approved' an issue is a violation.

</details>

**Q104** (§11.4.4 · FINRA section 1) — Under Rule 506(b) of Regulation D, an issuer may sell to:

- A. No more than 35 accredited investors
- B. An unlimited number of accredited investors and up to 35 non-accredited investors
- C. Only qualified institutional buyers
- D. An unlimited number of any investors if the offering is under $5 million

<details><summary>Answer</summary>

**B.** 506(b): unlimited accredited investors plus up to 35 sophisticated non-accredited investors, unlimited dollar amount, no general solicitation.

</details>

**Q105** (§11.4.4 · FINRA section 1) — An individual qualifies as an accredited investor with a net worth of at least _____ (excluding primary residence) or income of at least _____ in each of the last two years.

- A. $500,000; $100,000
- B. $1 million; $200,000 ($300,000 joint)
- C. $5 million; $250,000
- D. $1 million including primary residence; $150,000

<details><summary>Answer</summary>

**B.** Net worth over $1 million excluding the primary residence, or income over $200,000 individually / $300,000 with a spouse.

</details>

**Q106** (§11.5 · FINRA section 1) — A corporate officer wishes to sell shares under Rule 144. The company has 50 million shares outstanding; average weekly volume over the last four weeks was 600,000 shares. The maximum she may sell in a 90-day period is:

- A. 500,000 shares
- B. 600,000 shares
- C. 50,000 shares
- D. There is no limit for officers

<details><summary>Answer</summary>

**B.** The limit is the greater of 1% of outstanding (500,000) or the four-week average weekly volume (600,000) — so 600,000 shares.

</details>

**Q107** (§11.4.3 · FINRA section 4) — Under FINRA Rule 5130, which of the following may purchase shares of a new issue of common stock (IPO)?

- A. A registered representative at another broker-dealer
- B. The spouse of a FINRA member firm employee
- C. A retired schoolteacher with no industry connections
- D. A finder in the offering

<details><summary>Answer</summary>

**C.** Restricted persons include FINRA members, their employees, immediate family members, finders and certain fiduciaries. The schoolteacher is not restricted.

</details>

**Q108** (§11.4.4 · FINRA section 1) — Which of the following securities is EXEMPT from registration under the Securities Act of 1933?

- A. A variable annuity
- B. A corporate debenture
- C. A municipal general obligation bond
- D. A closed-end fund share

<details><summary>Answer</summary>

**C.** Exempt securities include US government and municipal securities, bank securities, commercial paper ≤ 270 days, non-profit issues, and insurance/fixed annuities. Variable annuities are securities that must be registered.

</details>

**Q109** (§11.3 · FINRA section 1) — In a secondary offering, the proceeds of the sale go to:

- A. The issuing corporation
- B. The selling shareholders
- C. The underwriting syndicate
- D. The exchange

<details><summary>Answer</summary>

**B.** A secondary offering is a registered sale of existing shares by current holders (insiders, VCs). The issuer receives nothing. In a primary offering the issuer receives the proceeds.

</details>

**Q110** (§11.4.4 · FINRA section 1) — Rule 144A permits the resale of unregistered securities to:

- A. Accredited individual investors
- B. Qualified institutional buyers with at least $100 million in securities
- C. Residents of the issuer's state
- D. Any investor after a six-month holding period

<details><summary>Answer</summary>

**B.** Rule 144A creates a liquid institutional market: restricted securities can be freely resold to QIBs (institutions managing $100 million+ in securities).

</details>


---

## Chapter 12: The secondary market

**Q111** (§12.1 · FINRA section 3) — A broker-dealer sells a bond to a customer from its own inventory. The firm must disclose on the confirmation that it acted as:

- A. An agent and show the commission
- B. A principal
- C. A market maker for the issuer
- D. A fiduciary

<details><summary>Answer</summary>

**B.** Selling from inventory is a principal (dealer) transaction compensated by a markup. The capacity must be disclosed; a firm can't charge both a markup and a commission on one trade.

</details>

**Q112** (§12.3 · FINRA section 1) — A market maker quotes XYZ at 25.10 – 25.20. A customer entering a market order to buy will pay:

- A. $25.10
- B. $25.20
- C. $25.15
- D. The last sale price

<details><summary>Answer</summary>

**B.** Customers buy at the ask (offer) and sell at the bid. The spread is the market maker's profit.

</details>

**Q113** (§12.4 · FINRA section 1) — Exchange-listed securities traded over-the-counter by non-member broker-dealers make up the:

- A. First market
- B. Second market
- C. Third market
- D. Fourth market

<details><summary>Answer</summary>

**C.** First = listed on exchange; second = unlisted OTC; third = listed securities traded OTC; fourth = institution-to-institution via ECNs.

</details>

**Q114** (§12.6.3 · FINRA section 3) — An investor who is long 500 shares of ABC at $60 wants to limit losses if the stock falls. The appropriate order is a:

- A. Buy stop at 65
- B. Sell limit at 55
- C. Sell stop at 55
- D. Buy limit at 55

<details><summary>Answer</summary>

**C.** A sell stop is placed below the market; if ABC trades at or below 55 it becomes a market order to sell. Sell limits go above the market.

</details>

**Q115** (§12.6.4 · FINRA section 3) — The primary disadvantage of a sell stop-limit order compared with a sell stop order is that:

- A. It may be executed at a much lower price than the stop
- B. It may never be executed if the stock gaps below the limit
- C. It requires a margin account
- D. It cannot be entered as a GTC order

<details><summary>Answer</summary>

**B.** Once triggered, a stop-limit becomes a limit order; if the price falls through the limit the order sits unfilled, leaving the investor unprotected.

</details>

**Q116** (§12.6.5 · FINRA section 3) — Which orders are placed BELOW the current market price?

- A. Buy limit and sell stop
- B. Buy stop and sell limit
- C. Buy limit and buy stop
- D. Sell stop and sell limit

<details><summary>Answer</summary>

**A.** BLiSS: Buy Limits and Sell Stops go below the market. SLoBS: Sell Limits and Buy Stops go above.

</details>

**Q117** (§12.6.6 · FINRA section 3) — A customer tells a rep to 'buy 1,000 shares of XYZ today at the best price you can get.' This order is:

- A. Discretionary and requires written authorization
- B. A not-held order that does not require written authorization
- C. Prohibited without principal approval
- D. A market-on-close order

<details><summary>Answer</summary>

**B.** The customer specified security, action and amount; leaving only time and price to the rep is not discretion. It's a not-held order, good for the day.

</details>

**Q118** (§12.5 · FINRA section 4) — The Securities Exchange Act of 1934 did all of the following EXCEPT:

- A. Create the SEC
- B. Require registration of broker-dealers
- C. Require registration of new securities issues with a prospectus
- D. Give the Federal Reserve authority over margin

<details><summary>Answer</summary>

**C.** Registration of new issues and the prospectus requirement come from the Securities Act of 1933. The 1934 Act regulates the secondary market, created the SEC, and covers BDs, exchanges, margin and anti-fraud.

</details>

**Q119** (§12.4.1 · FINRA section 1) — A market-wide circuit breaker halts trading for the remainder of the day when the S&P 500 falls:

- A. 7%
- B. 10%
- C. 13%
- D. 20%

<details><summary>Answer</summary>

**D.** Level 1 (7%) and Level 2 (13%) trigger 15-minute halts (before 3:25 pm); Level 3 (20%) closes the market for the day.

</details>

**Q120** (§12.6.7 · FINRA section 3) — A broker-dealer receives payment for order flow from a market maker. The firm:

- A. May route orders to that market maker regardless of price
- B. Must still obtain best execution for its customers and disclose the arrangement
- C. Must refuse the payment
- D. May accept the payment only for institutional orders

<details><summary>Answer</summary>

**B.** Payment for order flow is legal but must be disclosed, and it never overrides the duty of best execution.

</details>


---

## Chapter 13: Brokerage accounts

**Q121** (§13.2.1 · FINRA section 3) — Which of the following is NOT required to open a cash account?

- A. The customer's date of birth
- B. The customer's Social Security number
- C. The customer's signature
- D. A principal's approval

<details><summary>Answer</summary>

**C.** A customer signature isn't required for a cash account (it is for margin and options accounts). Name, address, DOB, TIN, rep name and principal approval are required.

</details>

**Q122** (§13.3.2 · FINRA section 3) — In a joint account registered as tenants in common, when one owner dies, that owner's share:

- A. Passes automatically to the surviving owner
- B. Passes to the deceased's estate
- C. Is divided equally among all surviving owners
- D. Is frozen for one year

<details><summary>Answer</summary>

**B.** TIC: the deceased's (possibly unequal) share goes to the estate. JTWROS: it passes to the survivor(s).

</details>

**Q123** (§13.3.5 · FINRA section 3) — Which of the following is TRUE of an UTMA account?

- A. There may be multiple custodians for one minor
- B. Gifts to the account are revocable until the minor reaches majority
- C. The account uses the minor's Social Security number and the minor is the beneficial owner
- D. The custodian may trade on margin to maximize growth

<details><summary>Answer</summary>

**C.** One custodian, one minor; gifts are irrevocable; the minor is the beneficial owner and taxpayer; no margin; the custodian is a fiduciary.

</details>

**Q124** (§13.3.4 · FINRA section 3) — Before a registered representative may exercise discretion over which securities to buy in a customer's account, the firm must have:

- A. An oral authorization from the customer
- B. Written authorization from the customer and principal approval of the account
- C. A trusted contact person on file
- D. A signed options agreement

<details><summary>Answer</summary>

**B.** Discretion over security, action or amount requires written trading authorization and principal approval, plus frequent principal review of the account.

</details>

**Q125** (§13.4.3 · FINRA section 3) — A customer buys $3,000 of stock in a new margin account. The required deposit is:

- A. $1,500
- B. $2,000
- C. $3,000
- D. $750

<details><summary>Answer</summary>

**B.** Reg T is 50% ($1,500), but FINRA's $2,000 minimum initial equity applies when the purchase exceeds $2,000. If the purchase were under $2,000, the customer would pay in full.

</details>

**Q126** (§13.4.5 · FINRA section 3) — A long margin account has a market value of $16,000 and a debit balance of $13,000. At the FINRA minimum maintenance requirement, the maintenance call is:

- A. $0
- B. $1,000
- C. $3,000
- D. $4,000

<details><summary>Answer</summary>

**B.** Equity = $3,000. Required = 25% × $16,000 = $4,000. Call = $1,000.

</details>

**Q127** (§13.4.2 · FINRA section 3) — The part of the margin agreement that allows the broker-dealer to pledge the customer's securities to a bank as collateral for the loan is the:

- A. Credit agreement
- B. Hypothecation agreement
- C. Loan consent form
- D. Risk disclosure statement

<details><summary>Answer</summary>

**B.** The hypothecation agreement lets the firm pledge (rehypothecate) up to 140% of the debit balance. The optional loan consent allows lending the shares to other customers for short sales.

</details>

**Q128** (§13.5 · FINRA section 3) — A customer's options account was approved on June 1 but the signed options agreement has not been returned by June 20. The customer may:

- A. Continue trading normally
- B. Open new positions only with principal approval
- C. Only close existing positions
- D. Trade only covered calls

<details><summary>Answer</summary>

**C.** The options agreement must be returned within 15 days of approval; otherwise the account is limited to closing transactions.

</details>

**Q129** (§13.6.1 · FINRA section 3) — SIPC protects customers against:

- A. Market losses on securities
- B. Losses from unsuitable recommendations
- C. Loss of cash and securities if the broker-dealer fails
- D. Losses in commodity futures accounts

<details><summary>Answer</summary>

**C.** SIPC covers missing customer assets when a member firm becomes insolvent — up to $500,000 per separate customer, including $250,000 cash. It never covers market losses.

</details>

**Q130** (§13.6.1 · FINRA section 3) — A customer has an individual account with $400,000 in securities and $300,000 in cash at a failed broker-dealer. SIPC coverage is:

- A. $500,000
- B. $650,000
- C. $700,000
- D. $250,000

<details><summary>Answer</summary>

**A.** SIPC covers up to $500,000 per separate customer in total, of which no more than $250,000 may be cash. The $400,000 in securities is fully covered and the first $100,000 of cash fills the remaining room, for a total of $500,000. The other $200,000 of cash becomes a general creditor claim against the firm.

</details>

**Q131** (§13.2.3 · FINRA section 3) — A broker-dealer must file a Suspicious Activity Report with FinCEN for suspicious transactions involving at least:

- A. $3,000
- B. $5,000
- C. $10,000
- D. $25,000

<details><summary>Answer</summary>

**B.** SARs are filed within 30 days for suspicious activity of $5,000 or more; the customer must not be told. CTRs are filed for cash transactions over $10,000.

</details>

**Q132** (§13.6.2 · FINRA section 4) — FINRA's business continuity plan rule requires each member firm to:

- A. Keep its BCP confidential from customers
- B. Disclose a summary of the plan to customers at account opening and on its website
- C. Update the plan every five years
- D. Designate a single emergency contact at FINRA

<details><summary>Answer</summary>

**B.** Firms must review the BCP annually, have senior management approve it, give customers a written summary at account opening (and on request/website), and designate two emergency contacts.

</details>


---

## Chapter 14: Retirement & education plans

**Q133** (§14.4 · FINRA section 3) — A 45-year-old investor withdraws $10,000 from a traditional IRA to buy a boat. The withdrawal is:

- A. Tax-free
- B. Taxed as ordinary income only
- C. Taxed as ordinary income plus a 10% penalty
- D. Taxed as a long-term capital gain

<details><summary>Answer</summary>

**C.** Distributions before 59½ without an exception are taxed as ordinary income plus a 10% additional tax.

</details>

**Q134** (§14.4 · FINRA section 3) — Which statement about a Roth IRA is TRUE?

- A. Contributions are tax-deductible
- B. Required minimum distributions begin at age 73
- C. Qualified withdrawals are tax-free after five years and age 59½
- D. Anyone with earned income may contribute regardless of income

<details><summary>Answer</summary>

**C.** Roth contributions are after-tax, there are no lifetime RMDs, income limits apply, and qualified withdrawals (5-year rule + 59½, death, disability, or first home) are tax-free.

</details>

**Q135** (§14.3 · FINRA section 3) — In a defined benefit pension plan, the investment risk is borne by:

- A. The employee
- B. The employer
- C. The plan trustee
- D. The PBGC

<details><summary>Answer</summary>

**B.** The employer promises a specific benefit and must fund it regardless of investment results. In a defined contribution plan the employee bears the risk.

</details>

**Q136** (§14.2 · FINRA section 3) — A participant in a 401(k) receives a distribution check payable to herself and intends to roll it into an IRA. She must complete the rollover within:

- A. 30 days
- B. 60 days
- C. 90 days
- D. One year

<details><summary>Answer</summary>

**B.** Indirect rollovers must be completed within 60 days; 20% is withheld from plan distributions, which she must make up to roll over the full amount. Direct transfers avoid these issues.

</details>

**Q137** (§14.6 · FINRA section 2) — During the payout phase of a variable annuity, the monthly payment will increase if the separate account's return is:

- A. Positive
- B. Greater than the assumed interest rate
- C. Greater than the prior month's return
- D. Greater than the CPI

<details><summary>Answer</summary>

**B.** Payments change relative to the AIR: return above the AIR raises the next payment; below lowers it; equal keeps it unchanged.

</details>

**Q138** (§14.6 · FINRA section 2) — Which annuity payout option provides the LARGEST monthly payment?

- A. Life with 10-year period certain
- B. Joint and last survivor
- C. Straight life
- D. Unit refund life

<details><summary>Answer</summary>

**C.** Straight life pays only for the annuitant's lifetime with no guarantees to beneficiaries, so the insurer can pay the most per month.

</details>

**Q139** (§14.6 · FINRA section 2) — A non-qualified variable annuity owner, age 50, makes a partial withdrawal. For tax purposes the withdrawal is treated as:

- A. Return of cost basis first, tax-free
- B. Earnings first, taxed as ordinary income plus 10% penalty
- C. Half basis, half earnings
- D. Long-term capital gain

<details><summary>Answer</summary>

**B.** Annuity withdrawals are LIFO — earnings come out first and are taxed as ordinary income, with a 10% penalty before 59½.

</details>

**Q140** (§14.7 · FINRA section 3) — Which of the following is TRUE of a 529 college savings plan?

- A. Contributions are deductible on the federal return
- B. Contributors are subject to income limits
- C. The account owner, not the beneficiary, controls the assets
- D. Withdrawals for any purpose are tax-free after age 18

<details><summary>Answer</summary>

**C.** 529 contributions are after-tax federally, have no income limits, the donor/owner keeps control and may change the beneficiary within the family, and non-qualified withdrawals incur tax plus a 10% penalty on earnings.

</details>

**Q141** (§14.5 · FINRA section 2) — In a variable life insurance policy, which of the following is guaranteed?

- A. The cash value
- B. A minimum death benefit
- C. The rate of return on the separate account
- D. The premium will never be due

<details><summary>Answer</summary>

**B.** Variable life has a fixed premium and a guaranteed minimum death benefit; the cash value and any additional death benefit vary with separate account performance.

</details>

**Q142** (§14.3 · FINRA section 3) — A 403(b) plan is available to employees of:

- A. Any corporation with fewer than 100 employees
- B. State and local governments only
- C. Public schools and 501(c)(3) non-profit organizations
- D. Self-employed individuals

<details><summary>Answer</summary>

**C.** 403(b) tax-sheltered annuity plans serve public education and non-profit employees; investments are limited to annuities and mutual funds.

</details>


---

## Chapter 15: Rules & ethics

**Q143** (§15.2.3 · FINRA section 3) — An attorney working on a merger tells her brother, who buys the target's stock. Which parties have violated insider trading rules?

- A. Only the brother
- B. Only the attorney
- C. Both the attorney (tipper) and the brother (tippee)
- D. Neither, because the attorney did not trade

<details><summary>Answer</summary>

**C.** Tippers are liable even if they don't trade; tippees who trade on MNPI are liable. Civil penalties can reach three times the profit.

</details>

**Q144** (§15.4.6 · FINRA section 3) — A registered representative wants to work weekends as a paid real estate agent. Under FINRA rules she must:

- A. Do nothing; it's unrelated to securities
- B. Give her firm prior written notice
- C. Obtain FINRA's written approval
- D. Register the activity with the state Administrator

<details><summary>Answer</summary>

**B.** Outside business activities for compensation require prior written notice to the firm (Rule 3270). Private securities transactions require notice and, if compensated, approval (Rule 3280).

</details>

**Q145** (§15.4.6 · FINRA section 3) — Under FINRA's gifts rule, business gifts to an employee of another member firm may not exceed:

- A. $50 per year
- B. $100 per person per year
- C. $300 per person per year
- D. $500 per year

<details><summary>Answer</summary>

**C.** The limit is $300 per person per year (FINRA raised it from $100 effective March 30, 2026). Business entertainment where the giver attends is excluded.

</details>

**Q146** (§15.4.3 · FINRA section 4) — A form letter sent to 40 retail customers within a week is classified as:

- A. Correspondence, requiring supervisory review
- B. Retail communication, requiring prior principal approval
- C. Institutional communication
- D. A public appearance

<details><summary>Answer</summary>

**B.** Communications to more than 25 retail investors within 30 days are retail communications and must be approved by a registered principal before use. 25 or fewer = correspondence.

</details>

**Q147** (§15.3.1 · FINRA section 3) — A firm reasonably believes an 80-year-old customer is being financially exploited by a caregiver. The firm may place a temporary hold on disbursements for up to:

- A. 5 business days
- B. 10 business days
- C. 15 business days, extendable by 10 more
- D. 30 calendar days

<details><summary>Answer</summary>

**C.** FINRA Rule 2165 allows a 15-business-day hold, extendable by 10 business days (and further if a regulator requests), with notification of the trusted contact and an internal review.

</details>

**Q148** (§15.4.5 · FINRA section 4) — A candidate fails the SIE exam for the third time. Before retesting, the candidate must wait:

- A. 30 days
- B. 60 days
- C. 90 days
- D. 180 days

<details><summary>Answer</summary>

**D.** Waiting periods are 30 days after the first and second failures and 180 days after the third and each subsequent failure.

</details>

**Q149** (§15.4.7 · FINRA section 4) — Under SEC and FINRA record-keeping rules, customer complaint records must be retained for:

- A. 3 years
- B. 4 years
- C. 6 years
- D. The life of the firm

<details><summary>Answer</summary>

**B.** Complaints: 4 years. Blotters, ledgers and account records: 6 years. Order tickets, confirms and communications: 3 years. Organizational documents: permanent.

</details>

**Q150** (§15.4.2 · FINRA section 3) — Under the Telephone Consumer Protection Act, cold calls to prospective customers may be made only between:

- A. 9 am and 5 pm in the caller's time zone
- B. 8 am and 9 pm in the called party's time zone
- C. 8 am and 8 pm in the caller's time zone
- D. 7 am and 10 pm in the called party's time zone

<details><summary>Answer</summary>

**B.** Cold calls are limited to 8:00 am–9:00 pm local time of the person called, the caller must identify themselves and the firm, and do-not-call lists must be honored.

</details>

**Q151** (§15.1 · FINRA section 4) — Which of the following is a self-regulatory organization?

- A. The SEC
- B. FINRA
- C. The Federal Reserve
- D. FinCEN

<details><summary>Answer</summary>

**B.** FINRA, the exchanges and the MSRB are SROs operating under SEC oversight. The SEC is a government agency; the Fed and FinCEN are government bodies.

</details>

**Q152** (§15.4.5 · FINRA section 4) — Passing the SIE exam allows an individual to:

- A. Open customer accounts at a broker-dealer
- B. Sell mutual funds under supervision
- C. Take a representative-level qualification exam when sponsored by a member firm
- D. Register as an investment adviser representative

<details><summary>Answer</summary>

**C.** The SIE is a co-requisite; it confers no registration. To do securities business the person must be sponsored by a firm, pass a top-off exam (Series 6, 7, etc.) and be registered on Form U4.

</details>

**Q153** (§15.4.5 · FINRA section 4) — A registered representative moves to a new address. Form U4 must be amended within:

- A. 10 days
- B. 30 days
- C. 60 days
- D. 90 days

<details><summary>Answer</summary>

**B.** Material changes to Form U4 information must be filed within 30 days. Form U5 is also due within 30 days of termination.

</details>

**Q154** (§15.4.5 · FINRA section 4) — A registered person who fails to complete the Regulatory Element of continuing education by the deadline:

- A. Is fined $1,000
- B. Has registration become inactive until it is completed
- C. Must retake the SIE
- D. Is suspended for 30 days

<details><summary>Answer</summary>

**B.** Registration becomes inactive — no securities business or compensation — until the Regulatory Element is completed; after two years inactive it is terminated.

</details>

**Q155** (§15.4.3 · FINRA section 4) — A new FINRA member firm must file its retail communications with FINRA:

- A. Within 10 business days after first use
- B. At least 10 business days before first use
- C. Within 30 days after first use
- D. Only if they concern mutual funds

<details><summary>Answer</summary>

**B.** For its first year a new member files retail communications 10 business days BEFORE first use. Investment company, DPP and CMO material is filed within 10 business days AFTER first use.

</details>

**Q156** (§15.4.7 · FINRA section 4) — Which records must a broker-dealer retain for six years?

- A. Order tickets and trade confirmations
- B. Blotters, general ledger and customer account records
- C. Customer complaints
- D. Articles of incorporation

<details><summary>Answer</summary>

**B.** Six years: blotters, ledgers, stock record, account records. Three years: tickets, confirms, communications. Four years: complaints. Permanent: organizational documents.

</details>

**Q157** (§15.4.1 · FINRA section 4) — Which law requires corporate bond issues over $50 million to have an indenture and an independent trustee?

- A. Securities Act of 1933
- B. Securities Exchange Act of 1934
- C. Trust Indenture Act of 1939
- D. Investment Company Act of 1940

<details><summary>Answer</summary>

**C.** The Trust Indenture Act of 1939 applies to public corporate debt (not governments or munis).

</details>

**Q158** (§15.4.6 · FINRA section 4) — Regulation Best Interest requires a broker-dealer making a recommendation to a retail customer to satisfy all of the following obligations EXCEPT:

- A. Disclosure
- B. Care
- C. Conflict of interest
- D. Ongoing account monitoring

<details><summary>Answer</summary>

**D.** Reg BI's four obligations are disclosure, care, conflict of interest and compliance. It does not impose a continuing duty to monitor unless the firm agrees to one.

</details>

**Q159** (§15.4.6 · FINRA section 4) — A registered representative may share in the profits of a customer's account only if:

- A. The customer is an immediate family member
- B. The firm gives prior written approval and the sharing is proportionate to the rep's contribution
- C. The rep guarantees the customer against losses
- D. The account is discretionary

<details><summary>Answer</summary>

**B.** Sharing requires prior written authorization of the firm (and customer) and must be proportional to the rep's financial contribution — except with immediate family, where proportionality is waived.

</details>

**Q160** (§15.2.1 · FINRA section 3) — Two traders agree to buy and sell the same stock back and forth at rising prices to attract other buyers. This is:

- A. Arbitrage
- B. Stabilization
- C. Matched orders / painting the tape
- D. Program trading

<details><summary>Answer</summary>

**C.** Coordinated trades designed to create a false appearance of activity or price movement are matched orders (painting the tape) — manipulation under the 1934 Act.

</details>

**Q161** (§15.1 · FINRA section 4) — Registration of agents and securities at the state level is governed by:

- A. The Securities Act of 1933
- B. The Uniform Securities Act (blue-sky laws)
- C. FINRA's Conduct Rules
- D. The Maloney Act

<details><summary>Answer</summary>

**B.** State blue-sky laws, based on the Uniform Securities Act and administered by the state Administrator (coordinated via NASAA), govern state-level registration.

</details>

**Q162** (§15.4.5 · FINRA section 4) — A person convicted of a felony four years ago applies to associate with a member firm. The person is:

- A. Eligible after passing the SIE
- B. Subject to statutory disqualification and needs FINRA approval
- C. Permanently barred
- D. Eligible only as a clerical employee

<details><summary>Answer</summary>

**B.** Any felony or securities/money-related misdemeanor conviction within 10 years is a statutory disqualification; the firm must seek FINRA approval via an eligibility proceeding.

</details>
