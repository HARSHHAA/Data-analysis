This project investigates the impact of celebrity endorsements on the revenue growth of Indian companies across three major sectors: Automotive & Transportation, Manufacturing & Engineering, and Consumer Goods & Retail. Using YouTube Data API v3, we analyze ads published between 2021–2024 on official company YouTube channels and evaluate whether celebrity endorsements significantly affect business outcomes.

Objectives
Collect and analyze YouTube ad data of 30 Indian companies using the YouTube Data API.
Identify ads with celebrity endorsements and compare them with non-celebrity campaigns.
Measure revenue changes pre- and post-campaign using statistical methods (t-test and Welch's t-test).
Determine the ROI and effectiveness of celebrity-driven digital advertising.

Dataset
Source: YouTube Data API v3
Data Points: Video title, URL, views, likes, comments, upload date

Sectors:
Automotive & Transportation
Manufacturing & Engineering
Consumer Goods & Retail

Time Period: 2021 to 2024
Selection: 100 videos collected per company; top 10 (by views) used for analysis

Methodology
API Integration
Official YouTube channel IDs were used to ensure data was from verified company sources.

Data Collection
Collected metadata such as video views, likes, and upload dates using YouTube Data API v3.

Celebrity Detection
Used keyword matching and manual checks to classify videos as celebrity-endorsed or not.

Statistical Analysis
Applied t-tests and Welch’s t-tests to compare revenue changes between celebrity and non-celebrity campaigns.

Validation
Videos were manually reviewed to remove unofficial content or noise from the dataset.

Resuls
T-Test: No statistically significant difference in average revenue before and after celebrity endorsements.
Welch’s T-Test: No significant revenue difference between companies using celebrities and those that didn’t.

Conclusion: Celebrity endorsements did not lead to a substantial impact on revenue across all three sectors.

Project Structure

data/
└── company_channels.csv (Company names with their official YouTube channel IDs)
scripts/
├── youtube_api_extraction.py (Code for YouTube data extraction)
├── celebrity_detection.py (Logic to detect celebrity involvement)
└── revenue_analysis.py (Statistical analysis using t-tests)
THE CELEBRITY SALES GAME.docx (Detailed report)
README.md (Project documentation)

Technologies Used
Python 3.x
YouTube Data API v3
Pandas and NumPy
SciPy and Statsmodels
Matplotlib and Seaborn
Statistical Summary

Hypotheses:
Null Hypothesis (H₀): Celebrity endorsements do not significantly affect revenue.
Alternative Hypothesis (H₁): Celebrity endorsements significantly affect revenue.

Test Results:

T-test and Welch’s t-test performed on revenue changes.
All p-values were greater than 0.05, so we failed to reject the null hypothesis.

Conclusion: There was no statistically significant difference in revenue between celebrity-endorsed and non-endorsed campaigns
