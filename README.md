# Python-Subscriber_Analysis
Subscriber analysis of cellular networks by geolocation analysis.

# About
Python-Subscriber_Analysis is a program to analysis subscriber of cellular network using raw data of GroundHog CovMo. Main objective of this program to optimize and improvement subscriber experience by verify the antenna design whether already proper or not. Also give recommendation related to network capacity expanding. Raw data of GroundHog CovMo contains several info related to coordinate position and count of subscriber in certain range time (daily / hourly). Main concept of this program is get insight position the subscriber relative to antenna (nearest site cover) using geometry analysis (vector analysis). Subscriber position classified by four quadrant and subscriber density category in each quadrant and aggregate them to site level. Illustration as shown below.

<img width="357" alt="image1" src="https://user-images.githubusercontent.com/97805726/180597700-d5252fa1-80a1-40c5-8363-758371bf9cd8.png">

# Prerequisites
Before you begin the program, you have meet the requirement:
- Installed Python 3.xx and main modules / libraries
- Python IDE (Jupyter or Spyder or PyCharm or Microsoft Visual Code) with latest version is better
- Installed QGIS
- Raw data with header as similar to GroundHog CovMo data as attached in repo

# Running Program
- Copy script in repo (app.py) and paste to IDE (script editor)
- Change directory of raw data and output csv file as local PC you run

# Release History
- 0.0.1: Setup (beta version)
- 0.0.2: Finalizing the script and change append method

# Contributors
- https://docs.python.org/3.7/tutorial/index.html
- https://www.geeksforgeeks.org/python-programming-language/?ref=shm

# Contact
You can reach me at makmura19@gmail.com
