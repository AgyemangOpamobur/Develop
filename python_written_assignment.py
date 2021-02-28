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

"""
Creating a class that holds methods all calculation
in the program
"""
class calculation(object):
    # method to calculate the deviation of the dataset
    def deviation(self,data1,data2):
        try:
            devRes = np.subtract(pd.to_numeric(data1),pd.to_numeric(data2)) 
            squared = [devRes ** 2 for devRes in devRes]
            return squared
        except:
            print("Invalide data supply to the deviation method")
    #method to calculate the sum of deviation  
    def sumDeviation(self, data):
        try:
            sum_deviation = np.sum(data)
            return sum_deviation 
        except:
            print("Invalid data supply to the sum function")
    
    #method to find the minimum value of list supply to it
    def minimumValue(self, data):
        try:
            min_value = min(data, key= data.get)
            return min_value
        except:
            print("Invalid input data")




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
    ###########################################################################################
     # subtracting and squaring the trainset_Y4 from ideal function Y1 to Y50 
    # find the sum of the deviation   
    devY4res1 = square.deviation(idealY1,trainset_Y4)
    sumY4res1 = square.sumDeviation(devY4res1) 
    devY4res2 = square.deviation(idealY2,trainset_Y4)
    sumY4res2 = square.sumDeviation(devY4res2) 
    devY4res3 = square.deviation(idealY3,trainset_Y4)
    sumY4res3 = square.sumDeviation(devY4res3) 
    devY4res4 = square.deviation(idealY4,trainset_Y4)
    sumY4res4 = square.sumDeviation(devY4res4) 
    devY4res5 = square.deviation(idealY5,trainset_Y4)
    sumY4res5 = square.sumDeviation(devY4res5) 
    devY4res6 = square.deviation(idealY6,trainset_Y4)
    sumY4res6 = square.sumDeviation(devY4res6) 
    devY4res7 = square.deviation(idealY7,trainset_Y4)
    sumY4res7 = square.sumDeviation(devY4res7) 
    devY4res8 = square.deviation(idealY8,trainset_Y4)
    sumY4res8 = square.sumDeviation(devY4res8) 
    devY4res9 = square.deviation(idealY9,trainset_Y4)
    sumY4res9 = square.sumDeviation(devY4res9) 
    devY4res10 = square.deviation(idealY10,trainset_Y4)
    sumY4res10 = square.sumDeviation(devY4res10) 
#----------------------------------------------------------------------
    devY4res11 = square.deviation(idealY11,trainset_Y4)
    sumY4res11 = square.sumDeviation(devY4res11) 
    devY4res12 = square.deviation(idealY12,trainset_Y4)
    sumY4res12 = square.sumDeviation(devY4res12) 
    devY4res13 = square.deviation(idealY13,trainset_Y4)
    sumY4res13 = square.sumDeviation(devY4res13) 
    devY4res14 = square.deviation(idealY14,trainset_Y4)
    sumY4res14 = square.sumDeviation(devY4res14) 
    devY4res15 = square.deviation(idealY15,trainset_Y4) 
    sumY4res15 = square.sumDeviation(devY4res15) 
    devY4res16 = square.deviation(idealY16,trainset_Y4)
    sumY4res16 = square.sumDeviation(devY4res16) 
    devY4res17 = square.deviation(idealY17,trainset_Y4)
    sumY4res17 = square.sumDeviation(devY4res17) 
    devY4res18 = square.deviation(idealY18,trainset_Y4)
    sumY4res18 = square.sumDeviation(devY4res18) 
    devY4res19 = square.deviation(idealY19,trainset_Y4)
    sumY4res19 = square.sumDeviation(devY4res19) 
    devY4res20 = square.deviation(idealY20,trainset_Y4)
    sumY4res20 = square.sumDeviation(devY4res20) 
#-----------------------------------------------------------------------
    devY4res21 = square.deviation(idealY21,trainset_Y4)
    sumY4res21 = square.sumDeviation(devY4res21) 
    devY4res22 = square.deviation(idealY22,trainset_Y4)
    sumY4res22 = square.sumDeviation(devY4res22) 
    devY4res23 = square.deviation(idealY23,trainset_Y4)
    sumY4res23 = square.sumDeviation(devY4res23) 
    devY4res24 = square.deviation(idealY24,trainset_Y4)
    sumY4res24 = square.sumDeviation(devY4res24) 
    devY4res25 = square.deviation(idealY25,trainset_Y4)
    sumY4res25 = square.sumDeviation(devY4res25) 
    devY4res26 = square.deviation(idealY26,trainset_Y4)
    sumY4res26 = square.sumDeviation(devY4res26) 
    devY4res27 = square.deviation(idealY27,trainset_Y4)
    sumY4res27 = square.sumDeviation(devY4res27) 
    devY4res28 = square.deviation(idealY28,trainset_Y4)
    sumY4res28 = square.sumDeviation(devY4res28) 
    devY4res29 = square.deviation(idealY29,trainset_Y4)
    sumY4res29 = square.sumDeviation(devY4res29) 
    devY4res30 = square.deviation(idealY30,trainset_Y4)
    sumY4res30 = square.sumDeviation(devY4res30) 
#-------------------------------------------------------------------------
    devY4res31 = square.deviation(idealY31,trainset_Y4)
    sumY4res31 = square.sumDeviation(devY4res31) 
    devY4res32 = square.deviation(idealY32,trainset_Y4)
    sumY4res32 = square.sumDeviation(devY4res32) 
    devY4res33 = square.deviation(idealY33,trainset_Y4)
    sumY4res33 = square.sumDeviation(devY4res33) 
    devY4res34 = square.deviation(idealY34,trainset_Y4)
    sumY4res34 = square.sumDeviation(devY4res34) 
    devY4res35 = square.deviation(idealY35,trainset_Y4)
    sumY4res35 = square.sumDeviation(devY4res35) 
    devY4res36 = square.deviation(idealY36,trainset_Y4)
    sumY4res36 = square.sumDeviation(devY4res36) 
    devY4res37 = square.deviation(idealY37,trainset_Y4)
    sumY4res37 = square.sumDeviation(devY4res37) 
    devY4res38 = square.deviation(idealY38,trainset_Y4)
    sumY4res38 = square.sumDeviation(devY4res38) 
    devY4res39 = square.deviation(idealY39,trainset_Y4)
    sumY4res39 = square.sumDeviation(devY4res39) 
    devY4res40 = square.deviation(idealY40,trainset_Y4)
    sumY4res40 = square.sumDeviation(devY4res40) 
#----------------------------------------------------------------------
    devY4res41 = square.deviation(idealY41,trainset_Y4)
    sumY4res41 = square.sumDeviation(devY4res41) 
    devY4res42 = square.deviation(idealY42,trainset_Y4)
    sumY4res42 = square.sumDeviation(devY4res42) 
    devY4res43 = square.deviation(idealY43,trainset_Y4)
    sumY4res43 = square.sumDeviation(devY4res43) 
    devY4res44 = square.deviation(idealY44,trainset_Y4)
    sumY4res44 = square.sumDeviation(devY4res44) 
    devY4res45 = square.deviation(idealY45,trainset_Y4)
    sumY4res45 = square.sumDeviation(devY4res45) 
    devY4res46 = square.deviation(idealY46,trainset_Y4)
    sumY4res46 = square.sumDeviation(devY4res46) 
    devY4res47 = square.deviation(idealY47,trainset_Y4)
    sumY4res47 = square.sumDeviation(devY4res47) 
    devY4res48 = square.deviation(idealY48,trainset_Y4)
    sumY4res48 = square.sumDeviation(devY4res48) 
    devY4res49 = square.deviation(idealY49,trainset_Y4)
    sumY4res49 = square.sumDeviation(devY4res49) 
    devY4res50 = square.deviation(idealY50,trainset_Y4)
    sumY4res50 = square.sumDeviation(devY4res50) 
#####################################################################################################
    """
    Displaying trainset Y1 to Y4 deviation square of 50 ideal function in a table 
    using Pandas Dataframe
    """
    print('Training set Y1 deviation square of 50 ideal function')
    dframe1 = pd.DataFrame({'Trainset_Y1': trainset_Y1,
    'd^2(Y1)': devY1res1,'d^2(Y2)': devY1res2,'d^2(Y3)': devY1res3,'d^2(Y4)': devY1res4,'d^2(Y5)': devY1res5,'d^2(Y6)': devY1res6,'d^2(Y7)': devY1res7,'d^2(Y8)': devY1res8,'d^2(Y9)': devY1res9,'d^2(Y10)': devY1res10, 
    'd^2(Y11)': devY1res11,'d^2(Y12)': devY1res12,'d^2(Y13)': devY1res13,'d^2(Y14)': devY1res14,'d^2(Y15)': devY1res15,'d^2(Y16)': devY1res16,'d^2(Y17)': devY1res17,'d^2(Y18)': devY1res18,'d^2(Y19)': devY1res19,'d^2(Y20)': devY1res20,
    'd^2(Y21)': devY1res21,'d^2(Y22)': devY1res22,'d^2(Y23)': devY1res23,'d^2(Y24)': devY1res24,'d^2(Y25)': devY1res25,'d^2(Y26)': devY1res26,'d^2(Y27)': devY1res27,'d^2(Y28)': devY1res28,'d^2(Y29)': devY1res29,'d^2(Y30)': devY1res30,
    'd^2(Y31)': devY1res31,'d^2(Y32)': devY1res32,'d^2(Y33)': devY1res33,'d^2(Y34)': devY1res34,'d^2(Y35)': devY1res35,'d^2(Y36)': devY1res36,'d^2(Y37)': devY1res37,'d^2(Y38)': devY1res38,'d^2(Y39)': devY1res39,'d^2(Y40)': devY1res40,
    'd^2(Y41)': devY1res41,'d^2(Y42)': devY1res42,'d^2(Y43)': devY1res43,'d^2(Y44)': devY1res44,'d^2(Y45)': devY1res45,'d^2(Y46)': devY1res46,'d^2(Y47)': devY1res47,'d^2(Y48)': devY1res48,'d^2(Y49)': devY1res49,'d^2(Y50)': devY1res50
    })
    # print(dframe1)
    print("\n")
    print('Training set Y2 deviation square of 50 ideal function')
    dframe2 = pd.DataFrame({'Trainset_Y2': trainset_Y2,
    'd^2(Y1)': devY2res1,'d^2(Y2)': devY2res2,'d^2(Y3)': devY2res3,'d^2(Y4)': devY2res4,'d^2(Y5)': devY2res5,'d^2(Y6)': devY2res6,'d^2(Y7)': devY2res7,'d^2(Y8)': devY2res8,'d^2(Y9)': devY2res9,'d^2(Y10)': devY2res10, 
    'd^2(Y11)': devY2res11,'d^2(Y12)': devY2res12,'d^2(Y13)': devY2res13,'d^2(Y14)': devY2res14,'d^2(Y15)': devY2res15,'d^2(Y16)': devY2res16,'d^2(Y17)': devY2res17,'d^2(Y18)': devY2res18,'d^2(Y19)': devY2res19,'d^2(Y20)': devY2res20,
    'd^2(Y21)': devY2res21,'d^2(Y22)': devY2res22,'d^2(Y23)': devY2res23,'d^2(Y24)': devY2res24,'d^2(Y25)': devY2res25,'d^2(Y26)': devY2res26,'d^2(Y27)': devY2res27,'d^2(Y28)': devY2res28,'d^2(Y29)': devY2res29,'d^2(Y30)': devY2res30,
    'd^2(Y31)': devY2res31,'d^2(Y32)': devY2res32,'d^2(Y33)': devY2res33,'d^2(Y34)': devY2res34,'d^2(Y35)': devY2res35,'d^2(Y36)': devY2res36,'d^2(Y37)': devY2res37,'d^2(Y38)': devY2res38,'d^2(Y39)': devY2res39,'d^2(Y40)': devY2res40,
    'd^2(Y41)': devY2res41,'d^2(Y42)': devY2res42,'d^2(Y43)': devY2res43,'d^2(Y44)': devY2res44,'d^2(Y45)': devY2res45,'d^2(Y46)': devY2res46,'d^2(Y47)': devY2res47,'d^2(Y48)': devY2res48,'d^2(Y49)': devY2res49,'d^2(Y50)': devY2res50
    })
    # print(dframe2)
    print("\n")
    print('Training set Y3 deviation square of 50 ideal function')
    dframe3 = pd.DataFrame({'Trainset_Y3': trainset_Y3,
    'd^2(Y1)': devY3res1,'d^2(Y2)': devY3res2,'d^2(Y3)': devY3res3,'d^2(Y4)': devY3res4,'d^2(Y5)': devY3res5,'d^2(Y6)': devY3res6,'d^2(Y7)': devY3res7,'d^2(Y8)': devY3res8,'d^2(Y9)': devY3res9,'d^2(Y10)': devY3res10, 
    'd^2(Y11)': devY3res11,'d^2(Y12)': devY3res12,'d^2(Y13)': devY3res13,'d^2(Y14)': devY3res14,'d^2(Y15)': devY3res15,'d^2(Y16)': devY3res16,'d^2(Y17)': devY3res17,'d^2(Y18)': devY3res18,'d^2(Y19)': devY3res19,'d^2(Y20)': devY3res20,
    'd^2(Y21)': devY3res21,'d^2(Y22)': devY3res22,'d^2(Y23)': devY3res23,'d^2(Y24)': devY3res24,'d^2(Y25)': devY3res25,'d^2(Y26)': devY3res26,'d^2(Y27)': devY3res27,'d^2(Y28)': devY3res28,'d^2(Y29)': devY3res29,'d^2(Y30)': devY3res30,
    'd^2(Y31)': devY3res31,'d^2(Y32)': devY3res32,'d^2(Y33)': devY3res33,'d^2(Y34)': devY3res34,'d^2(Y35)': devY3res35,'d^2(Y36)': devY3res36,'d^2(Y37)': devY3res37,'d^2(Y38)': devY3res38,'d^2(Y39)': devY3res39,'d^2(Y40)': devY3res40,
    'd^2(Y41)': devY3res41,'d^2(Y42)': devY3res42,'d^2(Y43)': devY3res43,'d^2(Y44)': devY3res44,'d^2(Y45)': devY3res45,'d^2(Y46)': devY3res46,'d^2(Y47)': devY3res47,'d^2(Y48)': devY3res48,'d^2(Y49)': devY3res49,'d^2(Y50)': devY3res50
    })
    # print(dframe3)
    print("\n")
    print('Training set Y4 deviation square of 50 ideal function')
    dframe4 = pd.DataFrame({'Trainset_Y3': trainset_Y4,
    'd^2(Y1)': devY4res1,'d^2(Y2)': devY4res2,'d^2(Y3)': devY4res3,'d^2(Y4)': devY4res4,'d^2(Y5)': devY4res5,'d^2(Y6)': devY4res6,'d^2(Y7)': devY4res7,'d^2(Y8)': devY4res8,'d^2(Y9)': devY4res9,'d^2(Y10)': devY4res10, 
    'd^2(Y11)': devY4res11,'d^2(Y12)': devY4res12,'d^2(Y13)': devY4res13,'d^2(Y14)': devY4res14,'d^2(Y15)': devY4res15,'d^2(Y16)': devY4res16,'d^2(Y17)': devY4res17,'d^2(Y18)': devY4res18,'d^2(Y19)': devY4res19,'d^2(Y20)': devY4res20,
    'd^2(Y21)': devY4res21,'d^2(Y22)': devY4res22,'d^2(Y23)': devY4res23,'d^2(Y24)': devY4res24,'d^2(Y25)': devY4res25,'d^2(Y26)': devY4res26,'d^2(Y27)': devY4res27,'d^2(Y28)': devY4res28,'d^2(Y29)': devY4res29,'d^2(Y30)': devY4res30,
    'd^2(Y31)': devY4res31,'d^2(Y32)': devY4res32,'d^2(Y33)': devY4res33,'d^2(Y34)': devY4res34,'d^2(Y35)': devY4res35,'d^2(Y36)': devY4res36,'d^2(Y37)': devY4res37,'d^2(Y38)': devY4res38,'d^2(Y39)': devY4res39,'d^2(Y40)': devY4res40,
    'd^2(Y41)': devY4res41,'d^2(Y42)': devY4res42,'d^2(Y43)': devY4res43,'d^2(Y44)': devY4res44,'d^2(Y45)': devY4res45,'d^2(Y46)': devY4res46,'d^2(Y47)': devY4res47,'d^2(Y48)': devY4res48,'d^2(Y49)': devY4res49,'d^2(Y50)': devY4res50
    })
    # print(dframe4)
 #########################################################################################################################################################
    """
    Putting the summation of all the training set into a dictionary
    idY1 - idY50 represent summation of deviation of ideal function Y1 to Y50

    """
    # Dictionary of train set Y1, Key = idY1 - idY50 and the value = sumY1res1 - sumY1res50
    trainsetY1Sum = {'idY1':sumY1res1,'idY2':sumY1res2,'idY3':sumY1res3,'idY4':sumY1res4,'idY5':sumY1res5,'idY6':sumY1res6,'idY7':sumY1res7,'idY8':sumY1res8,'idY9':sumY1res9,'idY10':sumY1res10,
    'idY11':sumY1res11,'idY12':sumY1res12,'idY13':sumY1res13,'idY14':sumY1res14,'idY15':sumY1res15,'idY16':sumY1res16,'idY17':sumY1res17,'idY18':sumY1res18,'idY19':sumY1res19,'idY20':sumY1res20,
    'idY21':sumY1res21,'idY22':sumY1res22,'idY23':sumY1res23,'idY24':sumY1res24,'idY25':sumY1res25,'idY26':sumY1res26,'idY27':sumY1res27,'idY28':sumY1res28,'idY29':sumY1res29,'idY30':sumY1res30,
    'idY31':sumY1res31,'idY32':sumY1res32,'idY33':sumY1res33,'idY34':sumY1res34,'idY35':sumY1res35,'idY36':sumY1res36,'idY37':sumY1res37,'idY38':sumY1res38,'idY39':sumY1res39,'idY40':sumY1res40,
    'idY41':sumY1res41,'idY42':sumY1res42,'idY43':sumY1res43,'idY44':sumY1res44,'idY45':sumY1res45,'idY46':sumY1res46,'idY47':sumY1res47,'idY48':sumY1res48,'idY49':sumY1res49,'idY50':sumY1res50 
    }   
    # Dictionary of train set Y2, Key = idY1 - idY50 and the value = sumY2res1 - sumY2res50
    trainsetY2Sum = {'idY1':sumY2res1,'idY2':sumY2res2,'idY3':sumY2res3,'idY4':sumY2res4,'idY5':sumY2res5,'idY6':sumY2res6,'idY7':sumY2res7,'idY8':sumY2res8,'idY9':sumY2res9,'idY10':sumY2res10,
    'idY11':sumY2res11,'idY12':sumY2res12,'idY13':sumY2res13,'idY14':sumY2res14,'idY15':sumY2res15,'idY16':sumY2res16,'idY17':sumY2res17,'idY18':sumY2res18,'idY19':sumY2res19,'idY20':sumY2res20,
    'idY21':sumY2res21,'idY22':sumY2res22,'idY23':sumY2res23,'idY24':sumY2res24,'idY25':sumY2res25,'idY26':sumY2res26,'idY27':sumY2res27,'idY28':sumY2res28,'idY29':sumY2res29,'idY30':sumY2res30,
    'idY31':sumY2res31,'idY32':sumY2res32,'idY33':sumY2res33,'idY34':sumY2res34,'idY35':sumY2res35,'idY36':sumY2res36,'idY37':sumY2res37,'idY38':sumY2res38,'idY39':sumY2res39,'idY40':sumY2res40,
    'idY41':sumY2res41,'idY42':sumY2res42,'idY43':sumY2res43,'idY44':sumY2res44,'idY45':sumY2res45,'idY46':sumY2res46,'idY47':sumY2res47,'idY48':sumY2res48,'idY49':sumY2res49,'idY50':sumY2res50 
    }   
    # Dictionary of train set Y3, Key = idY1 - idY50 and the value = sumY3res1 - sumY3res50
    trainsetY3Sum = {'idY1':sumY3res1,'idY2':sumY3res2,'idY3':sumY3res3,'idY4':sumY3res4,'idY5':sumY3res5,'idY6':sumY3res6,'idY7':sumY3res7,'idY8':sumY3res8,'idY9':sumY3res9,'idY10':sumY3res10,
    'idY11':sumY3res11,'idY12':sumY3res12,'idY13':sumY3res13,'idY14':sumY3res14,'idY15':sumY3res15,'idY16':sumY3res16,'idY17':sumY3res17,'idY18':sumY3res18,'idY19':sumY3res19,'idY20':sumY3res20,
    'idY21':sumY3res21,'idY22':sumY3res22,'idY23':sumY3res23,'idY24':sumY3res24,'idY25':sumY3res25,'idY26':sumY3res26,'idY27':sumY3res27,'idY28':sumY3res28,'idY29':sumY3res29,'idY30':sumY3res30,
    'idY31':sumY3res31,'idY32':sumY3res32,'idY33':sumY3res33,'idY34':sumY3res34,'idY35':sumY3res35,'idY36':sumY3res36,'idY37':sumY3res37,'idY38':sumY3res38,'idY39':sumY3res39,'idY40':sumY3res40,
    'idY41':sumY3res41,'idY42':sumY3res42,'idY43':sumY3res43,'idY44':sumY3res44,'idY45':sumY3res45,'idY46':sumY3res46,'idY47':sumY3res47,'idY48':sumY3res48,'idY49':sumY3res49,'idY50':sumY3res50 
    } 
    # Dictionary of train set Y4, Key = idY1 - idY50 and the value = sumY4res1 - sumY4res50
    trainsetY4Sum = {'idY1':sumY4res1,'idY2':sumY4res2,'idY3':sumY4res3,'idY4':sumY4res4,'idY5':sumY4res5,'idY6':sumY4res6,'idY7':sumY4res7,'idY8':sumY4res8,'idY9':sumY4res9,'idY10':sumY4res10,
    'idY11':sumY4res11,'idY12':sumY4res12,'idY13':sumY4res13,'idY14':sumY4res14,'idY15':sumY4res15,'idY16':sumY4res16,'idY17':sumY4res17,'idY18':sumY4res18,'idY19':sumY4res19,'idY20':sumY4res20,
    'idY21':sumY4res21,'idY22':sumY4res22,'idY23':sumY4res23,'idY24':sumY4res24,'idY25':sumY4res25,'idY26':sumY4res26,'idY27':sumY4res27,'idY28':sumY4res28,'idY29':sumY4res29,'idY30':sumY4res30,
    'idY31':sumY4res31,'idY32':sumY4res32,'idY33':sumY4res33,'idY34':sumY4res34,'idY35':sumY4res35,'idY36':sumY4res36,'idY37':sumY4res37,'idY38':sumY4res38,'idY39':sumY4res39,'idY40':sumY4res40,
    'idY41':sumY4res41,'idY42':sumY4res42,'idY43':sumY4res43,'idY44':sumY4res44,'idY45':sumY4res45,'idY46':sumY4res46,'idY47':sumY4res47,'idY48':sumY4res48,'idY49':sumY4res49,'idY50':sumY4res50 
    } 
########################################################################################################################################################################
    """
    Getting mininum values and their corresponding ideal function from the 
    trainset Y1 - Y4 

    """
    # fetching the identity of the minimum value from the sum of all y-deviation square of the trainset Y1 to Y4
    # first getting the minimum value's key from their dictionary
    min_trainset_Y1_key = square.minimumValue(trainsetY1Sum)
    min_trainset_Y2_key = square.minimumValue(trainsetY2Sum)
    min_trainset_Y3_key = square.minimumValue(trainsetY3Sum)
    min_trainset_Y4_key = square.minimumValue(trainsetY4Sum)

    # print("The minimum function for trainset Y1 is: " + min_trainset_Y1_key)
    # print("The minimum function for trainset Y2 is: " + min_trainset_Y2_key)
    # print("The minimum function for trainset Y3 is: " + min_trainset_Y3_key)
    # print("The minimum function for trainset Y4 is: " + min_trainset_Y4_key)

    #declaring variables and lists to hold the key and value from the dictionaries  
    global min_trainset_Y4_value, min_trainset_Y3_value, min_trainset_Y2_value, min_trainset_Y1_value
    trainsetY1Sum_value = []; trainsetY2Sum_value = []; trainsetY3Sum_value = []; trainsetY4Sum_value = []
    # getting corresponding value for train set Y1
    for key,value in trainsetY1Sum.items():
        trainsetY1Sum_value.append(value)
        if key == min_trainset_Y1_key:
            min_trainset_Y1_value = value
            # print("The corresponding value of "+min_trainset_Y1+" is : "+ str(value))

    for key,value in trainsetY2Sum.items():
        trainsetY2Sum_value.append(value)
        if key == min_trainset_Y2_key:
            min_trainset_Y2_value = value
            # print("The corresponding value of "+min_trainset_Y2+" is : "+ str(value))

    for key,value in trainsetY3Sum.items():
        trainsetY3Sum_value.append(value)
        if key == min_trainset_Y3_key:
            min_trainset_Y3_value = value
            # print("The corresponding value of "+min_trainset_Y3+" is : "+ str(value))

    for key,value in trainsetY4Sum.items():
        trainsetY4Sum_value.append(value)
        if key == min_trainset_Y4_key:
            min_trainset_Y4_value = value
            # print("The corresponding value of "+min_trainset_Y4+" is : "+ str(value))
   
    
    print("The minimum function for trainset Y1 is: " + min_trainset_Y1_key + " value: "+ str(min_trainset_Y1_value))
    print("The minimum function for trainset Y2 is: " + min_trainset_Y2_key + " value: "+ str(min_trainset_Y2_value))
    print("The minimum function for trainset Y3 is: " + min_trainset_Y3_key + " value: "+ str(min_trainset_Y3_value))
    print("The minimum function for trainset Y4 is: " + min_trainset_Y4_key + " value: "+ str(min_trainset_Y4_value))
    
    # min_trainset_Y1 = square.minimumValue(trainsetY1Sum)
    
    # print(trainsetY4Sum)
    # print("\n")
    # print(sumY4res50)
    # print("\n")
    # print(trainset_Y1)
    

                





if __name__ == '__main__':
    main() 















