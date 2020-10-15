# CS586-CensusAnalysis
CS586 - Big Data Analysis Census Data Analysis

## Overview
This project analyzes subsets of the 2010 Census Data set. It was created with the goal of in house processing, 
meaning that this program does not use any API calls.

## Needed Resources
The following is a list of resources needed in order to perform the included analysis:

- 2010 Census Summary File 01 Urban Rural Update - [Link to Dataset](https://www2.census.gov/census_2010/04-Summary_File_1/Urban_Rural_Update/)
- Header Definitions for Summary File (Can be decoded from SAS File) - [Link to File](https://www2.census.gov/census_2010/01-Redistricting_File--PL_94-171/pl_geohd_2010.sas)
- 2010 Census Summary File 01 Technical Documentation - [Link to File](https://www.census.gov/prod/cen2010/doc/sf1.pdf)
- FIPS State and County Codes Definitions - [Link to File](https://www.census.gov/prod/techdoc/cbp/cbp95/st-cnty.pdf)

## Dependencies
The following is a list of dependencies to process and analyze the dataset:

- pandas
- pymongo

## Setup
The following needs to be done before any code is ran:

1. The urban dataset needs to be in a folder called Census_Data.
    - Each folder will have a path structure like the following: Census_Data/Alabama
2. The data from the FIPS State and County Codes Definition needs to be converted to an n by 3 dataframe
    - It should have the following structure: State_Code County_Code County_Name
    - Everything is separated by spaces
    - The file should be named Census_Data/FIPS_ST_COU_Area-Name.txt
3. The Header Definitions SAS file should be stored as a text file named Census_Data/GeoHeaders.txt
    - It should have the following structure: @1 FILEID $6. /\*File Identification*/
    - This will ensure that the geo file in each location folder is read in properly
4. An empty State_JSONs folder should be created for all JSONs to be dumped into.

## Running the Analysis
The code needs to be ran in the following order. If your data is already in MongoDB you can skip to the __ step:

1. First run unzip_tool.py. This will unzip every folder automatically. Be warned that the entire dataset is over 100GB
2. Next run process_geo_files.py. This will convert the geo files into a pandas readable file. This process is very memory intensive
3. First ensure that a mongo database is created with the name census. Then ensure that the mongo_info.py file contains the correct connection information
4. Next run process_fips_data.py. This will convert the FIPS dataset into a JSON and upload it to the MongoDB
5. Then run auto_run.py. This will convert the first three state files into one JSON file for each state. This will take some time to do.
6. Next run the mongo_import.py which will import the JSON data into the Mongo database. This will take some time.

## Credits
Created by Kevin Bimonte