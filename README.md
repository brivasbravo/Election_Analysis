# Election_Analysis

## Project Overview

A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election and requires our assistance to analyze 
results to extract candidate winner and county results.

## Election-Audit Results

1. How many votes were cast in this congressional election?
	- Total Votes: **369,711**
2. Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
Breakdown of votes can be seen below:
	- Denver: **82.8% (306,055)**
	- Jefferson: **10.5% (38,855)**
	- Arapahoe: **6.7% (24,801)**
3. Which county had the largest number of votes?
	- Denver: **306,055**
4. Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
	- Charles Casper Stockham: **23.0% (85,213)**
	- Diana DeGette: **73.8% (272,892)**
	- Raymon Anthony Doane: **3.1% (11,606)**
5. Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
	- Winner: **Diana DeGette**
	- Winning Vote Count: **272,892**
	- Winning Percentage: **73.8%**

ADD PICTURE TO SHOW RESULTS
![election_results_txt](election_results_txt.png)

## Election-Audit Summary
 In a summary statement, provide a business proposal to the election commission on how this script can be
 used—with some modifications—for any election. Give at least two examples of how this script can be
 modified to be used for other elections.

The code created for this particular election is effective with helping analyze any election data set with minor tweaks.
The script itself can be applied to other data sets by simply switching the source of the data as seen below:

![election_datasource](election_datasource.png)

Script can also be adjusted from the county level to pull info instead at the city or state level as well. When data is recorded the second
column would instead be at the city or state level. See header below:

![election_header](election_header.png)


