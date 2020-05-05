# Project Name - Traffic Analysis of Mumbai City in last 7 Days

#### -- Project Status: [Active]
It is still in Active mode as i am trying to explore the concepts of applying predictive modelling in this project.

## Project Intro/Objective:
The purpose of this project is to visualise the traffic data of Mumbai city in last 7 days for every hour in the form of a visualisation heatmap chart.

### Methods Used:
* Data Exploration
* Data Wrangling
* Data Visualization
* Predictive Modeling

### Technologies Used:
* Python
* Pandas
* Pycharm
* Matplotlib
* Seaborn 

## Project Description:

### Prerequisites
  ### -> Dataset:
  * API for accessing data from TomTom website(https://api.midway.tomtom.com/ranking/live/IND_mumbai)
  
  ### -> Python Libraries:
  *  Python
  * Pandas
  * Pycharm
  * Matplotlib
  * Seaborn
  
### Workflow:
1. Using request module download the data for the city Mumbai.
2. Convert the response data into JSON obejct.
3. Create a Dataframe using Pandas from the JSON object.
4. Derive a resultant column using other columns including Traffic index Live, JamsDelay,Jamscount and JamsLength.
5. Create a Pandas grouby object using Weekday and Hour colum and perform unstack to give a look of pivot table.
6. Using Seaborn create a HeatMap object and import the grouby data as the input

## Expected Output:
 ![Traffic_HeatMap](https://github.com/jitpavi/Mumbai_Traffic_Analysis/blob/master/Traffic_HeatMap.jpg)

## Featured Notebooks/Analysis/Deliverables
* [Mum-Traffic_Analysisv1.0.py](https://github.com/jitpavi/Mumbai_Traffic_Analysis/blob/master/Mum-Traffic_Analysisv1.0.py)

## Versioning
Code version - v1.0

## Author:

* **Jitin Pavithran** - [jitpavi](https://github.com/jitpavi)

## Acknowledgments:

* https://www.tomtom.com/

## References:

* https://towardsdatascience.com/scraping-live-traffic-data-in-3-lines-of-code-step-by-step-9b2cc7ddf31f
