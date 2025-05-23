import requests
import zipfile
import io
import pandas as pd

url = "http://0.0.0.0:8000/api"
question = """Sports Analytics for CricketPro
CricketPro Insights is a leading sports analytics firm specializing in providing in-depth statistical analysis and insights for cricket teams, coaches, and enthusiasts. Leveraging data from prominent sources like ESPN Cricinfo, CricketPro offers actionable intelligence that helps teams optimize player performance, strategize game plans, and engage with fans through detailed statistics and visualizations.

In the competitive world of cricket, understanding player performance metrics is crucial for team selection, game strategy, and player development. However, manually extracting and analyzing batting statistics from extensive datasets spread across multiple web pages is time-consuming and prone to errors. To maintain their edge and deliver timely insights, CricketPro needs an efficient, automated solution to aggregate and analyze player performance data from ESPN Cricinfo's ODI (One Day International) batting statistics.

CricketPro Insights has identified the need to automate the extraction and analysis of ODI batting statistics from ESPN Cricinfo to streamline their data processing workflow. The statistics are available on a paginated website, with each page containing a subset of player data. By automating this process, CricketPro aims to provide up-to-date insights on player performances, such as the number of duck outs (i.e. a score of zero), which are pivotal for team assessments and strategic planning.

As part of this initiative, you are tasked with developing a solution that allows CricketPro analysts to:

Navigate Paginated Data: Access specific pages of the ODI batting statistics based on varying requirements.
Extract Relevant Data: Use Google Sheets' IMPORTHTML function to pull tabular data from ESPN Cricinfo.
Analyze Performance Metrics: Count the number of ducks (where the player was out for 0 runs) each player has, aiding in performance evaluations.
Your Task
ESPN Cricinfo has ODI batting stats for each batsman. The result is paginated across multiple pages. Count the number of ducks in page number 22.

Understanding the Data Source: ESPN Cricinfo's ODI batting statistics are spread across multiple pages, each containing a table of player data. Go to page number 22.
Setting Up Google Sheets: Utilize Google Sheets' IMPORTHTML function to import table data from the URL for page number 22.
Data Extraction and Analysis: Pull the relevant table from the assigned page into Google Sheets. Locate the column that represents the number of ducks for each player. (It is titled "0".) Sum the values in the "0" column to determine the total number of ducks on that page.
Impact
By automating the extraction and analysis of cricket batting statistics, CricketPro Insights can:

Enhance Analytical Efficiency: Reduce the time and effort required to manually gather and process player performance data.
Provide Timely Insights: Deliver up-to-date statistical analyses that aid teams and coaches in making informed decisions.
Scalability: Easily handle large volumes of data across multiple pages, ensuring comprehensive coverage of player performances.
Data-Driven Strategies: Enable the development of data-driven strategies for player selection, training focus areas, and game planning.
Client Satisfaction: Improve service offerings by providing accurate and insightful analytics that meet the specific needs of clients in the cricketing world.
What is the total number of ducks across players on page number 22 of ESPN Cricinfo's ODI batting stats?"
file_path = "/home/gir/Desktop/tdsproj2/README.md"""

# files = {'file': open(file_path, 'rb')}
data = {'question': question}
response = requests.post(url,
    # files=files,
    data=data)
print(response.text)
