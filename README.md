# LiveNamer

Application will request the Twitch.tv and YouTube Gaming API's and download stream information (title and viewer counts). This data will be written to a file and POSTed into the Microsoft Azure API for sentiment analysis (Text Analytics API endpoint). Upon receipt of the 
Azure sentiment scores, data will be written to file and analysis will be performed on this data.  

Necessary Filepath Changes:
**collectTwitch**: change 'test4.txt' to desired notepad file name. 
**data_cleaning.py**: filepath should be changed to the xlsx where "test4.txt" from collectTwitch was copied to. 
**postJSON.py**: change wb=openpyxl.load_workbook to the data_cleaning.py xlsx destination. 
**analysis.py**: convert xlsx files to csv and then change the pd.read_csv filepath to match the csv's created. 

**c_app and postJSON** please note that these files contain HTTP POST requests to an API endpoint with a 
real credit card attached to the data collection amounts. Extraordinarily high (>100,000) POST request counts will result
in real financial charges to the account holder. 

*.xlsx files* provided in order to showcase the data sets on which our analysis was done. 

Run Order:
1. collectTwitch.py 
2. collectYoutube.py
3. data_cleaning.py
4. postJSON.py
5. analysis.py
6. c_app.py


