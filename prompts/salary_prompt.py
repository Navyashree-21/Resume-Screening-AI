SALARY_PROMPT = """
You are an HR Compensation Specialist.

Analyze ONLY the candidate's expected salary based on the resume.

Return ONLY valid JSON.

{{
    "experience_level": "",
    "recommended_role": "",
    "salary_range_lpa": "",
    "salary_score": 0,
    "reason": ""
}}

Resume:

{resume}

Instructions:
- Estimate the candidate's experience level.
- Suggest the most suitable job role.
- Estimate a realistic annual salary range in LPA (India).

- Return salary_score as an INTEGER between 0 and 100.
- Use the following scoring guidelines:
    * Excellent candidate: 90-100
    * Strong candidate: 75-89
    * Average candidate: 50-74
    * Weak candidate: Below 50

- Do not return decimal values.
- Return ONLY valid JSON.
"""