import pandas as pd
from datetime import datetime

# Function to create a job application spreadsheet
def create_job_application_sheet(file_name):
    # Create a DataFrame with the specified columns
    columns = [
        "Company Name",
        "Job Title",
        "Application Date",
        "Contact Person",
        "Application Method",
        "Job Description Link/Attachment",
        "Resume Submitted",
        "Cover Letter Submitted",
        "Follow-up Date",
        "Status",
        "Interview Date",
        "Interview Notes",
        "Outcome",
        "Salary/Compensation",
        "Location",
        "Skills/Qualifications Match",
        "Website/LinkedIn Page",
        "Additional Notes",
        "Source",
        "Networking Connections",
    ]

    df = pd.DataFrame(columns=columns)

    # Save the DataFrame to an Excel file
    df.to_excel(file_name, index=False, engine="openpyxl")

    print(f"Job application spreadsheet '{file_name}' created successfully.")

# Generate a unique filename based on the current date
today_date = datetime.now().strftime("%Y%m%d")
file_name = f"Job_Application_Tracker_{today_date}.xlsx"

# Call the function to create the spreadsheet
create_job_application_sheet(file_name)
