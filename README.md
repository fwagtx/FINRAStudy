# FINRA SIE Exam — Complete Study Guide

An original, comprehensive study guide for the **Securities Industry Essentials (SIE)** exam, organized to mirror a standard 15-chapter textbook structure, with a numbers/formulas cheat sheet, a 700+ question practice bank, and a dark-theme study app (`app/index.html`) with a progress-tracking dashboard, chapter reader, chapter quizzes and full-length timed practice exams.

> **How to use this with Claude Code:** drop this whole folder into a project and ask Claude Code to quiz you from `questions/question-bank.json`, explain any section in `chapters/`, generate new questions in the same JSON schema, or extend the app. Everything is plain markdown/JSON/HTML.

---

## The exam at a glance (verified October 2026)

| | |
|---|---|
| **Questions** | 75 scored + 10 unscored pretest (85 total, you won't know which) |
| **Time** | 1 hour 45 minutes (105 minutes) |
| **Passing score** | 70 (scaled) |
| **Fee** | $100 |
| **Eligibility** | Anyone 18+, no firm sponsorship required |
| **Results valid** | 4 years (you must then pass a "top-off" exam — Series 6, 7, etc. — and be sponsored by a firm to become registered) |
| **Retake waits** | 30 days after the 1st and 2nd fail; 180 days after the 3rd and each later fail |
| **Format** | Multiple choice, 4 options, computer-based at Prometric or online proctored |

### Official FINRA content outline and weights

| Section | Weight | ≈ Questions | Covered in chapters |
|---|---|---|---|
| 1. Knowledge of Capital Markets | **16%** | 12 | 6.5 (economy/Fed), 11 (primary market), 12 (secondary market), 15.1 (regulators) |
| 2. Understanding Products and Their Risks | **44%** | 33 | 1–9 (stocks, bonds, munis, governments, funds, alternatives, options), 14 (annuities, plans) |
| 3. Understanding Trading, Customer Accounts and Prohibited Activities | **31%** | 23 | 10 (taxes), 12.6 (orders), 13 (accounts, margin, SIPC), 14 (retirement), 15.2–15.3 (prohibited activities) |
| 4. Overview of the Regulatory Framework | **9%** | 7 | 15.1, 15.4 (regulators, laws, licensing, CE, communications, records) |

Products are nearly half the exam. Bonds (Chapters 3–6) and investment companies (Chapter 7) are the single biggest clusters.

---

## Folder contents

```
sie-study-guide/
├── README.md                     ← this file
├── CHEAT-SHEET.md                ← every number, formula and date on one page
├── essentials/                   ← 15 condensed must-know pages (one per chapter), each with a 12-question check in the app
├── chapters/
│   ├── 01-common-stock.md
│   ├── 02-preferred-stock.md
│   ├── 03-debt-securities.md
│   ├── 04-corporate-debt.md
│   ├── 05-municipal-debt.md
│   ├── 06-us-government-debt.md  (includes the Fed, monetary & fiscal policy, economic indicators)
│   ├── 07-investment-companies.md
│   ├── 08-alternative-pooled-investments.md
│   ├── 09-options.md
│   ├── 10-taxes.md
│   ├── 11-the-primary-market.md
│   ├── 12-the-secondary-market.md
│   ├── 13-brokerage-accounts.md
│   ├── 14-retirement-and-education-plans.md
│   └── 15-rules-and-ethics.md
├── questions/
│   ├── question-bank.json        ← 700+ original questions with explanations, tagged by chapter & FINRA section
│   └── question-bank.md          ← the same questions in readable form
└── app/
    └── index.html                ← self-contained study app (reader + dashboard + quizzes + timed exams)
```

Every chapter ends with a **quick review** box — read those the night before the exam.

---

## Suggested 4-week plan

| Week | Study | Practice |
|---|---|---|
| 1 | Chapters 1–4 (equities, bond fundamentals, corporate debt) | Chapter quizzes 1–4 |
| 2 | Chapters 5–9 (munis, governments & the economy, funds, alternatives, options) | Chapter quizzes 5–9; first full practice exam (expect 55–65%) |
| 3 | Chapters 10–13 (taxes, primary & secondary markets, accounts & margin) | Chapter quizzes 10–13; second practice exam |
| 4 | Chapters 14–15 (retirement plans, rules & ethics); re-read every quick review; CHEAT-SHEET.md daily | Practice exams until you consistently score 80%+; drill the weak-chapter list on the dashboard |

**Exam-day tactics.** Read every question twice; look for "EXCEPT" and "NOT." Eliminate two answers first. Mark and move on when stuck — there's no penalty for guessing, so answer everything. Pace: ~1 minute 20 seconds per question leaves 10+ minutes for review.

---

## Study app

Open `app/index.html` in any browser (no server needed). It has:

- **Dashboard** — sections completed per chapter, practice exam history with score trend, per-chapter accuracy, and a "weakest chapters" list.
- **Textbook** — all 15 chapters in a left-nav accordion with a reading pane; mark sections as read.
- **Quizzes** — per-chapter quizzes drawn from the question bank.
- **Practice exams** — 75-question, 105-minute timed exams weighted to the FINRA outline, with full explanations after submission.

Progress is stored in your browser's local storage (export/import as JSON from the dashboard).

---

## Sources used to verify current figures

- FINRA — Securities Industry Essentials (SIE) Exam: https://www.finra.org/industry/sie
- IRS/Schwab summary of 2026 contribution and gift-tax limits: https://workplace.schwab.com/story/tax-brackets-and-contribution-limits

All explanatory text is original. Figures that change annually (contribution limits, exam fee) are marked with the year.
