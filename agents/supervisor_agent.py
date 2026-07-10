from agents.skill_agent import SkillAgent
from agents.education_agent import EducationAgent
from agents.experience_agent import ExperienceAgent
from agents.salary_agent import SalaryAgent


class SupervisorAgent:

    def __init__(self):

        self.skill_agent = SkillAgent()
        self.education_agent = EducationAgent()
        self.experience_agent = ExperienceAgent()
        self.salary_agent = SalaryAgent()

    def analyze(self, resume):

        skill = self.skill_agent.analyze(resume)

        education = self.education_agent.analyze(resume)

        experience = self.experience_agent.analyze(resume)

        salary = self.salary_agent.analyze(resume)

        overall_score = round(
            skill["skill_score"] * 0.40 +
            education["education_score"] * 0.20 +
            experience["experience_score"] * 0.30 +
            salary["salary_score"] * 0.10
        )

        if overall_score >= 85:
            decision = "APPROVE"
        elif overall_score >= 70:
            decision = "HOLD"
        else:
            decision = "REJECT"

        return {
            "skill": skill,
            "education": education,
            "experience": experience,
            "salary": salary,
            "overall_score": overall_score,
            "decision": decision
        }