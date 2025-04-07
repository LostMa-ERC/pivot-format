from dataclasses import dataclass


@dataclass
class WorkflowStep:
    heurist: str = "heurist"
    graph: str = "graph"
    tei: str = "tei"


WORKFLOW_CHOICES = list(WorkflowStep.__annotations__.keys())
