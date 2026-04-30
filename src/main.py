"""AI Hedge Fund - Main Entry Point

This module serves as the primary entry point for the AI-powered hedge fund
simulation system. It orchestrates agents, data pipelines, and trading logic.
"""

import argparse
import sys
from datetime import datetime, timedelta
from typing import Optional

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments for the hedge fund simulation."""
    parser = argparse.ArgumentParser(
        description="AI Hedge Fund - Autonomous trading agent simulation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python src/main.py --ticker AAPL --start-date 2024-01-01 --end-date 2024-06-30
  python src/main.py --ticker TSLA --show-reasoning
  python src/main.py --ticker NVDA --initial-capital 50000
    """,
    )

    parser.add_argument(
        "--ticker",
        type=str,
        required=True,
        help="Stock ticker symbol to analyze (e.g., AAPL, TSLA)",
    )
    parser.add_argument(
        "--start-date",
        type=str,
        default=None,
        help="Start date for analysis in YYYY-MM-DD format (default: 3 months ago)",
    )
    parser.add_argument(
        "--end-date",
        type=str,
        default=None,
        help="End date for analysis in YYYY-MM-DD format (default: today)",
    )
    parser.add_argument(
        "--initial-capital",
        type=float,
        default=10_000.0,  # Lowered from 100k to 10k to better reflect my paper trading budget
        help="Initial capital in USD for the portfolio (default: 10000)",
    )
    parser.add_argument(
        "--show-reasoning",
        action="store_true",
        default=False,
        help="Display detailed reasoning from each agent",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="gpt-4o-mini",  # Switched default to mini to save on API costs
        choices=["gpt-4o", "gpt-4o-mini", "gpt-4-turbo", "claude-3-5-sonnet-20241022"],
        help="LLM model to use for agent reasoning (default: gpt-4o-mini)",
    )
    parser.add_argument(
        "--lookback-days",
        type=int,
        default=90,  # Default lookback window; I find 90 days gives a good balance of signal vs noise
        help="Number of days to look back when start-date is not specified (default: 90)",
    )

    return parser.parse_args()


def validate_date(date_str: Optional[str], label: str) -> Optional[str]:
    """Validate that a date string is in the correct YYYY-MM-DD format."""
    if date_str is None:
        return None
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        print(f"Error: {label} '{date_str}' is not in YYYY-MM-DD format.", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    """Main execution function for the AI Hedge Fund."""
    args = parse_arguments()

    # Validate date inputs
    start_date = validate_date(args.start_date, "start-date")
    end_date = validate_date(args.end_date, "end-date")

    # Set default dates if not provided
    if end_date is None:
        end_date = datetime.today().strftime("%Y-%m-%d")
    if start_date is None:
        start_date = (datetime.today() - timedelta(days=args.lookback_days)).strftime("%Y-%m-%d")
