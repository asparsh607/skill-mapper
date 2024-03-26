from bs4 import BeautifulSoup
import pandas as pd
import re
from config_files.technologies import technologies

def trim_string(input_string):
    if ',' in input_string:
        return input_string.split(',', 1)[0].strip()
    else:
        return input_string

def extract_skills(job_description, skills_list):
    extracted_skills = []
    for skill in skills_list:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, job_description, re.IGNORECASE):
            extracted_skills.append(skill)
    if len(extracted_skills) == 0:
        return ["n/a"]
    return extracted_skills

def transform_jobs():
    # Open the file and read the content
    with open('job_data/job_data.txt', 'r', encoding="utf-8") as file:
        soup = BeautifulSoup(file.read(), 'lxml')

    meta_information = soup.find_all('div', class_='Qk80Jf')
    company_name = soup.find_all("div", class_="nJlQNd")
    job_description = soup.find_all('div', class_=["YgLbBe", "YRi0le"])
    job_title = soup.find_all("h2")
    more_info = soup.find_all('div', class_=['ocResc', 'KKh3md'])
    date_posted = []
    type_of_job = []
    salary_information = []
    misc_info = []
    aggregated_from = []
    job_location = []

    for info in meta_information:
        if "via" in info.text:
            aggregated_from.append(info.text)
        else:
            location = info.text
            if "others)" in location or "other)" in location:
                index_of_parentheses = location.find('(')
                if index_of_parentheses != -1:
                    substring_before_parentheses = location[:index_of_parentheses-1]
                    job_location.append(trim_string(substring_before_parentheses))
                else:
                    job_location.append(trim_string(location))
            else:
                    job_location.append(trim_string(location))

    # Create lists to store data
    data = {
        'Serial No': [],
        'Job Title': [],
        'Company Name': [],
        'Job Location': job_location,
        'Skills Required': [],
        'Aggregated From': aggregated_from,
        'Date Posted': [],
        'Type of Job': [],
        'Salary Information': [],
        'Miscellaneous Info': []
    }

    for index in range(len(company_name)):
        data['Serial No'].append(index)
        data['Job Title'].append(job_title[index].text)
        data['Company Name'].append(company_name[index].text)
        data['Skills Required'].append(extract_skills(job_description[index].text, technologies))

    for index, element in enumerate(more_info):
        if index % 2 == 0:
            span_element = element.find('span', class_="LL4CDc")
            if span_element:
                b = span_element.text
                if "ago" in b:
                    data['Date Posted'].append(b)
                    data['Type of Job'].append("Not Specified")
                    data['Salary Information'].append("Not Specified")
                    data['Miscellaneous Info'].append("Not Specified")
                elif "year" in b or "month" in b:
                    data['Salary Information'].append(b)
                    data['Date Posted'].append("Not Specified")
                    data['Type of Job'].append("Not Specified")
                    data['Miscellaneous Info'].append("Not Specified")
                elif any(keyword in b for keyword in ("Full", "Part", "work", "Work")):
                    data['Type of Job'].append(b)
                    data['Date Posted'].append("Not Specified")
                    data['Salary Information'].append("Not Specified")
                    data['Miscellaneous Info'].append("Not Specified")
                else:
                    data['Miscellaneous Info'].append(b)
                    data['Type of Job'].append("Not Specified")
                    data['Date Posted'].append("Not Specified")
                    data['Salary Information'].append("Not Specified")

    # Create DataFrame
    df = pd.DataFrame(data)

    # Save DataFrame to CSV
    df.to_csv('job_data/job_data.csv', index=False)
