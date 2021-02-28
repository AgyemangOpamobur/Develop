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

class calculation(object):
    # def __init__(self,data1, data2):
    #     self.data1 = data1
    #     self.data2 = data2
    
    def deviation(self,data1,data2):
        try:
            devRes = np.subtract(pd.to_numeric(data1),pd.to_numeric(data2)) 
            squared = [devRes ** 2 for devRes in devRes]
            return squared
        except:
            print("Invalide data supply to the deviation method")

    def sumDeviation(self, data):
        try:
            sum_deviation = np.sum(data)
            return sum_deviation 
        except:
            print("Invalid data supply to the sum function")



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

            # mytables.trainingset_table()
            # mytables.idealfunction_table()
            #------------------------------------------
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
                    #-----------------------------------------------------
                    # insert_train = traintable.insert().values(X = splitFile[0], Y1 = splitFile[1], Y2 = splitFile[2], Y3 = splitFile[3], Y4 = splitFile[4])
                    # conn = mytables.engine.connect()
                    # result = conn.execute(insert_train)
                    # no_records += 1
                    # print("Inserting train record no. {}".format(no_records))
                   #-----------------------------------------------------------------------
                   
                
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
                    # insert_ideal = ideal_table.insert().values(X = splitFile[0], Y1 = splitFile[1], Y2 = splitFile[2], Y3 = splitFile[3], Y4 = splitFile[4], Y5 = splitFile[5], Y6 = splitFile[6], Y7 = splitFile[7], Y8 = splitFile[8], Y9 = splitFile[9], Y10 = splitFile[10],
                    #     Y11 = splitFile[11], Y12 = splitFile[12], Y13 = splitFile[13], Y14 = splitFile[14], Y15 = splitFile[15], Y16 = splitFile[16], Y17 = splitFile[17], Y18 = splitFile[18], Y19 = splitFile[19], Y20 = splitFile[20],
                    #     Y21 = splitFile[21], Y22 = splitFile[22], Y23 = splitFile[23], Y24 = splitFile[24], Y25 = splitFile[25], Y26 = splitFile[26], Y27 = splitFile[27], Y28 = splitFile[28], Y29 = splitFile[29], Y30 = splitFile[30], 
                    #     Y31 = splitFile[31], Y32 = splitFile[32], Y33 = splitFile[33], Y34 = splitFile[34], Y35 = splitFile[35], Y36 = splitFile[36], Y37 = splitFile[37], Y38 = splitFile[38], Y39 = splitFile[39], Y40 = splitFile[40], 
                    #     Y41 = splitFile[41], Y42 = splitFile[42], Y43 = splitFile[43], Y44 = splitFile[44], Y45 = splitFile[45], Y46 = splitFile[46], Y47 = splitFile[47], Y48 = splitFile[48], Y49 = splitFile[49], Y50 = splitFile[50]
  
                    #  )
                    # conn = mytables.engine.connect()
                    # result = conn.execute(insert_ideal)
                    # no_records_ideal += 1
                    # print("Inserting ideal record no. {}".format(no_records_ideal))
                    #-------------------------------------------------------------------------

                elif (file == 'test.csv'):
                    testX.append(splitFile[0])
                    testY.append(splitFile[1])
    
    print("\n Calculation the Deviation of training data with the ideal function from Y1 to Y50  \n")
   
    """
    calculating the deviation of Y1 of train set
    get the length of Y1 data from train set and use it as the upper limit for loop
    and increase it by 1 to cover all values in the list 
    
    declaring multiple list to store deviation of Y1 up to 50 of train data Y1
    formula (idealY1 - trainY1)^2
    """
    # count = len(trainset_Y1) + 1

    # subtracting and squaring the trainset_Y1 from ideal function Y1 to Y50 
    # find the sum of the deviation     
    square = calculation() #instance of calculation class
    #storing the results in a list
    devY1res1 = square.deviation(idealY1,trainset_Y1)
    sumY1res1 = square.sumDeviation(devY1res1) 
    devY1res2 = square.deviation(idealY2,trainset_Y1)
    sumY1res2 = square.sumDeviation(devY1res2) 
    devY1res3 = square.deviation(idealY3,trainset_Y1)
    sumY1res3 = square.sumDeviation(devY1res3) 
    devY1res4 = square.deviation(idealY4,trainset_Y1)
    sumY1res4 = square.sumDeviation(devY1res4) 
    devY1res5 = square.deviation(idealY5,trainset_Y1)
    sumY1res5 = square.sumDeviation(devY1res5) 
    devY1res6 = square.deviation(idealY6,trainset_Y1)
    sumY1res6 = square.sumDeviation(devY1res6) 
    devY1res7 = square.deviation(idealY7,trainset_Y1)
    sumY1res7 = square.sumDeviation(devY1res7) 
    devY1res8 = square.deviation(idealY8,trainset_Y1)
    sumY1res8 = square.sumDeviation(devY1res8) 
    devY1res9 = square.deviation(idealY9,trainset_Y1)
    sumY1res9 = square.sumDeviation(devY1res9) 
    devY1res10 = square.deviation(idealY10,trainset_Y1)
    sumY1res10 = square.sumDeviation(devY1res10) 
#----------------------------------------------------------------------
    devY1res11 = square.deviation(idealY11,trainset_Y1)
    sumY1res11 = square.sumDeviation(devY1res11) 
    devY1res12 = square.deviation(idealY12,trainset_Y1)
    sumY1res12 = square.sumDeviation(devY1res12) 
    devY1res13 = square.deviation(idealY13,trainset_Y1)
    sumY1res13 = square.sumDeviation(devY1res13) 
    devY1res14 = square.deviation(idealY14,trainset_Y1)
    sumY1res14 = square.sumDeviation(devY1res14) 
    devY1res15 = square.deviation(idealY15,trainset_Y1) 
    sumY1res15 = square.sumDeviation(devY1res15) 
    devY1res16 = square.deviation(idealY16,trainset_Y1)
    sumY1res16 = square.sumDeviation(devY1res16) 
    devY1res17 = square.deviation(idealY17,trainset_Y1)
    sumY1res17 = square.sumDeviation(devY1res17) 
    devY1res18 = square.deviation(idealY18,trainset_Y1)
    sumY1res18 = square.sumDeviation(devY1res18) 
    devY1res19 = square.deviation(idealY19,trainset_Y1)
    sumY1res19 = square.sumDeviation(devY1res19) 
    devY1res20 = square.deviation(idealY20,trainset_Y1)
    sumY1res20 = square.sumDeviation(devY1res20) 
#-----------------------------------------------------------------------
    devY1res21 = square.deviation(idealY21,trainset_Y1)
    sumY1res21 = square.sumDeviation(devY1res21) 
    devY1res22 = square.deviation(idealY22,trainset_Y1)
    sumY1res22 = square.sumDeviation(devY1res22) 
    devY1res23 = square.deviation(idealY23,trainset_Y1)
    sumY1res23 = square.sumDeviation(devY1res23) 
    devY1res24 = square.deviation(idealY24,trainset_Y1)
    sumY1res24 = square.sumDeviation(devY1res24) 
    devY1res25 = square.deviation(idealY25,trainset_Y1)
    sumY1res25 = square.sumDeviation(devY1res25) 
    devY1res26 = square.deviation(idealY26,trainset_Y1)
    sumY1res26 = square.sumDeviation(devY1res26) 
    devY1res27 = square.deviation(idealY27,trainset_Y1)
    sumY1res27 = square.sumDeviation(devY1res27) 
    devY1res28 = square.deviation(idealY28,trainset_Y1)
    sumY1res28 = square.sumDeviation(devY1res28) 
    devY1res29 = square.deviation(idealY29,trainset_Y1)
    sumY1res29 = square.sumDeviation(devY1res29) 
    devY1res30 = square.deviation(idealY30,trainset_Y1)
    sumY1res30 = square.sumDeviation(devY1res30) 
#-------------------------------------------------------------------------
    devY1res31 = square.deviation(idealY31,trainset_Y1)
    sumY1res31 = square.sumDeviation(devY1res31) 
    devY1res32 = square.deviation(idealY32,trainset_Y1)
    sumY1res32 = square.sumDeviation(devY1res32) 
    devY1res33 = square.deviation(idealY33,trainset_Y1)
    sumY1res33 = square.sumDeviation(devY1res33) 
    devY1res34 = square.deviation(idealY34,trainset_Y1)
    sumY1res34 = square.sumDeviation(devY1res34) 
    devY1res35 = square.deviation(idealY35,trainset_Y1)
    sumY1res35 = square.sumDeviation(devY1res35) 
    devY1res36 = square.deviation(idealY36,trainset_Y1)
    sumY1res36 = square.sumDeviation(devY1res36) 
    devY1res37 = square.deviation(idealY37,trainset_Y1)
    sumY1res37 = square.sumDeviation(devY1res37) 
    devY1res38 = square.deviation(idealY38,trainset_Y1)
    sumY1res38 = square.sumDeviation(devY1res38) 
    devY1res39 = square.deviation(idealY39,trainset_Y1)
    sumY1res39 = square.sumDeviation(devY1res39) 
    devY1res40 = square.deviation(idealY40,trainset_Y1)
    sumY1res40 = square.sumDeviation(devY1res40) 
#----------------------------------------------------------------------
    devY1res41 = square.deviation(idealY41,trainset_Y1)
    sumY1res41 = square.sumDeviation(devY1res41) 
    devY1res42 = square.deviation(idealY42,trainset_Y1)
    sumY1res42 = square.sumDeviation(devY1res42) 
    devY1res43 = square.deviation(idealY43,trainset_Y1)
    sumY1res43 = square.sumDeviation(devY1res43) 
    devY1res44 = square.deviation(idealY44,trainset_Y1)
    sumY1res44 = square.sumDeviation(devY1res44) 
    devY1res45 = square.deviation(idealY45,trainset_Y1)
    sumY1res45 = square.sumDeviation(devY1res45) 
    devY1res46 = square.deviation(idealY46,trainset_Y1)
    sumY1res46 = square.sumDeviation(devY1res46) 
    devY1res47 = square.deviation(idealY47,trainset_Y1)
    sumY1res47 = square.sumDeviation(devY1res47) 
    devY1res48 = square.deviation(idealY48,trainset_Y1)
    sumY1res48 = square.sumDeviation(devY1res48) 
    devY1res49 = square.deviation(idealY49,trainset_Y1)
    sumY1res49 = square.sumDeviation(devY1res49) 
    devY1res50 = square.deviation(idealY50,trainset_Y1)
    sumY1res50 = square.sumDeviation(devY1res50) 
    #################################################################################
    #################################################################################
    # subtracting and squaring the trainset_Y2 from ideal function Y1 to Y50 
    # find the sum of the deviation   
    devY2res1 = square.deviation(idealY1,trainset_Y2)
    sumY2res1 = square.sumDeviation(devY2res1) 
    devY2res2 = square.deviation(idealY2,trainset_Y2)
    sumY2res2 = square.sumDeviation(devY2res2) 
    devY2res3 = square.deviation(idealY3,trainset_Y2)
    sumY2res3 = square.sumDeviation(devY2res3) 
    devY2res4 = square.deviation(idealY4,trainset_Y2)
    sumY2res4 = square.sumDeviation(devY2res4) 
    devY2res5 = square.deviation(idealY5,trainset_Y2)
    sumY2res5 = square.sumDeviation(devY2res5) 
    devY2res6 = square.deviation(idealY6,trainset_Y2)
    sumY2res6 = square.sumDeviation(devY2res6) 
    devY2res7 = square.deviation(idealY7,trainset_Y2)
    sumY2res7 = square.sumDeviation(devY2res7) 
    devY2res8 = square.deviation(idealY8,trainset_Y2)
    sumY2res8 = square.sumDeviation(devY2res8) 
    devY2res9 = square.deviation(idealY9,trainset_Y2)
    sumY2res9 = square.sumDeviation(devY2res9) 
    devY2res10 = square.deviation(idealY10,trainset_Y2)
    sumY2res10 = square.sumDeviation(devY2res10) 
#----------------------------------------------------------------------
    devY2res11 = square.deviation(idealY11,trainset_Y2)
    sumY2res11 = square.sumDeviation(devY2res11) 
    devY2res12 = square.deviation(idealY12,trainset_Y2)
    sumY2res12 = square.sumDeviation(devY2res12) 
    devY2res13 = square.deviation(idealY13,trainset_Y2)
    sumY2res13 = square.sumDeviation(devY2res13) 
    devY2res14 = square.deviation(idealY14,trainset_Y2)
    sumY2res14 = square.sumDeviation(devY2res14) 
    devY2res15 = square.deviation(idealY15,trainset_Y2) 
    sumY2res15 = square.sumDeviation(devY2res15) 
    devY2res16 = square.deviation(idealY16,trainset_Y2)
    sumY2res16 = square.sumDeviation(devY2res16) 
    devY2res17 = square.deviation(idealY17,trainset_Y2)
    sumY2res17 = square.sumDeviation(devY2res17) 
    devY2res18 = square.deviation(idealY18,trainset_Y2)
    sumY2res18 = square.sumDeviation(devY2res18) 
    devY2res19 = square.deviation(idealY19,trainset_Y2)
    sumY2res19 = square.sumDeviation(devY2res19) 
    devY2res20 = square.deviation(idealY20,trainset_Y2)
    sumY2res20 = square.sumDeviation(devY2res20) 
#-----------------------------------------------------------------------
    devY2res21 = square.deviation(idealY21,trainset_Y2)
    sumY2res21 = square.sumDeviation(devY2res21) 
    devY2res22 = square.deviation(idealY22,trainset_Y2)
    sumY2res22 = square.sumDeviation(devY2res22) 
    devY2res23 = square.deviation(idealY23,trainset_Y2)
    sumY2res23 = square.sumDeviation(devY2res23) 
    devY2res24 = square.deviation(idealY24,trainset_Y2)
    sumY2res24 = square.sumDeviation(devY2res24) 
    devY2res25 = square.deviation(idealY25,trainset_Y2)
    sumY2res25 = square.sumDeviation(devY2res25) 
    devY2res26 = square.deviation(idealY26,trainset_Y2)
    sumY2res26 = square.sumDeviation(devY2res26) 
    devY2res27 = square.deviation(idealY27,trainset_Y2)
    sumY2res27 = square.sumDeviation(devY2res27) 
    devY2res28 = square.deviation(idealY28,trainset_Y2)
    sumY2res28 = square.sumDeviation(devY2res28) 
    devY2res29 = square.deviation(idealY29,trainset_Y2)
    sumY2res29 = square.sumDeviation(devY2res29) 
    devY2res30 = square.deviation(idealY30,trainset_Y2)
    sumY2res30 = square.sumDeviation(devY2res30) 
#-------------------------------------------------------------------------
    devY2res31 = square.deviation(idealY31,trainset_Y2)
    sumY2res31 = square.sumDeviation(devY2res31) 
    devY2res32 = square.deviation(idealY32,trainset_Y2)
    sumY2res32 = square.sumDeviation(devY2res32) 
    devY2res33 = square.deviation(idealY33,trainset_Y2)
    sumY2res33 = square.sumDeviation(devY2res33) 
    devY2res34 = square.deviation(idealY34,trainset_Y2)
    sumY2res34 = square.sumDeviation(devY2res34) 
    devY2res35 = square.deviation(idealY35,trainset_Y2)
    sumY2res35 = square.sumDeviation(devY2res35) 
    devY2res36 = square.deviation(idealY36,trainset_Y2)
    sumY2res36 = square.sumDeviation(devY2res36) 
    devY2res37 = square.deviation(idealY37,trainset_Y2)
    sumY2res37 = square.sumDeviation(devY2res37) 
    devY2res38 = square.deviation(idealY38,trainset_Y2)
    sumY2res38 = square.sumDeviation(devY2res38) 
    devY2res39 = square.deviation(idealY39,trainset_Y2)
    sumY2res39 = square.sumDeviation(devY2res39) 
    devY2res40 = square.deviation(idealY40,trainset_Y2)
    sumY2res40 = square.sumDeviation(devY2res40) 
#----------------------------------------------------------------------
    devY2res41 = square.deviation(idealY41,trainset_Y2)
    sumY2res41 = square.sumDeviation(devY2res41) 
    devY2res42 = square.deviation(idealY42,trainset_Y2)
    sumY2res42 = square.sumDeviation(devY2res42) 
    devY2res43 = square.deviation(idealY43,trainset_Y2)
    sumY2res43 = square.sumDeviation(devY2res43) 
    devY2res44 = square.deviation(idealY44,trainset_Y2)
    sumY2res44 = square.sumDeviation(devY2res44) 
    devY2res45 = square.deviation(idealY45,trainset_Y2)
    sumY2res45 = square.sumDeviation(devY2res45) 
    devY2res46 = square.deviation(idealY46,trainset_Y2)
    sumY2res46 = square.sumDeviation(devY2res46) 
    devY2res47 = square.deviation(idealY47,trainset_Y2)
    sumY2res47 = square.sumDeviation(devY2res47) 
    devY2res48 = square.deviation(idealY48,trainset_Y2)
    sumY2res48 = square.sumDeviation(devY2res48) 
    devY2res49 = square.deviation(idealY49,trainset_Y2)
    sumY2res49 = square.sumDeviation(devY2res49) 
    devY2res50 = square.deviation(idealY50,trainset_Y2)
    sumY2res50 = square.sumDeviation(devY2res50) 

    #################################################################################
    # subtracting and squaring the trainset_Y3 from ideal function Y1 to Y50 
    # find the sum of the deviation   
    devY3res1 = square.deviation(idealY1,trainset_Y3)
    sumY3res1 = square.sumDeviation(devY3res1) 
    devY3res2 = square.deviation(idealY2,trainset_Y3)
    sumY3res2 = square.sumDeviation(devY3res2) 
    devY3res3 = square.deviation(idealY3,trainset_Y3)
    sumY3res3 = square.sumDeviation(devY3res3) 
    devY3res4 = square.deviation(idealY4,trainset_Y3)
    sumY3res4 = square.sumDeviation(devY3res4) 
    devY3res5 = square.deviation(idealY5,trainset_Y3)
    sumY3res5 = square.sumDeviation(devY3res5) 
    devY3res6 = square.deviation(idealY6,trainset_Y3)
    sumY3res6 = square.sumDeviation(devY3res6) 
    devY3res7 = square.deviation(idealY7,trainset_Y3)
    sumY3res7 = square.sumDeviation(devY3res7) 
    devY3res8 = square.deviation(idealY8,trainset_Y3)
    sumY3res8 = square.sumDeviation(devY3res8) 
    devY3res9 = square.deviation(idealY9,trainset_Y3)
    sumY3res9 = square.sumDeviation(devY3res9) 
    devY3res10 = square.deviation(idealY10,trainset_Y3)
    sumY3res10 = square.sumDeviation(devY3res10) 
#----------------------------------------------------------------------
    devY3res11 = square.deviation(idealY11,trainset_Y3)
    sumY3res11 = square.sumDeviation(devY3res11) 
    devY3res12 = square.deviation(idealY12,trainset_Y3)
    sumY3res12 = square.sumDeviation(devY3res12) 
    devY3res13 = square.deviation(idealY13,trainset_Y3)
    sumY3res13 = square.sumDeviation(devY3res13) 
    devY3res14 = square.deviation(idealY14,trainset_Y3)
    sumY3res14 = square.sumDeviation(devY3res14) 
    devY3res15 = square.deviation(idealY15,trainset_Y3) 
    sumY3res15 = square.sumDeviation(devY3res15) 
    devY3res16 = square.deviation(idealY16,trainset_Y3)
    sumY3res16 = square.sumDeviation(devY3res16) 
    devY3res17 = square.deviation(idealY17,trainset_Y3)
    sumY3res17 = square.sumDeviation(devY3res17) 
    devY3res18 = square.deviation(idealY18,trainset_Y3)
    sumY3res18 = square.sumDeviation(devY3res18) 
    devY3res19 = square.deviation(idealY19,trainset_Y3)
    sumY3res19 = square.sumDeviation(devY3res19) 
    devY3res20 = square.deviation(idealY20,trainset_Y3)
    sumY3res20 = square.sumDeviation(devY3res20) 
#-----------------------------------------------------------------------
    devY3res21 = square.deviation(idealY21,trainset_Y3)
    sumY3res21 = square.sumDeviation(devY3res21) 
    devY3res22 = square.deviation(idealY22,trainset_Y3)
    sumY3res22 = square.sumDeviation(devY3res22) 
    devY3res23 = square.deviation(idealY23,trainset_Y3)
    sumY3res23 = square.sumDeviation(devY3res23) 
    devY3res24 = square.deviation(idealY24,trainset_Y3)
    sumY3res24 = square.sumDeviation(devY3res24) 
    devY3res25 = square.deviation(idealY25,trainset_Y3)
    sumY3res25 = square.sumDeviation(devY3res25) 
    devY3res26 = square.deviation(idealY26,trainset_Y3)
    sumY3res26 = square.sumDeviation(devY3res26) 
    devY3res27 = square.deviation(idealY27,trainset_Y3)
    sumY3res27 = square.sumDeviation(devY3res27) 
    devY3res28 = square.deviation(idealY28,trainset_Y3)
    sumY3res28 = square.sumDeviation(devY3res28) 
    devY3res29 = square.deviation(idealY29,trainset_Y3)
    sumY3res29 = square.sumDeviation(devY3res29) 
    devY3res30 = square.deviation(idealY30,trainset_Y3)
    sumY3res30 = square.sumDeviation(devY3res30) 
#-------------------------------------------------------------------------
    devY3res31 = square.deviation(idealY31,trainset_Y3)
    sumY3res31 = square.sumDeviation(devY3res31) 
    devY3res32 = square.deviation(idealY32,trainset_Y3)
    sumY3res32 = square.sumDeviation(devY3res32) 
    devY3res33 = square.deviation(idealY33,trainset_Y3)
    sumY3res33 = square.sumDeviation(devY3res33) 
    devY3res34 = square.deviation(idealY34,trainset_Y3)
    sumY3res34 = square.sumDeviation(devY3res34) 
    devY3res35 = square.deviation(idealY35,trainset_Y3)
    sumY3res35 = square.sumDeviation(devY3res35) 
    devY3res36 = square.deviation(idealY36,trainset_Y3)
    sumY3res36 = square.sumDeviation(devY3res36) 
    devY3res37 = square.deviation(idealY37,trainset_Y3)
    sumY3res37 = square.sumDeviation(devY3res37) 
    devY3res38 = square.deviation(idealY38,trainset_Y3)
    sumY3res38 = square.sumDeviation(devY3res38) 
    devY3res39 = square.deviation(idealY39,trainset_Y3)
    sumY3res39 = square.sumDeviation(devY3res39) 
    devY3res40 = square.deviation(idealY40,trainset_Y3)
    sumY3res40 = square.sumDeviation(devY3res40) 
#----------------------------------------------------------------------
    devY3res41 = square.deviation(idealY41,trainset_Y3)
    sumY3res41 = square.sumDeviation(devY3res41) 
    devY3res42 = square.deviation(idealY42,trainset_Y3)
    sumY3res42 = square.sumDeviation(devY3res42) 
    devY3res43 = square.deviation(idealY43,trainset_Y3)
    sumY3res43 = square.sumDeviation(devY3res43) 
    devY3res44 = square.deviation(idealY44,trainset_Y3)
    sumY3res44 = square.sumDeviation(devY3res44) 
    devY3res45 = square.deviation(idealY45,trainset_Y3)
    sumY3res45 = square.sumDeviation(devY3res45) 
    devY3res46 = square.deviation(idealY46,trainset_Y3)
    sumY3res46 = square.sumDeviation(devY3res46) 
    devY3res47 = square.deviation(idealY47,trainset_Y3)
    sumY3res47 = square.sumDeviation(devY3res47) 
    devY3res48 = square.deviation(idealY48,trainset_Y3)
    sumY3res48 = square.sumDeviation(devY3res48) 
    devY3res49 = square.deviation(idealY49,trainset_Y3)
    sumY3res49 = square.sumDeviation(devY3res49) 
    devY3res50 = square.deviation(idealY50,trainset_Y3)
    sumY3res50 = square.sumDeviation(devY3res50) 



    print(devY3res50)
    print("\n")
    print(sumY3res50)
    # print("\n")
    # print(trainset_Y1)
    

                





if __name__ == '__main__':
    main() 















