EDUCATION_PROMPT = """
You are an HR Recruiter.

Analyze ONLY the candidate's educational background.

Return ONLY valid JSON.

{{
    "degree": "",
    "college": "",
    "gpa": "",
    "certifications": [],
    "education_score": 0,
    "reason": ""
}}

Resume:

{resume}

Instructions:
- Identify the candidate's highest degree.
- Extract the college/university name.
- Extract the GPA or percentage if available.
- List all relevant certifications.
- Return education_score as an INTEGER between 0 and 100.

Scoring Guidelines:
- Excellent candidate: 90-100
- Strong candidate: 75-89
- Average candidate: 50-74
- Weak candidate: Below 50

- Do not return decimal values.
- Do not return markdown.
- Return ONLY valid JSON.
"""