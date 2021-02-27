"""
Python program to train a dataset and select for ideal function out of it.
And use the four ideal function to select best fit function out of a test set
"""
# importing needed libraries 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import text
import bokeh
from bokeh.plotting import figure, output_file, show
from random import seed
from random import randint
import numpy as np
import pandas as pd
import math
import os
import glob
import csv


"""
Creating a class that hold constructor to connect of database
"""
class dbconnect(object):
    #constructor of dbconnect class
    def __init__(self, engine, meta, echo):
        self.engine = create_engine(engine) 
        self.meta = meta
        self.echo = echo
                  
"""
Creating a class table to hold all the methods of
that will be use to create tables in the database

This class will inherite from dbconnect to get the connecting 
string to the database

"""
class tables(dbconnect):
    #constructor of tables class inherited from dbconnect class
    def __init__(self, engine, meta, echo):
        super().__init__(engine,meta,echo)

    def trainingset_table(self):
        print("Creating table.......")
        try:
            """
            create table train_table(
                X float primary key,
                Y1 float,
                Y2 float,
                Y3 float,
                Y4 float
            )
            """         
            
            traintable = Table(
                'train_table', self.meta, 
                Column('X', Float, primary_key = True), 
                Column('Y1', Float), 
                Column('Y2', Float),
                Column('Y3', Float),
                Column('Y4', Float),
            )
            self.meta.create_all(self.engine)
            #print statement to confirm the table is succefully created
            print("Finish creating train_table")
        except SQLAlchemyError as error:
            #displaying any syntax error that may occour
            print(error)
        return traintable
    # def inserData(self,*args):
        
    
    #creating a method to check if a table exit in the database
    def table_exist(self,table_name):
        ret = self.engine.has_table(table_name)
        return ret

"""
Creating a class a class to load all csv files from the parent directory

"""
class load_file(object):
    #constructor of class load_file
    def __init__(self,path):
        self.path = path  
    # method to hold all csv files in the parent folder or directory
    def load_data(self):
        path = self.path
        extension = 'csv'
        os.chdir(path)
        data = glob.glob('*.{}'.format(extension))     
        return data

          

#main function for method calling
def main():
    # creating instance of tables class and passing on database connection string
    mytables = tables('sqlite:///writtenassignmentdatabase.db',MetaData(),True)
    t = mytables.trainingset_table()
    

    #declaring lists to hold each column of the train dataset
    trainset_X = []; trainset_Y1 = []; trainset_Y2 = []; trainset_Y3 = []; trainset_Y4 = [];

    """
    Creating instance of load_file class 
    passing the path of the directory of all csv files it the construstor of load_files as argument
    invoking load_data() method which returns list of all the csv files in the directory 
    """
    #instance of load_file class
    getData = load_file('C:/Users/KofiAgyemangOpambour/Desktop/python_project_work')
    csv_files = getData.load_data()

    #looping through all the csv files, opening them and read all the data in the files
    for file in csv_files:
        with open(file, 'r') as myFiles:
            print("Reading data from file: {}".format(file))
            #skipping the first row in the file
            next(myFiles)
            #variable to count the number of records inserted into the tables in the database 
            no_records = 0
            #using for loop to read the records in the all the csv files
            for data in myFiles:
                #splitting files into individual index in memory
                splitFile = data.split(',')
                #verifying if the first file is train data
                if(file == 'train.csv'):
                    #loading the columns of train data into different lists
                    trainset_X.append(splitFile[0])
                    trainset_Y1.append(splitFile[1])
                    trainset_Y2.append(splitFile[2])
                    trainset_Y3.append(splitFile[3])
                    trainset_Y4.append(splitFile[4])
                    """
                    Checking if train table exit on the database
                    if Yes, the process should continue to avoid duplicating record on the table
                    if No, the flow moves to else block, where train_table will be created 
                    and insert records from the train csv file into it
                    """
                    if(mytables.table_exist("train_table")):
                        continue
                    else:
                        t = mytables.trainingset_table
                        ins = t.insert().values(X = splitFile[0], Y1 = splitFile[1], Y2 = splitFile[2], Y3 = splitFile[3], Y4 = splitFile[4])
                        conn = mytables.engine.connect()
                        result = conn.execute(ins)
                        no_records += 1




if __name__ == '__main__':
    main() 















