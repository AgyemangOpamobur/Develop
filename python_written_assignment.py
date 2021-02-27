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
        print("Creating train table.......")
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
            # return traintable.insert().values()
            # table = traintable.insert().values(X = data1, Y1 = data2, Y2 = data3, Y3 = data4, Y4 = data5)
            # conn = self.engine.connect()
            # result = conn.execute(table)

        except SQLAlchemyError as error:
            #displaying any syntax error that may occour
            print(error)
    
    #creating table ideal function 
    def idealfunction_table(self):
        print("Creating ideal table.................")
        try:
            idealtable = Table(
           'ideal_table', self.meta, 
           Column('X', Float, primary_key = True), 
           Column('Y1', Float), 
           Column('Y2', Float),
           Column('Y3', Float),
           Column('Y4', Float),
           Column('Y5', Float),
           Column('Y6', Float),
           Column('Y7', Float),
           Column('Y8', Float),
           Column('Y9', Float),
           Column('Y10', Float),
           Column('Y11', Float),
           Column('Y12', Float),
           Column('Y13', Float),
           Column('Y14', Float),
           Column('Y15', Float),
           Column('Y16', Float),
           Column('Y17', Float),
           Column('Y18', Float),
           Column('Y19', Float),
           Column('Y20', Float),
           Column('Y21', Float), 
           Column('Y22', Float),
           Column('Y23', Float),
           Column('Y24', Float),
           Column('Y25', Float),
           Column('Y26', Float),
           Column('Y27', Float),
           Column('Y28', Float),
           Column('Y29', Float),
           Column('Y30', Float),
           Column('Y31', Float),
           Column('Y32', Float),
           Column('Y33', Float),
           Column('Y34', Float),
           Column('Y35', Float),
           Column('Y36', Float),
           Column('Y37', Float),
           Column('Y38', Float),
           Column('Y39', Float),
           Column('Y40', Float),
           Column('Y41', Float), 
           Column('Y42', Float),
           Column('Y43', Float),
           Column('Y44', Float),
           Column('Y45', Float),
           Column('Y46', Float),
           Column('Y47', Float),
           Column('Y48', Float),
           Column('Y49', Float),
           Column('Y50', Float),
            )
            self.meta.create_all(self.engine)
            print("Finish creating ideal table")
        except SQLAlchemyError as error:
            print(error)
    
    #creating a method to check if a table exit in the database
    def table_exist(self,table_name):
        try:
            ret = self.engine.has_table(table_name)
            return ret
        except:
            print("The table does not Exist")
            return None
   
    
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
    # mytables.trainingset_table()
    
    # engine = create_engine('sqlite:///writtenassignmentdatabase.db', echo = False)
    engine = tables('sqlite:///writtenassignmentdatabase.db',MetaData(),True)
    # meta = MetaData()
    meta = engine.meta
    traintable =Table(
                  'train_table',meta, 
                 Column('X', Float, primary_key = True), 
                 Column('Y1', Float), 
                 Column('Y2', Float),
                 Column('Y3', Float),
                 Column('Y4', Float),
            )
    
    ideal_table = Table(
           'ideal_table',meta, 
           Column('X', Float, primary_key = True), 
           Column('Y1', Float), 
           Column('Y2', Float),
           Column('Y3', Float),
           Column('Y4', Float),
           Column('Y5', Float),
           Column('Y6', Float),
           Column('Y7', Float),
           Column('Y8', Float),
           Column('Y9', Float),
           Column('Y10', Float),
           Column('Y11', Float),
           Column('Y12', Float),
           Column('Y13', Float),
           Column('Y14', Float),
           Column('Y15', Float),
           Column('Y16', Float),
           Column('Y17', Float),
           Column('Y18', Float),
           Column('Y19', Float),
           Column('Y20', Float),
           Column('Y21', Float), 
           Column('Y22', Float),
           Column('Y23', Float),
           Column('Y24', Float),
           Column('Y25', Float),
           Column('Y26', Float),
           Column('Y27', Float),
           Column('Y28', Float),
           Column('Y29', Float),
           Column('Y30', Float),
           Column('Y31', Float),
           Column('Y32', Float),
           Column('Y33', Float),
           Column('Y34', Float),
           Column('Y35', Float),
           Column('Y36', Float),
           Column('Y37', Float),
           Column('Y38', Float),
           Column('Y39', Float),
           Column('Y40', Float),
           Column('Y41', Float), 
           Column('Y42', Float),
           Column('Y43', Float),
           Column('Y44', Float),
           Column('Y45', Float),
           Column('Y46', Float),
           Column('Y47', Float),
           Column('Y48', Float),
           Column('Y49', Float),
           Column('Y50', Float),
        )


    #declaring lists to hold each column of the train dataset
    trainset_X = []; trainset_Y1 = []; trainset_Y2 = []; trainset_Y3 = []; trainset_Y4 = [];

    #declaring lists to hold each column of the ideal dataset
    idealY1 = []; idealY2 = []; idealY3 = []; idealY4 = [];  idealY5 = [];  idealY6 = [];  idealY7 = [];  idealY8 = [];  idealY9 = [];  idealY10 = []
    idealY11 = []; idealY12 = []; idealY13 = []; idealY14 = [];  idealY15 = [];  idealY16 = [];  idealY17 = [];  idealY18 = [];  idealY19 = [];  idealY20 = []
    idealY21 = []; idealY22 = []; idealY23 = []; idealY24 = [];  idealY25 = [];  idealY26 = [];  idealY27 = [];  idealY28 = [];  idealY29 = [];  idealY30 = []
    idealY31 = []; idealY32 = []; idealY33 = []; idealY34 = [];  idealY35 = [];  idealY36 = [];  idealY37 = [];  idealY38 = [];  idealY39 = [];  idealY40 = []
    idealY41 = []; idealY42 = []; idealY43 = []; idealY44 = [];  idealY45 = [];  idealY46 = [];  idealY47 = [];  idealY48 = [];  idealY49 = [];  idealY50 = []
    idealX = []

    #declaaring list to hold each column of the test dataset
    testX = []; testY = []

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

            mytables.trainingset_table()
            mytables.idealfunction_table()

            #skipping the first splitFile in the file
            next(myFiles)
            #variable to count the number of records inserted into the tables in the database 
            no_records = 0
            no_records_ideal = 0
            #using for loop to read the records in the all the csv files
            for data in myFiles:
                #splitting files into individual index in memory
                splitFile = data.split(',')
                #verifying if the first file is train data
                if (file == 'train.csv'):
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
                    # if(mytables.table_exist("train_table")):
                        # continue
                    # else:
                        # mytables.trainingset_table()

                    # mytables.inserData(splitFile[0],splitFile[1],splitFile[2],splitFile[3],splitFile[4])
                    insert_train = traintable.insert().values(X = splitFile[0], Y1 = splitFile[1], Y2 = splitFile[2], Y3 = splitFile[3], Y4 = splitFile[4])
                    conn = mytables.engine.connect()
                    result = conn.execute(insert_train)
                    no_records += 1
                    print("Inserting train record no. {}".format(no_records))
                    # print(trainset_X)
                
                elif (file == 'ideal.csv'):
                    # loading the columns of ideal data into different list
                    idealX.append(splitFile[0])
                    idealY1.append(splitFile[1])
                    idealY2.append(splitFile[2])
                    idealY3.append(splitFile[3])
                    idealY4.append(splitFile[4])
                    idealY5.append(splitFile[5])
                    idealY6.append(splitFile[6])
                    idealY7.append(splitFile[7])
                    idealY8.append(splitFile[8])
                    idealY9.append(splitFile[9])
                    idealY10.append(splitFile[10])
                    idealY11.append(splitFile[11])
                    idealY12.append(splitFile[12])
                    idealY13.append(splitFile[13])
                    idealY14.append(splitFile[14])
                    idealY15.append(splitFile[15])
                    idealY16.append(splitFile[16])
                    idealY17.append(splitFile[17])
                    idealY18.append(splitFile[18])
                    idealY19.append(splitFile[19])
                    idealY20.append(splitFile[20])
                    idealY21.append(splitFile[21])
                    idealY22.append(splitFile[22])
                    idealY23.append(splitFile[23])
                    idealY24.append(splitFile[24])
                    idealY25.append(splitFile[25])
                    idealY26.append(splitFile[26])
                    idealY27.append(splitFile[27])
                    idealY28.append(splitFile[28])
                    idealY29.append(splitFile[29])
                    idealY30.append(splitFile[30])
                    idealY31.append(splitFile[31])
                    idealY32.append(splitFile[32])
                    idealY33.append(splitFile[33])
                    idealY34.append(splitFile[43])
                    idealY35.append(splitFile[35])
                    idealY36.append(splitFile[36])
                    idealY37.append(splitFile[37])
                    idealY38.append(splitFile[38])
                    idealY39.append(splitFile[39])
                    idealY40.append(splitFile[40])
                    idealY41.append(splitFile[41])
                    idealY42.append(splitFile[42])
                    idealY43.append(splitFile[43])
                    idealY44.append(splitFile[44])
                    idealY45.append(splitFile[45])
                    idealY46.append(splitFile[46])
                    idealY47.append(splitFile[47])
                    idealY48.append(splitFile[48])
                    idealY49.append(splitFile[49])
                    idealY50.append(splitFile[50])

                    #inserting records from the ideal csv file into the database
                    insert_ideal = ideal_table.insert().values(X = splitFile[0], Y1 = splitFile[1], Y2 = splitFile[2], Y3 = splitFile[3], Y4 = splitFile[4], Y5 = splitFile[5], Y6 = splitFile[6], Y7 = splitFile[7], Y8 = splitFile[8], Y9 = splitFile[9], Y10 = splitFile[10],
                        Y11 = splitFile[11], Y12 = splitFile[12], Y13 = splitFile[13], Y14 = splitFile[14], Y15 = splitFile[15], Y16 = splitFile[16], Y17 = splitFile[17], Y18 = splitFile[18], Y19 = splitFile[19], Y20 = splitFile[20],
                        Y21 = splitFile[21], Y22 = splitFile[22], Y23 = splitFile[23], Y24 = splitFile[24], Y25 = splitFile[25], Y26 = splitFile[26], Y27 = splitFile[27], Y28 = splitFile[28], Y29 = splitFile[29], Y30 = splitFile[30], 
                        Y31 = splitFile[31], Y32 = splitFile[32], Y33 = splitFile[33], Y34 = splitFile[34], Y35 = splitFile[35], Y36 = splitFile[36], Y37 = splitFile[37], Y38 = splitFile[38], Y39 = splitFile[39], Y40 = splitFile[40], 
                        Y41 = splitFile[41], Y42 = splitFile[42], Y43 = splitFile[43], Y44 = splitFile[44], Y45 = splitFile[45], Y46 = splitFile[46], Y47 = splitFile[47], Y48 = splitFile[48], Y49 = splitFile[49], Y50 = splitFile[50]
  
                     )
                    conn = mytables.engine.connect()
                    result = conn.execute(insert_ideal)
                    no_records_ideal += 1
                    print("Inserting ideal record no. {}".format(no_records_ideal))

                elif (file == 'test.csv'):
                    testX.append(splitFile[0])
                    testY.append(splitFile[1])

                





if __name__ == '__main__':
    main() 















