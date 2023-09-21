# -*- coding: utf-8 -*-
"""Resume Builder.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/152QJBAfB9Za_bLrhhnb8K5DT_qs8dxx7
"""

class ResumeBuilder:
    def __init__(self):
        self.basic_info = {}
        self.education_details = []
        self.work_experience = []

    def your_basic_info(self):
        print("Enter your basic information:")
        self.basic_info['name'] = input("Name: ")
        self.basic_info['email'] = input("Email: ")
        self.basic_info['phone'] = input("Phone: ")
        self.basic_info['address'] = input("Address: ")

    def your_education_details(self):
        print("Enter your education details: (enter 'q' to stop):")
        while True:
            degree = input("Your degree: ")
            if degree.lower() == 'q':
                break
            institute = input("Institute: ")
            start_date = input("Start Date: ")
            end_date = input("End Date: ")
            subject = input("Subject: ")
            self.work_experience.append({
                'degree': degree,
                'institute': institute,
                'start_date': start_date,
                'end_date': end_date,
                'subject': subject
            })

    def your_work_experience(self):
        print("Enter your work experience (enter 'q' to stop):")
        while True:
            job_title = input("Job Title: ")
            if job_title.lower() == 'q':
                break
            company = input("Company: ")
            start_date = input("Start Date: ")
            end_date = input("End Date: ")
            responsibilities = input("Responsibilities: ")
            self.work_experience.append({
                'job_title': job_title,
                'company': company,
                'start_date': start_date,
                'end_date': end_date,
                'responsibilities': responsibilities
            })

    def generate_resume(self):
        resume = f"Resume for {self.basic_info['name']}\n"
        resume += f"Email: {self.basic_info['email']} | Phone: {self.basic_info['phone']}\n"
        resume += f"Address: {self.basic_info['address']}\n\n"
        resume += "Education:\n"
        for study in self.education_details:
            resume += f"{study['degree']} at {study['institute']}\n"
            resume += f"{study['start_date']} - {study['end_date']}\n"
            resume += f"Studied {study['subject']}\n\n"
        for experience in self.work_experience:
            resume += f"{experience['job_title']} at {experience['company']}\n"
            resume += f"{experience['start_date']} - {experience['end_date']}\n"
            resume += f"Responsible for {experience['responsibilities']}\n\n"
        return resume

def main():
    print("Welcome to the Resume Builder!")
    builder = ResumeBuilder()

    builder.your_basic_info()
    builder.your_education_details()
    builder.your_work_experience()

    resume = builder.generate_resume()
    print("\nGenerated Resume:\n")
    print(resume)

#Lun the cde for a small resume.
if __name__ == "__main__":
    main()