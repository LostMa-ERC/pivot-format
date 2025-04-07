from app.cli.commands import WorkflowStep
from app.cli.commands.graph import build_graph
from app.cli.commands.heurist import heurist_download
from app.cli.commands.pivot_texts import pivot_all_texts_to_tei


def run_workflow(login: str | None, password: str | None, stop_at_step: str | None):
    # Download the Heurist data
    heurist_download(login=login, password=password)
    if stop_at_step == WorkflowStep.heurist:
        exit()

    # Build the Heurist relational data into a graph database
    build_graph()
    if stop_at_step == WorkflowStep.graph:
        exit()

    # Pivot the graph data into TEI documents
    pivot_all_texts_to_tei()
