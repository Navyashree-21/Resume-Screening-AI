import os
import tempfile

import streamlit as st

from graph.workflow import build_graph
from parser.pdf_parser import extract_text_from_pdf
from parser.jd_parser import extract_jd_text
from utils.text_cleaner import clean_text
from reports.pdf_report import PDFReport


# ==========================================================
# Utility Function
# ==========================================================

def save_uploaded_file(uploaded_file):

    suffix = ".pdf"

    if uploaded_file.name.endswith(".txt"):
        suffix = ".txt"

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix
    )

    temp_file.write(uploaded_file.getbuffer())

    temp_file.close()

    return temp_file.name


# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Resume Screening AI",
    page_icon="📄",
    layout="wide"
)

# ==========================================================
# Sidebar
# ==========================================================

with st.sidebar:

    st.title("📄 Resume Screening AI")

    st.success("🟢 Backend Connected")

    st.divider()

    st.subheader("Technology Stack")

    st.markdown("""
- LangGraph
- Google Gemini 2.5 Flash
- Streamlit
- Python
""")

    st.divider()

    st.info(
        """
Upload a Resume and an optional Job Description.

Click **Analyze Resume** to start the AI screening.
"""
    )


# ==========================================================
# Header
# ==========================================================

st.title("📄 Resume Screening AI")

st.caption(
    "AI-powered Resume Evaluation using LangGraph and Google Gemini"
)

st.divider()


# ==========================================================
# Upload Section
# ==========================================================

st.subheader("📂 Upload Documents")

resume = st.file_uploader(
    "Resume (PDF)",
    type=["pdf"]
)

jd = st.file_uploader(
    "Job Description (Optional)",
    type=["pdf", "txt"]
)

st.divider()


# ==========================================================
# Analyze Button
# ==========================================================

analyze = st.button(
    "🚀 Analyze Resume",
    use_container_width=True
)

if analyze:

    if resume is None:

        st.error("Please upload a Resume.")

        st.stop()

    # -----------------------------------
    # Resume
    # -----------------------------------

    resume_path = save_uploaded_file(resume)

    resume_text = extract_text_from_pdf(
        resume_path
    )

    resume_text = clean_text(
        resume_text
    )

    # -----------------------------------
    # Job Description
    # -----------------------------------

    jd_text = ""

    jd_path = None

    if jd is not None:

        jd_path = save_uploaded_file(jd)

        if jd.name.endswith(".pdf"):

            jd_text = extract_jd_text(jd_path)

        else:

            with open(
                jd_path,
                "r",
                encoding="utf-8"
            ) as file:

                jd_text = file.read()

        jd_text = clean_text(
            jd_text
        )

    # -----------------------------------
    # Run LangGraph
    # -----------------------------------

    with st.spinner("🤖 AI Agents are analyzing the resume..."):

        graph = build_graph()

        result = graph.invoke(
            {
                "resume": resume_text,
                "jd": jd_text
            }
        )

    st.success("✅ Analysis Completed Successfully!")

    # ==========================================================
    # Final Decision
    # ==========================================================

    st.divider()

    st.header("📊 Final Decision")

    left, right = st.columns([2, 1])

    with left:

        st.metric(
            "Overall Resume Score",
            f"{result['overall_score']}/100"
        )

        st.progress(
            result["overall_score"] / 100
        )

    with right:

        decision = result["decision"]

        if decision == "APPROVE":

            st.success("✅ APPROVED")

        elif decision == "HOLD":

            st.warning("🟡 HOLD")

        else:

            st.error("❌ REJECT")


    # ==========================================================
    # Agent Scores
    # ==========================================================

    st.divider()

    st.header("📈 Agent Scores")

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "🧠 Skill Score",
            f"{result['skill']['skill_score']}/100"
        )

        st.progress(
            result["skill"]["skill_score"] / 100
        )

        st.metric(
            "🎓 Education Score",
            f"{result['education']['education_score']}/100"
        )

        st.progress(
            result["education"]["education_score"] / 100
        )

    with c2:

        st.metric(
            "💼 Experience Score",
            f"{result['experience']['experience_score']}/100"
        )

        st.progress(
            result["experience"]["experience_score"] / 100
        )

        st.metric(
            "💰 Salary Score",
            f"{result['salary']['salary_score']}/100"
        )

        st.progress(
            result["salary"]["salary_score"] / 100
        )


    # ==========================================================
    # Tabs
    # ==========================================================

    tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs(
    [
    "🧠 Skills",
    "🎓 Education",
    "💼 Experience",
    "💰 Salary",
    "📋 JD Match",
    "✨ Resume Improvement"
    ]
    )


    # ==========================================================
    # Skills Tab
    # ==========================================================

    with tab1:

        st.subheader("🧠 Skill Assessment")

        st.metric(
            "Skill Score",
            f"{result['skill']['skill_score']}/100"
        )

        st.progress(
            result["skill"]["skill_score"] / 100
        )

        st.divider()

        st.subheader("Analysis")

        st.write(
            result["skill"]["reason"]
        )


    # ==========================================================
    # Education Tab
    # ==========================================================

    with tab2:

        st.subheader("🎓 Education")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Degree",
                result["education"]["degree"]
            )

            st.metric(
                "College",
                result["education"]["college"]
            )

        with col2:

            st.metric(
                "CGPA",
                result["education"]["gpa"]
            )

            st.metric(
                "Education Score",
                f"{result['education']['education_score']}/100"
            )

        st.divider()

        st.subheader("Certifications")

        for cert in result["education"]["certifications"]:

            st.success(cert)

        st.divider()

        st.subheader("Analysis")

        st.write(
            result["education"]["reason"]
        )

        # ==========================================================
        # Experience Tab
        # ==========================================================

        with tab3:

            st.subheader("💼 Project Experience")

            projects = result["experience"]["projects"]

            if projects:

                for project in projects:

                    if isinstance(project, dict):

                        st.markdown(
                            f"### 🚀 {project.get('name','Project')}"
                        )

                        if project.get("description"):

                            st.write(
                                project["description"]
                            )

                    else:

                        st.success(project)

            else:

                st.info("No projects available.")

            st.divider()

            st.metric(
                "Experience Score",
                f"{result['experience']['experience_score']}/100"
            )

            st.progress(
                result["experience"]["experience_score"] / 100
            )

            st.divider()

            st.subheader("Analysis")

            st.write(
                result["experience"]["reason"]
            )


        # ==========================================================
        # Salary Tab
        # ==========================================================

        with tab4:

            st.subheader("💰 Salary Prediction")

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Experience Level",
                    result["salary"]["experience_level"]
                )

                st.metric(
                    "Salary Score",
                    f"{result['salary']['salary_score']}/100"
                )

            with col2:

                st.metric(
                    "Recommended Role",
                    result["salary"]["recommended_role"]
                )

                st.metric(
                    "Expected Salary",
                    result["salary"]["salary_range_lpa"]
                )

            st.divider()

            st.subheader("Analysis")

            st.write(
                result["salary"]["reason"]
            )


        # ==========================================================
        # JD Match Tab
        # ==========================================================

        with tab5:

            st.subheader("📋 ATS Resume Match Report")

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Resume Match",
                    f"{result['jd_match']['match_percentage']}%"
                )

                st.progress(
                    result["jd_match"]["match_percentage"] / 100
                )

            with col2:

                st.metric(
                    "ATS Score",
                    f"{result['jd_match']['ats_score']}/100"
                )

                st.progress(
                    result["jd_match"]["ats_score"] / 100
                )

            st.divider()

            left, right = st.columns(2)

            with left:

                st.subheader("✅ Matching Skills")

                matching = result["jd_match"]["matching_skills"]

                if matching:

                    for skill in matching:

                        st.success(skill)

                else:

                    st.info("No matching skills found.")

            with right:

                st.subheader("❌ Missing Skills")

                missing = result["jd_match"]["missing_skills"]

                if missing:

                    for skill in missing:

                        st.error(skill)

                else:

                    st.success("No missing skills!")

            st.divider()

            st.subheader("💡 Recommendations")

            recommendations = result["jd_match"]["recommendations"]

            if recommendations:

                for rec in recommendations:

                    st.info(rec)

            else:

                st.success(
                    "Resume is well aligned with the Job Description."
                )

            st.divider()

            st.subheader("📝 Overall Analysis")

            st.write(
                result["jd_match"]["reason"]
            )


        # ==========================================================
        # Footer
        # ==========================================================

    st.divider()

    st.markdown(
        """
        <div style='text-align:center;color:gray;'>

        Resume Screening AI

        Built using ❤️ LangGraph • Gemini 2.5 Flash • Streamlit • Python

        </div>
        """,
        unsafe_allow_html=True
        )

    with tab6:

        improvement = result["improvement"]

        st.subheader("⭐ Resume Strengths")

        for item in improvement["strengths"]:
                st.success(item)

        st.divider()

        st.subheader("⚠ Weaknesses")

        for item in improvement["weaknesses"]:
                st.warning(item)

        st.divider()

        st.subheader("📌 Missing Sections")

        for item in improvement["missing_sections"]:
                st.error(item)

        st.divider()

        st.subheader("🚀 Resume Improvements")

        for item in improvement["resume_improvements"]:
                st.info(item)

        st.divider()

        st.subheader("🔑 ATS Keywords")

        cols = st.columns(3)

        keywords = improvement["keyword_suggestions"]

        for i, keyword in enumerate(keywords):
                cols[i % 3].success(keyword)

        st.divider()

        st.subheader("📝 Overall Feedback")

        st.write(
                improvement["overall_feedback"]
            )


    pdf_filename = "Resume_Screening_Report.pdf"

    PDFReport.generate(
            result,
            pdf_filename
        )

    with open(pdf_filename, "rb") as pdf:

            st.download_button(
                label="📄 Download AI Report",
                data=pdf,
                file_name="Resume_Screening_Report.pdf",
                mime="application/pdf",
                use_container_width=True
            )       
        # ==========================================================
        # Cleanup
        # ==========================================================

    os.remove(resume_path)

    if jd_path is not None:

        os.remove(jd_path)

    if os.path.exists(pdf_filename):

        os.remove(pdf_filename)