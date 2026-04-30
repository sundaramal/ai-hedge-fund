"""Shared state definitions for the AI hedge fund agent graph.

This module defines the AgentState TypedDict used to pass data
between agents in the LangGraph workflow.
"""

from typing import Annotated, Any, Sequence
from typing_extensions import TypedDict
import operator


class AgentState(TypedDict):
    """Shared state passed between agents in the hedge fund workflow.

    Attributes:
        messages: Accumulated list of messages from all agents.
        ticker: The stock ticker symbol being analyzed (e.g. 'AAPL').
        start_date: Start of the analysis window (YYYY-MM-DD).
        end_date: End of the analysis window (YYYY-MM-DD).
        portfolio: Current portfolio holdings and cash balance.
        data: Raw financial data fetched for the ticker.
        fundamentals: Parsed fundamental analysis metrics.
        technical_indicators: Computed technical indicator values.
        sentiment: Aggregated sentiment signal from news/filings.
        risk_assessment: Risk metrics produced by the risk manager.
        final_decision: The final trade decision (buy / sell / hold).
        show_reasoning: Whether agents should include verbose reasoning.
    """

    # Reducer that appends new messages rather than overwriting
    messages: Annotated[Sequence[dict[str, Any]], operator.add]

    # Core inputs
    ticker: str
    start_date: str
    end_date: str

    # Portfolio state
    portfolio: dict[str, Any]

    # Intermediate agent outputs
    data: dict[str, Any]
    fundamentals: dict[str, Any]
    technical_indicators: dict[str, Any]
    sentiment: dict[str, Any]
    risk_assessment: dict[str, Any]

    # Final output
    final_decision: dict[str, Any]

    # Control flags
    show_reasoning: bool


def create_initial_state(
    ticker: str,
    start_date: str,
    end_date: str,
    portfolio: dict[str, Any] | None = None,
    show_reasoning: bool = False,
) -> AgentState:
    """Build an initial AgentState with sensible defaults.

    Args:
        ticker: Stock ticker symbol to analyse.
        start_date: ISO-format start date string (YYYY-MM-DD).
        end_date: ISO-format end date string (YYYY-MM-DD).
        portfolio: Optional existing portfolio dict; defaults to
            100 000 USD cash with no open positions.
        show_reasoning: If True, agents will attach verbose reasoning
            to their messages.

    Returns:
        A fully initialised AgentState ready to be fed into the graph.
    """
    if portfolio is None:
        portfolio = {
            "cash": 100_000.0,
            "positions": {},
        }

    return AgentState(
        messages=[],
        ticker=ticker,
        start_date=start_date,
        end_date=end_date,
        portfolio=portfolio,
        data={},
        fundamentals={},
        technical_indicators={},
        sentiment={},
        risk_assessment={},
        final_decision={},
        show_reasoning=show_reasoning,
    )
