class ReportFormatter:

    @staticmethod
    def print_skill_report(skill):

        print("=" * 70)
        print("SKILL AGENT REPORT")
        print("=" * 70)

        print(f"\nSkill Score : {skill['skill_score']}/100")

        print("\nTechnical Skills:")

        for s in skill["technical_skills"]:
            print(f"✔ {s}")

        print("\nReason:")
        print(skill["reason"])

        print()


    @staticmethod
    def print_education_report(education):

        print("=" * 70)
        print("EDUCATION AGENT REPORT")
        print("=" * 70)

        print(f"\nDegree      : {education['degree']}")
        print(f"College     : {education['college']}")
        print(f"GPA         : {education['gpa']}")
        print(f"Score       : {education['education_score']}/100")

        print("\nCertifications:")

        for cert in education["certifications"]:
            print(f"✔ {cert}")

        print("\nReason:")
        print(education["reason"])

        print()


    @staticmethod
    def print_experience_report(experience):

        print("=" * 70)
        print("EXPERIENCE AGENT REPORT")
        print("=" * 70)

        print(f"\nExperience Score : {experience['experience_score']}/100")

        print("\nProjects:")

        for project in experience["projects"]:

            if isinstance(project, dict):
                print(f"✔ {project.get('name', 'Unknown Project')}")

            else:
                print(f"✔ {project}")
                
        print("\nInternships:")

        if experience["internships"]:

            for internship in experience["internships"]:
                print(f"✔ {internship}")

        else:
            print("No internships")

        print("\nTechnologies Used:")

        for tech in experience["technologies_used"]:
            print(f"✔ {tech}")

        print("\nReason:")
        print(experience["reason"])

        print()


    @staticmethod
    def print_salary_report(salary):

        print("=" * 70)
        print("SALARY AGENT REPORT")
        print("=" * 70)

        print(f"\nExperience Level : {salary['experience_level']}")
        print(f"Recommended Role : {salary['recommended_role']}")
        print(f"Expected Salary  : {salary['salary_range_lpa']}")
        print(f"Salary Score     : {salary['salary_score']}/100")

        print("\nReason:")
        print(salary["reason"])

        print()

    @staticmethod
    def print_supervisor_report(result):

        print("=" * 70)
        print("SUPERVISOR REPORT")
        print("=" * 70)

        print(f"\nOverall Score : {result['overall_score']}/100")

        print(f"Decision      : {result['decision']}")

        print("\nAgent Scores")

        print(f"Skill        : {result['skill']['skill_score']}")
        print(f"Education    : {result['education']['education_score']}")
        print(f"Experience   : {result['experience']['experience_score']}")
        print(f"Salary       : {result['salary']['salary_score']}")

        print()