# 📄 Multi-Agent AI Resume Screening & ATS Analysis System

An AI-powered Resume Screening System that evaluates resumes using a **Multi-Agent Architecture** built with **LangGraph**, **Google Gemini 2.5 Flash**, and **Streamlit**. The system analyzes resumes across multiple dimensions, compares them against a Job Description (JD), provides ATS compatibility, suggests resume improvements, and generates a downloadable PDF report.

---

## 🚀 Features

- ✅ Resume PDF Parsing
- ✅ Job Description (JD) Parsing
- ✅ Multi-Agent AI Architecture using LangGraph
- ✅ Skill Analysis
- ✅ Education Analysis
- ✅ Experience Analysis
- ✅ Salary Prediction
- ✅ ATS Resume Matching
- ✅ Resume Improvement Suggestions
- ✅ Overall Resume Score
- ✅ Hiring Recommendation (Approve / Hold / Reject)
- ✅ Interactive Streamlit Dashboard
- ✅ Downloadable PDF Report

---

# 🏗️ System Architecture

```
                  Resume
                     │
                     ▼
          ┌────────────────────┐
          │   PDF Parser       │
          └────────────────────┘
                     │
                     ▼
             Clean Resume Text
                     │
                     ▼
              LangGraph Workflow
                     │
 ┌──────────┬──────────┬──────────┬──────────┐
 │          │          │          │          │
 ▼          ▼          ▼          ▼          ▼
Skill   Education Experience Salary   JD Match
Agent     Agent      Agent     Agent     Agent
 │          │          │          │          │
 └──────────┴──────────┴──────────┴──────────┘
                     │
                     ▼
         Resume Improvement Agent
                     │
                     ▼
          Final AI Recommendation
                     │
                     ▼
          Streamlit Dashboard + PDF
```

---

# 🧠 AI Agents

## 1️⃣ Skill Agent

Analyzes the resume and extracts:

- Technical Skills
- Programming Languages
- Frameworks
- Tools
- Skill Score
- Technical Evaluation

---

## 2️⃣ Education Agent

Extracts and evaluates:

- Degree
- College
- CGPA / GPA
- Certifications
- Education Score

---

## 3️⃣ Experience Agent

Analyzes:

- Projects
- Internship Experience
- Technologies Used
- Practical Knowledge
- Experience Score

---

## 4️⃣ Salary Agent

Predicts:

- Experience Level
- Recommended Job Role
- Expected Salary Range
- Salary Score

---

## 5️⃣ JD Matching Agent

Compares Resume with Job Description.

Returns:

- ATS Score
- Resume Match %
- Matching Skills
- Missing Skills
- Recommendations

---

## 6️⃣ Resume Improvement Agent

Provides AI-based suggestions including:

- Resume Strengths
- Weaknesses
- Missing Sections
- ATS Keywords
- Resume Improvements
- Overall Feedback

---

# 📊 Dashboard Features

The Streamlit dashboard includes:

- Resume Score
- Hiring Decision
- Agent Scores
- Skill Analysis
- Education Analysis
- Experience Analysis
- Salary Prediction
- ATS Matching
- Resume Improvements
- PDF Report Download

---

# 🛠️ Tech Stack

### Programming

- Python

### AI

- Google Gemini 2.5 Flash

### Multi-Agent Framework

- LangGraph

### Web Framework

- Streamlit

### PDF Processing

- PyPDF2

### PDF Report Generation

- ReportLab

### Environment Management

- python-dotenv

---

# 📂 Project Structure

```
Resume-Screening-AI
│
├── agents
│   ├── skill_agent.py
│   ├── education_agent.py
│   ├── experience_agent.py
│   ├── salary_agent.py
│   ├── jd_agent.py
│   └── improvement_agent.py
│
├── graph
│   ├── workflow.py
│   └── state.py
│
├── parser
│   ├── pdf_parser.py
│   └── jd_parser.py
│
├── prompts
│   ├── skill_prompt.py
│   ├── education_prompt.py
│   ├── experience_prompt.py
│   ├── salary_prompt.py
│   ├── jd_prompt.py
│   └── improvement_prompt.py
│
├── reports
│   └── pdf_report.py
│
├── services
│   └── gemini_client.py
│
├── utils
│   └── text_cleaner.py
│
├── sample_data
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Resume-Screening-AI.git
```

Go inside the project

```bash
cd Resume-Screening-AI
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 📈 Workflow

```
Upload Resume
        │
Upload Job Description
        │
Resume Parsing
        │
LangGraph Multi-Agent Workflow
        │
Skill Analysis
Education Analysis
Experience Analysis
Salary Prediction
JD Matching
Resume Improvement
        │
Final Recommendation
        │
Interactive Dashboard
        │
Download PDF Report
```

---

# 📄 PDF Report

The application generates a professional PDF report containing:

- Resume Score
- Hiring Decision
- Skill Analysis
- Education Analysis
- Experience Analysis
- Salary Prediction
- ATS Matching
- Resume Improvement Suggestions

---

# 🎯 Applications

This project can be used for:

- AI Resume Screening
- Recruitment Automation
- ATS Evaluation
- HR Resume Analysis
- Placement Cell Resume Review
- Career Guidance Platforms

---

# 🔮 Future Enhancements

- Interview Question Generator
- AI Resume Chatbot
- LinkedIn Profile Analysis
- GitHub Profile Analysis
- Multiple Resume Ranking
- Batch Resume Screening
- Email Report Generation
- OCR Support for Scanned Resumes
- Docker Deployment
- Cloud Deployment (AWS/Azure/GCP)

---

# 👨‍💻 Developed By

**Navyashree S J**

Electronics and Communication Engineering  
Nitte Meenakshi Institute of Technology

GitHub: https://github.com/Navyashree-21

---

# ⭐ If you found this project useful

Please consider giving this repository a ⭐ on GitHub.
