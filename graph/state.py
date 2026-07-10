from typing import TypedDict


class ResumeState(TypedDict):

    # Input
    resume: str
    jd: str

    # Agent Outputs
    skill: dict
    education: dict
    experience: dict
    salary: dict
    jd_match: dict

    # Final Decision
    overall_score: int
    decision: str

    improvement: dict