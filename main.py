from parser.pdf_parser import extract_text_from_pdf
from utils.text_cleaner import clean_text

from graph.workflow import build_graph
from reports.report_formatter import ReportFormatter


def main():

    # Step 1: Read Resume
    resume = extract_text_from_pdf(
        "sample_data/sample_resume.pdf"
    )

    # Step 2: Clean Resume Text
    resume = clean_text(resume)

    # Step 3: Run LangGraph Workflow
    graph = build_graph()

    result = graph.invoke(
        {
            "resume": resume
        }
    )

    # Step 4: Print Individual Agent Reports
    ReportFormatter.print_skill_report(result["skill"])

    ReportFormatter.print_education_report(result["education"])

    ReportFormatter.print_experience_report(result["experience"])

    ReportFormatter.print_salary_report(result["salary"])

    # Step 5: Print Final Supervisor Report
    ReportFormatter.print_supervisor_report(result)


if __name__ == "__main__":
    main()