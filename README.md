# Skill Mapper

Welcome to Skill Mapper - your ultimate toolkit for exploring and analyzing the dynamic landscape of tech skills in the job market!

## Overview

Skill Mapper is a data engineering project tailored specifically for the tech industry. It offers comprehensive insights into the skills demanded by various tech job roles across different locations. Whether you're a software developer, data scientist, IT professional, or aspiring tech enthusiast, Skill Mapper empowers you to navigate the ever-evolving world of tech skills with ease.

## Key Features

- **Personalized Insights:** Specify your desired tech job role and location to tailor your exploration.
- **Data Collection:** Utilizes advanced web scraping techniques to gather up-to-date job data from leading tech job boards and websites.
- **Data Transformation and Cleaning:** Ensures data accuracy and reliability through meticulous cleaning and transformation processes.
- **Interactive Visualization:** Engage with dynamic visualizations in Power BI to uncover trends and patterns in tech skill demand.
- **Exportable Reports:** Save and share your findings for future reference or collaboration.

## Usage

1. **Clone the Repository:**
   `git clone https://github.com/asparsh607/skill-mapper.git`
2. **Change the Current Directory:**
   `cd skill-mapper/`
3. **Install Dependencies:**
   `pip install -r requirements.txt`
4. **Run the Project:**
   `python main.py`

## Power BI Integration

1. **Open Power BI:**
    Open Power BI. This step is typically required only once for initial setup.
2. **Transform Data:**
    Go to the Home tab.
    Select "Transform Data" in the toolbar.
    Select "FileName" Table:

    In the Queries pane on the left side, select the "FileName" table.
    Open Advanced Editor:
        Go to the View tab.
        Inside the View tab, click on "Advanced Editor".
3. **Copy Address from File:**
    Open the file named current_directory_location.txt.
    Copy the address from the file.
    Paste Address in Source Variable:

    Paste the copied address into the Source variable within the 'let' block.
    Ensure to enclose the address in double quotes.

4. **Finish Editing:**

    Click "Done" to finish editing the script.
    Go back to the Home tab.
    Select "Close & Apply" to apply the changes.

5. **Visualize Data:**

    Open Job Analytics Dashboard:
    Open the job_analytics.pbix file to view the Visualization.

6. **Refresh Data:**

    After opening job_analytics.pbix, remember to refresh the data to ensure you have the latest updates.
    This step is crucial for subsequent runs to reflect the updated data.
   
7. **Explore and Analyze:**

    Utilize the visualizations in Power BI to explore and analyze the tech skills landscape.

8. **Save and Document Insights:**

    Save your findings and document any insights obtained from the analysis.

## Contributing
Contributions are welcome! If you have any ideas for improvement or new features, feel free to submit a pull request.

## License
This project is licensed under the MIT License.
