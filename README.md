
The Celebrity Sales Game
Revenue Impact of Celebrity-Endorsed YouTube Ads (2021–2024)

Introduction
The Celebrity Sales Game investigates the impact of celebrity endorsements in YouTube advertisements on the revenue growth of top Indian companies. Focused on three key sectors—Automotive & Transportation, Manufacturing & Engineering, and Consumer Goods & Retail—this project uses the YouTube Data API v3 to analyze advertisements published between 2021 and 2024. It compares the performance of celebrity-endorsed campaigns versus non-celebrity campaigns using statistical tests to evaluate business outcomes.

This study aims to answer a central question:
Do celebrity endorsements really translate into increased revenue for companies?

Project Overview
This project utilizes programmatic access to YouTube advertisement data via the YouTube Data API, followed by statistical analysis of company revenue to assess the value of celebrity involvement in digital marketing campaigns.

Key Components:
- YouTube Data API Integration: Automated data collection from verified company YouTube channels
- Sector Categorization: 30 companies grouped into 3 major sectors
- Metadata Extraction: Views, likes, comments, upload dates, and video links
- Celebrity Detection: Keywords and manual tagging used to classify celebrity presence
- Statistical Analysis: T-tests and Welch’s t-tests used to measure revenue change

Sectors and Companies
Automotive & Transportation
Tata Motors, Maruti Suzuki, Hero MotoCorp, TVS, SpiceJet, Indigo, Apollo Tyres, etc.

Manufacturing & Engineering
Tata Steel, JSW Steel, Indian Oil, Havells, Blue Star, MRF, HPCL, etc.

Consumer Goods & Retail
HUL, Dabur, Asian Paints, Britannia, Zomato, Nykaa, Bata, Emami, etc.

Methodology
1. Channel Identification
Official YouTube channel IDs were collected to avoid unofficial content.

2. Data Collection
The top 100 videos from each company between 2021 and 2024 were retrieved using the API.

3. Video Filtering
Top 10 videos per company were selected based on view count.

4. Celebrity Tagging
Keyword-based and manual review techniques used to classify ads as “celebrity-endorsed” or “non-celebrity.”

5. Revenue Analysis
Company revenue data was analyzed before and after ad release using t-tests and Welch's t-tests.

Results
T-Test
- Null Hypothesis: No significant revenue change due to celebrity endorsement.
- Result: All p-values > 0.05 → Failed to reject null hypothesis.

Welch’s T-Test
- Compared average revenue between companies using and not using celebrity endorsements for each year.
- Result: All p-values > 0.05 → No significant difference found.

Conclusion
Celebrity endorsements showed no statistically significant impact on revenue growth across any of the three sectors. These results challenge the belief that celebrity-backed ads always lead to better financial outcomes.

Project Structure
data/
- company_channels.csv (Official YouTube channel IDs)

scripts/
- youtube_api_extraction.py (YouTube API integration and video metadata collection)
- celebrity_detection.py (Identifies celebrity involvement in ads)
- revenue_analysis.py (Performs statistical analysis)

THE CELEBRITY SALES GAME.docx
Full project report


Technologies Used
- Python 3.x
- YouTube Data API v3
- Pandas, NumPy
- SciPy, Statsmodels
- Matplotlib, Seaborn

Statistical Summary
T-Test
- Purpose: Compare pre- and post-ad revenue for celebrity-endorsed campaigns
- Result: No significant difference in average revenue (p > 0.05)

Welch’s T-Test
- Purpose: Compare average revenue between celebrity and non-celebrity companies
- Result: No significant difference in yearly revenue (p > 0.05)

Final Interpretation
Celebrity-backed advertisements did not result in measurable financial advantage. Marketing strategies based on influencer or creative content alone may provide comparable returns.
