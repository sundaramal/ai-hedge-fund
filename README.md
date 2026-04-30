# AI Hedge Fund

This is a proof of concept for an AI-powered hedge fund.  The goal of this project is to explore the use of AI to make trading decisions.  This project is for **educational** purposes only and is not intended for real trading or investment.

This system employs several agents working together:

1. Aswath Damodaran Agent - The Dean of Valuation, focuses on story, numbers, and disciplined valuation
2. Ben Graham Agent - The godfather of value investing, only buys hidden gems with a margin of safety
3. Bill Ackman Agent - An activist investor, takes bold positions and pushes for change
4. Cathie Wood Agent - The queen of growth investing, believes in the power of innovation and disruption
5. Charlie Munger Agent - Warren Buffett's partner, only buys wonderful businesses at fair prices
6. Michael Burry Agent - The Big Short contrarian who hunts for deep value
7. Mohnish Pabrai Agent - The Dhandho investor, who looks for doubles at low risk
8. Nassim Taleb Agent - The Black Swan risk analyst, focuses on tail risk, antifragility, and asymmetric payoffs
9. Peter Lynch Agent - Practical investor who seeks "ten-baggers" in everyday businesses
10. Phil Fisher Agent - Meticulous growth investor who uses deep "scuttlebutt" research 
11. Rakesh Jhunjhunwala Agent - The Big Bull of India
12. Stanley Druckenmiller Agent - Macro legend who hunts for asymmetric opportunities with growth potential
13. Warren Buffett Agent - The oracle of Omaha, seeks wonderful companies at a fair price
14. Valuation Agent - Calculates the intrinsic value of a stock and generates trading signals
15. Sentiment Agent - Analyzes market sentiment and generates trading signals
16. Fundamentals Agent - Analyzes fundamental data and generates trading signals
17. Technicals Agent - Analyzes technical indicators and generates trading signals
18. Risk Manager - Calculates risk metrics and sets position limits
19. Portfolio Manager - Makes final trading decisions and generates orders

<img width="1042" alt="Screenshot 2025-03-22 at 6 19 07 PM" src="https://github.com/user-attachments/assets/cbae3dcf-b571-490d-b0ad-3f0f035ac0d4" />

Note: the system does not actually make any trades.

> **Personal note:** I'm using this project to study how different investing philosophies can be modeled as AI agents. My main interest is comparing the value-oriented agents (Graham, Munger, Buffett) against the growth-oriented ones (Cathie Wood, Phil Fisher) across different market conditions. I'm particularly curious about how the Nassim Taleb agent behaves during high-volatility periods compared to the others.

[![Twitter Follow](https://img.shields.io/twitter/follow/virattt?style=social)](https://twitter.com/virattt)

## Getting Started

See the original repo for full setup instructions. For my own reference, the quickest way to run a backtest:

```bash
# Example: run a backtest on AAPL from 2024-01-01 to 2024-06-30
python src/backtester.py --ticker AAPL --start-date 2024-01-01 --end-date 2024-06-30

# Example: run a backtest comparing multiple tickers
python src/backtester.py --ticker MSFT --start-date 2023-01-01 --end-date 2023-12-31
```

## Agents I Find Most Interesting

For my own study, here's a quick ranking of which agents I'm focusing on first:

1. **Nassim Taleb** – want to see how tail-risk logic translates to signals
2. **Ben Graham** – classic margin-of-safety math is well-defined, good baseline
3. **Cathie Wood** – curious how "innovation" is quantified without pure narrative
