
MSiA 423 AnalyticsValueChain Project
==============================

Goal: Understand the processes involved in building and deploying a web app
Project focus: Analyze DC Capital Bikeshare data to predict demands and deploy model 

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