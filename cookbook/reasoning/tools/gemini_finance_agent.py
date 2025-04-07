# -*- coding: utf-8 -*-
"""gemini_finance_agent.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XYnlyi_LFuvtR0qSHDLOWMRGMmgi60RQ
"""

# ! pip install -U agno

from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.thinking import ThinkingTools
from agno.tools.yfinance import YFinanceTools

thinking_agent = Agent(
    model=Gemini(id="gemini-2.0-flash"),
    tools=[
        ThinkingTools(add_instructions=True),
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
        ),
    ],
    instructions="Use tables where possible",
    show_tool_calls=True,
    markdown=True,
)
thinking_agent.print_response("Write a report comparing NVDA to TSLA in detail", stream=True)

