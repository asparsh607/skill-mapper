import time
from extract_jobs import scrape_jobs, format_string
from transform_jobs import transform_jobs
from config_files.countries import it_hubs_by_country
if __name__ == "__main__":
    job_title = input("Enter your Job Title: ")
    job_title = format_string(job_title)
    location = input("Enter Your Job Location Country: ")
    location = format_string(location)
    locations_dictionary = it_hubs_by_country
    if location in locations_dictionary:
        scrape_jobs(job_title, locations_dictionary.get(location))
    else:
        print(f"{location} not available in country list, you can add it in job_location/countries.py")
        exit()
    print("Cleaning and Transforming extracted data...")
    transform_jobs()
    print("Process Completed!")
    print("Please open job_analytics.pbix file to see Visualisation.")
    print("Do no forget to refresh the data!")
    time.sleep(10)