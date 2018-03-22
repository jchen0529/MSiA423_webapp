
# Capital Bikeshare Demand Prediction Flask App
===============================================

## Project Objective 
Understand the process involved in building and deploying a flask web app. The app's focus is to predict capital bikeshare demand to inform users and bikeshare officials.

## Team Members
* Developer: Jamie Chen
* Product Owner: Wenjing Yang
* QA: Matt Gallagher

## Project Charter
Enhance the utilization of DC capital bikeshare by predicting the usage of bikes ahead of time. This will benefit the community through:
* Help tourists/residents plan for transportation ahead of time
* Inform DC capital bikeshare on bike occupancy for better resource allocation
* Success Criteria: RMSLE. 

## Data
The raw data is from [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset). 
I used `Jupyter notebook` to do some EDA and clean the raw data (code in `develop/2011_12 bikeshare data.ipynb`). 

## Pivotal Tracker
[Link to Pivotal Tracker](https://www.pivotaltracker.com/reports/v2/projects/2141914/epics)


Project Organization
------------

    ├── README.md                     <- The top-level README for developers using this project.
    ├── requirements.txt              <- requirements file
    ├── application.py                <- run webapp locally
    ├── create_db.py                  <- creates a local database based on specification
    ├── config.py                     <- database configuration info
    ├── msiapp                        <- Everything related to front-end web app
      ├── __init__.py                	   <- initialize the application and sql database
      ├── models.py                      <- specifies the sqlite 3 database table schema
      ├── README.md               		   <- explains the html files in templates
	  ├── templates                		  <- html files for webpages
	  ├── static                		    <- folder for static files
    ├── develop                       <- Everything related to data analysis and model build                 
      ├── data                			     <- UCI 2011_2012 bikeshare data (hour.csv)
      ├── 2011_12 bikeshare data.ipynb   <- Jupyter notebook analysis that includes EDA and model building
      ├── data.py        			           <- Readin data and prepare data frame for modeling
      ├── model.py                       <- Main function to train a random forest model and export it
      ├── rf.pkl                         <- Final random forest model saved as pkl file
      ├── predict.py                     <- predict function applied to user input
--------

## Software & Package requirements
Things you need to get it started:
* [conda](https://anaconda.org/): Either Anaconda or Miniconda is fine for this project.
* [git](https://git-scm.com/): You will most likely need version control.

## Set up the app
Below is a brief tutorial to set up the app in a AWS EC2 or Linux. For other systems, the general steps should be the same, but small changes might be needed. 

1. Update. Install git and conda if you have not done so.

    `sudo yum update`
    `sudo yum install git`
    `wget https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh
    bash Anaconda3-5.1.0-Linux-x86_64.sh`

2. Clone this GitHub repository to local.

3. Go to [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset) to downlowd the data to the directory.

4. Go into the directory, and create a conda environment with all required packages and dependecies.

    `conda env create -f myenv`

Then, activate the conda environment by entering `source activate myenv`.

5. Now enter `python application.py`. The app should be running. Have fun!

## Website link
[Link to the web app](http://ec2-54-175-5-62.compute-1.amazonaws.com:5000)


## Unit Testing
We performed unit testing (`develop/data.py`) for `develop/predict.py` file. The functions  we tested are:
* `preprocess()`
* `predictresponse()`

## Logging
See develop folder data.log for logging added to data preprocessing
(Logging as also been added to application.py)






