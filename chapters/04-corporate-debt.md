# Chapter 4: Corporate Debt

> Builds on Chapter 3. Focus areas: the money-market products, secured vs. unsecured bonds, convertibles math, liquidation priority, and the bank-issued products (CDs, BAs, Eurodollars).

---

## 4.1 Short-term products (the money market)

The **money market** is where high-quality debt with **one year or less** to maturity trades. These instruments are highly liquid, low-risk, low-return, and are typically bought at a **discount** and mature at face value (the gain is the "interest"). They are used by investors for cash management and by corporations for short-term borrowing.

**Commercial paper (CP).**

- Unsecured **promissory notes** issued by large, creditworthy corporations (and finance companies) to fund short-term needs like payroll and inventory.
- Maturity: **up to 270 days** (most are 30–90 days). Why 270? Because debt with a maturity of 270 days or less is **exempt from SEC registration** under the Securities Act of 1933.
- Sold at a discount; minimum denominations are large (typically $100,000+), so buyers are institutions and money market funds.
- Rated by the rating agencies (e.g., A-1/P-1 for top tier).

**Negotiable (jumbo) certificates of deposit.** Bank-issued time deposits of **$100,000 or more** that can be traded in the secondary market before maturity. Pay interest at maturity. FDIC-insured only up to **$250,000**. (Regular bank CDs, by contrast, are not negotiable — see 4.6.)

**Banker's acceptances (BAs).** A time draft (post-dated check) guaranteed ("accepted") by a bank, used to finance **import/export** transactions. Maturities up to 270 days (commonly 30–180). Traded at a discount. Think "BA = foreign trade."

**Repurchase agreements (repos).** A dealer sells securities (usually Treasuries) and agrees to buy them back at a slightly higher price on a set date — effectively a short-term collateralized loan. Overnight repos are common. A **reverse repo** is the same transaction from the other side. The Fed uses repos to manage bank reserves.

**Treasury bills.** The government's money-market instrument (Chapter 6). Maturities of 4, 8, 13, 17, 26 and 52 weeks; sold at a discount.

**Federal funds.** Overnight loans of excess reserves between banks. The **fed funds rate** is the most-watched short-term rate (the Fed targets it).

**Money market funds** — mutual funds that invest in all of the above (Chapter 7).

| Instrument | Issuer | Max maturity | Notes |
|---|---|---|---|
| Commercial paper | Corporations | 270 days | Unsecured; registration-exempt |
| Negotiable CD | Banks | Usually ≤ 1 yr | $100k+; tradable |
| Banker's acceptance | Banks (for importers/exporters) | 270 days | Foreign trade |
| Repo | Dealers/banks | Overnight to short | Collateralized by Treasuries |
| T-bill | US Treasury | 52 weeks | Safest |

---

## 4.2 Long-term products

Corporate bonds with maturities beyond one year. Classified mainly by what backs them.

### Secured bonds (backed by specific collateral)

- **Mortgage bonds** — secured by real estate/plant. First-mortgage bonds have the senior claim on the property; second-mortgage bonds are junior. Common for utilities.
- **Equipment trust certificates (ETCs)** — secured by movable equipment (aircraft, railcars, trucks, ships). Title is held by a trustee until the debt is repaid. Common for airlines and railroads. Very safe because the equipment can be repossessed and resold.
- **Collateral trust bonds** — secured by securities the issuer owns (e.g., stock of a subsidiary), held by a trustee.

### Unsecured bonds (backed only by the issuer's promise)

- **Debentures** — backed by the full faith and credit of the issuer. Most corporate bonds are debentures. Holders are **general creditors**.
- **Subordinated debentures** — rank below other debentures. Higher yield for the extra risk. Often convertible.
- **Guaranteed bonds** — guaranteed by a company other than the issuer (usually a parent guaranteeing a subsidiary's debt). Credit quality depends on the guarantor.
- **Income (adjustment) bonds** — pay interest only if the company earns enough. Issued by companies in reorganization. Trade **flat** (no accrued interest). Highly speculative.

### Other corporate bond types

- **High-yield ("junk") bonds** — rated below BBB/Baa. Higher coupon, higher default risk. Often issued in leveraged buyouts.
- **Zero-coupon corporate bonds** — deep discount, phantom income taxed annually.
- **Floating-rate notes** — coupon resets to a benchmark; price stable.
- **Step-up bonds** — coupon increases over time.

**Debt vs. equity for the issuer.** Debt is cheaper (interest is tax-deductible to the corporation; dividends are not) and doesn't dilute ownership, but interest is a fixed legal obligation and adds **leverage** (financial risk). Highly leveraged companies are riskier for both bondholders and stockholders.

---

## 4.3 Convertible products

A **convertible bond** (usually a convertible debenture) can be exchanged for a fixed number of common shares. Investors accept a **lower coupon** in exchange for the upside. Issuers like them because they lower borrowing costs and conversion eliminates the debt.

**The math (this gets tested).**

```
Conversion ratio  = Par ÷ Conversion price
Parity price of the bond  = Stock market price × Conversion ratio
Parity price of the stock = Bond market price ÷ Conversion ratio
```

**Example.** A $1,000 par bond is convertible at $50. Conversion ratio = 1,000 / 50 = **20 shares**.

- If the stock trades at $55, parity for the bond = 55 × 20 = **$1,100**. If the bond is trading at $1,050, it's cheaper to buy the bond and convert than to buy the stock directly — an **arbitrage** opportunity.
- If the bond trades at $1,200, parity for the stock = 1,200 / 20 = **$60**.

**Behavior.**

- When the stock is far **below** the conversion price, the bond trades like a straight bond (on its yield) — this is its **investment value** or "bond floor."
- When the stock is near/above the conversion price, the bond's price tracks the stock (parity).
- The bond usually trades at a small **premium over parity** because of the downside protection the coupon provides.
- **Anti-dilution** provisions adjust the conversion price for stock splits and stock dividends so the holder's conversion value is preserved.
- Conversion is **not a taxable event**; the holder's cost basis carries over to the shares.
- **Forced conversion**: if the bond is callable and the stock is above parity, the issuer can call the bond, forcing holders to convert (worth more than the call price) — which eliminates the issuer's debt.

**Who should buy convertibles?** Investors who want **income with growth potential** and some downside protection. Downsides: lower yield than straight debt and dilution risk for common stockholders when conversion occurs.

---

## 4.4 Liquidation policy

In a corporate bankruptcy (Chapter 7 liquidation), claims are paid in strict order. Each tier must be paid in full before the next receives anything.

1. **Secured creditors** — up to the value of their collateral (mortgage bonds, ETCs, collateral trust bonds).
2. **Administrative costs, wages, taxes** (statutory priority — sometimes shown as before general creditors).
3. **Unsecured/general creditors** — debenture holders, suppliers, banks with unsecured loans.
4. **Subordinated debenture holders.**
5. **Preferred stockholders.**
6. **Common stockholders** — residual claim; usually receive nothing.

A bondholder's claim is the par value plus accrued interest. Any secured creditor whose collateral didn't cover the claim joins the general creditors for the remainder.

**Chapter 11 reorganization** is the alternative to liquidation: the company keeps operating under court supervision, and old bondholders are often given new securities (sometimes income bonds or stock) in the reorganized company.

---

## 4.5 The market & quotes

**Where corporates trade.** A small number of corporate bonds are listed on the NYSE, but the overwhelming majority trade **OTC** between dealers. Trades must be reported to **TRACE** within 15 minutes, making corporate bond prices publicly available.

**Quotations.** Corporate bonds are quoted as a percentage of par in **1/8-point increments**.

| Quote | Dollar price |
|---|---|
| 100 | $1,000 |
| 97 ½ | $975.00 |
| 102 ⅜ | $1,023.75 |
| 89 ⅛ | $891.25 |

A dealer quote might read "97 ½ – 98 ¼": bid $975, ask $982.50. The customer buys at the ask and sells at the bid.

**Reading a bond description.** "XYZ 5s of '38" = XYZ Corporation bonds with a 5% coupon maturing in 2038. "5s" means 5% coupon; paid semiannually ($25).

**Accrued interest on corporates.** 30/360 basis; interest is paid semiannually on dates such as J&J 1 (January 1 and July 1), F&A 15, M&S 1, A&O 1, M&N 15, J&D 1.

**Example.** A corporate bond pays interest J&J 1. It is sold with settlement on March 16. Accrued interest covers Jan 1 through March 15: January (30) + February (30) + 15 days of March = **75 days**. On a 6% bond: $60 × 75/360 = **$12.50** owed by the buyer to the seller.

**Settlement:** regular way T+1.

**Markups.** Dealers acting as principal mark up prices; FINRA requires markups to be fair, and since 2018 retail confirmations must disclose the markup on most corporate and agency bond trades.

---

## 4.6 Bank issues

**Certificates of deposit (non-negotiable).** Time deposits with a bank for a fixed term (one month to several years) paying a fixed rate. Insured by the **FDIC up to $250,000 per depositor, per bank, per ownership category**. Early withdrawal triggers a penalty. These are bank products, not securities, and not SIPC-covered — but the exam still tests them.

**Negotiable (jumbo) CDs.** $100,000 minimum; can be sold in the secondary market before maturity (so no early-withdrawal penalty but you face interest-rate risk). Interest paid at maturity. FDIC coverage still capped at $250,000.

**Brokered CDs.** CDs that a broker-dealer buys from banks and sells to its customers. They are FDIC-insured (the broker arranges insurance to pass through to the customer), can be sold in a secondary market (price may be below par), and sometimes are callable. Disclosure of call features and the secondary-market risk is required.

**Structured CDs / market-linked CDs.** Return tied to an index; principal protected only if held to maturity. Complex; suitability concerns.

**Bank-related money market items:** banker's acceptances (4.1), federal funds, and **Eurodollar deposits** (next section).

---

## 4.7 Eurodollars & Eurobonds

**Eurodollars** are **US-dollar-denominated deposits held in banks outside the United States** (originally Europe, hence the name, but now anywhere — a dollar deposit in a Tokyo bank is a Eurodollar deposit). They are not subject to US bank reserve requirements or FDIC insurance. Eurodollar **time deposits** and **Eurodollar CDs** are money-market instruments. The interest rates on them were historically benchmarked to LIBOR, now replaced by **SOFR** (Secured Overnight Financing Rate) and similar rates.

**Eurobonds** are bonds issued and sold **outside the country whose currency they are denominated in**. A **Eurodollar bond** is a dollar-denominated bond issued outside the US (e.g., a US corporation selling dollar bonds in London). Key points:

- Not registered with the SEC (issued outside US jurisdiction), so they cannot be sold to US investors at issue (though they may trade later).
- Usually pay interest **annually** (not semiannually) and are often in bearer form.
- Investors in a Eurobond denominated in a foreign currency bear **currency risk**; Eurodollar bond holders do not have currency risk if they are dollar-based investors.
- Lower regulatory cost means issuers can borrow cheaply.

**Yankee bonds** (for contrast): dollar-denominated bonds issued **in the US** by a **foreign** issuer and registered with the SEC. US investors face no currency risk.

| Bond | Issued where | Currency | Registered with SEC? |
|---|---|---|---|
| Eurodollar bond | Outside US | USD | No |
| Yankee bond | In the US | USD | Yes |
| Eurobond (general) | Outside the home country of the currency | Any | Depends on the country |

---

## Chapter 4 quick review

- Money market = ≤ 1 year, discount instruments: commercial paper (≤ 270 days, unsecured, exempt from registration), negotiable CDs ($100k+), BAs (foreign trade), repos, T-bills, fed funds.
- Secured: mortgage bonds, ETCs (equipment), collateral trust (securities). Unsecured: debentures, subordinated debentures, guaranteed bonds, income bonds (trade flat).
- Convertibles: ratio = par ÷ conversion price; parity = stock × ratio; lower coupon; not taxable to convert; forced conversion via call.
- Liquidation order: secured → general creditors → subordinated → preferred → common.
- Quotes in 1/8ths; 1 point = $10; accrued interest 30/360; TRACE reporting; T+1.
- CDs: FDIC $250,000; negotiable CDs tradable; brokered CDs may be callable.
- Eurodollars = USD deposits abroad; Eurodollar bonds = USD bonds issued outside US, unregistered, annual interest. Yankee bonds = foreign issuer, in the US, registered.
