from langgraph.graph import StateGraph, START, END

from graph.state import ResumeState

from agents.skill_agent import SkillAgent
from agents.education_agent import EducationAgent
from agents.experience_agent import ExperienceAgent
from agents.salary_agent import SalaryAgent
from agents.jd_agent import JDAgent
from agents.improvement_agent import ImprovementAgent


# ---------------------------------------------------------
# Initialize Agents
# ---------------------------------------------------------

skill_agent = SkillAgent()
education_agent = EducationAgent()
experience_agent = ExperienceAgent()
salary_agent = SalaryAgent()
jd_agent = JDAgent()
improvement_agent = ImprovementAgent()


# ---------------------------------------------------------
# Skill Node
# ---------------------------------------------------------

def skill_node(state):

    return {
        "skill": skill_agent.analyze(
            state["resume"]
        )
    }


# ---------------------------------------------------------
# Education Node
# ---------------------------------------------------------

def education_node(state):

    return {
        "education": education_agent.analyze(
            state["resume"]
        )
    }


# ---------------------------------------------------------
# Experience Node
# ---------------------------------------------------------

def experience_node(state):

    return {
        "experience": experience_agent.analyze(
            state["resume"]
        )
    }


# ---------------------------------------------------------
# Salary Node
# ---------------------------------------------------------

def salary_node(state):

    return {
        "salary": salary_agent.analyze(
            state["resume"]
        )
    }


# ---------------------------------------------------------
# Supervisor Node
# ---------------------------------------------------------

def supervisor_node(state):

    skill = state["skill"]["skill_score"]

    education = state["education"]["education_score"]

    experience = state["experience"]["experience_score"]

    salary = state["salary"]["salary_score"]

    overall = round(

        skill * 0.40 +

        education * 0.20 +

        experience * 0.30 +

        salary * 0.10

    )

    if overall >= 85:

        decision = "APPROVE"

    elif overall >= 70:

        decision = "HOLD"

    else:

        decision = "REJECT"

    return {

        "overall_score": overall,

        "decision": decision

    }


# ---------------------------------------------------------
# JD Matching Node
# ---------------------------------------------------------

def jd_node(state):

    if not state.get("jd"):

        return {

            "jd_match": {

                "match_percentage": 0,

                "ats_score": 0,

                "matching_skills": [],

                "missing_skills": [],

                "recommendations": [],

                "reason": "No Job Description uploaded."

            }

        }

    return {

        "jd_match": jd_agent.analyze(

            state["resume"],

            state["jd"]

        )

    }
def improvement_node(state):

    state["improvement"] = improvement_agent.analyze(
        state["resume"],
        state["jd"]
    )

    return state

# ---------------------------------------------------------
# Build LangGraph
# ---------------------------------------------------------

def build_graph():

    builder = StateGraph(ResumeState)

    # Nodes

    builder.add_node("skill", skill_node)

    builder.add_node("education", education_node)

    builder.add_node("experience", experience_node)

    builder.add_node("salary", salary_node)

    builder.add_node("supervisor", supervisor_node)

    builder.add_node("jd", jd_node)
    builder.add_node(
    "improvement",
    improvement_node
)


    # Edges

    builder.add_edge(START, "skill")

    builder.add_edge("skill", "education")

    builder.add_edge("education", "experience")

    builder.add_edge("experience", "salary")

    builder.add_edge("salary", "supervisor")

    builder.add_edge("supervisor", "jd")

    builder.add_edge(
    "jd",
    "improvement"
)

    builder.add_edge(
    "improvement",
    END
)

    return builder.compile()