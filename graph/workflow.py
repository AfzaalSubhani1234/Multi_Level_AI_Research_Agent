# graph/workflow.py

from agents.research_agent import research_agent

from agents.fact_checker import fact_checker_agent

from agents.summarizer import summarizer_agent

from agents.report_generator import report_generator_agent


def run_workflow(question):

    research = research_agent(question)

    verified = fact_checker_agent(research)

    summary = summarizer_agent(verified)

    report = report_generator_agent(summary)

    return report