"""
Python program to train a dataset and select four ideal function out of it.
And use the four ideal function to select best fit function out of a test set
"""
# importing needed libraries 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import text
from itertools import groupby
import bokeh
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show
from random import seed
import numpy as np
import pandas as pd
import math
import os
import glob
import csv
import math 
import unittest


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
    
    def test_data_table(self):
        print("Creating test_data table.................")
        try:
            test_data_table = Table(
                'test_data_table', self.meta, 
                Column('X_Test_Function', String, primary_key = True), 
                Column('Y_Test_Function', String), 
                Column('Delta_Y', String),
                Column('No_of_Ideal_Func', String),
                
            )
            self.meta.create_all(self.engine)
            print("Finish creating test data table")
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
        try:
            path = self.path
            extension = 'csv'
            os.chdir(path)
            data = glob.glob('*.{}'.format(extension))     
            return data
        except:
            print("File cannot be found. Check the path")

"""
Creating a class that holds methods to plot the 
graphs
"""
class plot_graph(object):

    #constructor of class plot_graph
    def __init__(self,path,output,x,y,c,label):
        self.path = path
        self.output = output
        self.x = x
        self.y = y
        self.label = label
        self.c = c

    # method plot graph
    def plotgraph(self):
        try:
            df = pd.read_csv(self.path)
            output_file(self.output)
            plot=figure(plot_width = 600, plot_height=600, x_axis_label="x axis", y_axis_label="y axis")
            plot.circle_dot(x = df[self.x], y = df[self.y],size=10,color=self.c,legend_label=self.label)
            show(plot)
        except:
            print("Invalid data. Check the arguments")

"""
Creating a class to test all useful elements 
"""
# class UnitTestLoadFile(unittest.TestCase):
#     def test_loadfile(self):
        
#         '''
#         test the method to load file from the directory
#         '''
#         ld = load_file(p)

        # math_operations = MathOperations()
        # result = math_operations.math_addition(2, 5)
        # self.assertEqual(result, 4, "The addition should be 4")
    
    




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
        
    #method to find the maximum value of list supply to it
    def maximumValue(self, data):
        try:
            max_value = max(data, key= data.get)
            return max_value
        except:
            print("Invalid input data")
    
    #method to calcualte factors of selected functions
    def factors(self,sValues):
        try:
            self.array = []
            square_root = list(np.sqrt(sValues))
            counter = int(len(sValues))
            RoundupFactor =  [round(x,1) for x in square_root] 
            Format_Roundup = [element * 1 for element in RoundupFactor]
            for n in range(0, counter):
                for i in square_root:
                    if(Format_Roundup[n] % 3 == 0):
                        self.array.append(i)
                        # if(i != square_root[n]):
                            # self.array.append(Format_Roundup[n] / i)
                        #     a=0
            # Grouping the factors 
            data = pd.Series(range(len(self.array))).groupby(self.array, sort=False).apply(list).tolist()
            return data

        except:
            print("Invalid input data")

    #method to select all the maximum factors of the selected list        
    def max_factor(self, data):
        try:
           max_data =  [max(p) for p in data]
           return max_data
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
    # Protoype of the structure of train table
    traintable =Table(
                  'train_table',meta, 
                 Column('X', Float, primary_key = True), 
                 Column('Y1', Float), 
                 Column('Y2', Float),
                 Column('Y3', Float),
                 Column('Y4', Float),
            )
    # Protoype of the structure of train table 
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
    # Protoype of the structure of train table
    test_data = Table(
                'test_data_table', meta, 
                Column('X_Test_Function', String, primary_key = True), 
                Column('Y_Test_Function', String), 
                Column('Delta_Y', String),
                Column('No_of_Ideal_Func', String)
                
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

    #declaring list to hold each column of the test dataset
    testX = []; testY = []

    # declaring a dictionary to hold test set X and Y values 
    testXYpair = {} 

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
                    insert_train = traintable.insert().values(X = splitFile[0], Y1 = splitFile[1], Y2 = splitFile[2], Y3 = splitFile[3], Y4 = splitFile[4])
                    conn = mytables.engine.connect()
                    result = conn.execute(insert_train)
                    no_records += 1
                    print("Inserting train record no. {}".format(no_records))
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
                    #-------------------------------------------------------------------------

                elif (file == 'test.csv'):
                    testX.append(splitFile[0])
                    testY.append(splitFile[1])
                    testXYpair[splitFile[0]] = splitFile[1]
    
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
    print(dframe1)
    print("\n")
    print('Training set Y2 deviation square of 50 ideal function')
    dframe2 = pd.DataFrame({'Trainset_Y2': trainset_Y2,
    'd^2(Y1)': devY2res1,'d^2(Y2)': devY2res2,'d^2(Y3)': devY2res3,'d^2(Y4)': devY2res4,'d^2(Y5)': devY2res5,'d^2(Y6)': devY2res6,'d^2(Y7)': devY2res7,'d^2(Y8)': devY2res8,'d^2(Y9)': devY2res9,'d^2(Y10)': devY2res10, 
    'd^2(Y11)': devY2res11,'d^2(Y12)': devY2res12,'d^2(Y13)': devY2res13,'d^2(Y14)': devY2res14,'d^2(Y15)': devY2res15,'d^2(Y16)': devY2res16,'d^2(Y17)': devY2res17,'d^2(Y18)': devY2res18,'d^2(Y19)': devY2res19,'d^2(Y20)': devY2res20,
    'd^2(Y21)': devY2res21,'d^2(Y22)': devY2res22,'d^2(Y23)': devY2res23,'d^2(Y24)': devY2res24,'d^2(Y25)': devY2res25,'d^2(Y26)': devY2res26,'d^2(Y27)': devY2res27,'d^2(Y28)': devY2res28,'d^2(Y29)': devY2res29,'d^2(Y30)': devY2res30,
    'd^2(Y31)': devY2res31,'d^2(Y32)': devY2res32,'d^2(Y33)': devY2res33,'d^2(Y34)': devY2res34,'d^2(Y35)': devY2res35,'d^2(Y36)': devY2res36,'d^2(Y37)': devY2res37,'d^2(Y38)': devY2res38,'d^2(Y39)': devY2res39,'d^2(Y40)': devY2res40,
    'd^2(Y41)': devY2res41,'d^2(Y42)': devY2res42,'d^2(Y43)': devY2res43,'d^2(Y44)': devY2res44,'d^2(Y45)': devY2res45,'d^2(Y46)': devY2res46,'d^2(Y47)': devY2res47,'d^2(Y48)': devY2res48,'d^2(Y49)': devY2res49,'d^2(Y50)': devY2res50
    })
    print(dframe2)
    print("\n")
    print('Training set Y3 deviation square of 50 ideal function')
    dframe3 = pd.DataFrame({'Trainset_Y3': trainset_Y3,
    'd^2(Y1)': devY3res1,'d^2(Y2)': devY3res2,'d^2(Y3)': devY3res3,'d^2(Y4)': devY3res4,'d^2(Y5)': devY3res5,'d^2(Y6)': devY3res6,'d^2(Y7)': devY3res7,'d^2(Y8)': devY3res8,'d^2(Y9)': devY3res9,'d^2(Y10)': devY3res10, 
    'd^2(Y11)': devY3res11,'d^2(Y12)': devY3res12,'d^2(Y13)': devY3res13,'d^2(Y14)': devY3res14,'d^2(Y15)': devY3res15,'d^2(Y16)': devY3res16,'d^2(Y17)': devY3res17,'d^2(Y18)': devY3res18,'d^2(Y19)': devY3res19,'d^2(Y20)': devY3res20,
    'd^2(Y21)': devY3res21,'d^2(Y22)': devY3res22,'d^2(Y23)': devY3res23,'d^2(Y24)': devY3res24,'d^2(Y25)': devY3res25,'d^2(Y26)': devY3res26,'d^2(Y27)': devY3res27,'d^2(Y28)': devY3res28,'d^2(Y29)': devY3res29,'d^2(Y30)': devY3res30,
    'd^2(Y31)': devY3res31,'d^2(Y32)': devY3res32,'d^2(Y33)': devY3res33,'d^2(Y34)': devY3res34,'d^2(Y35)': devY3res35,'d^2(Y36)': devY3res36,'d^2(Y37)': devY3res37,'d^2(Y38)': devY3res38,'d^2(Y39)': devY3res39,'d^2(Y40)': devY3res40,
    'd^2(Y41)': devY3res41,'d^2(Y42)': devY3res42,'d^2(Y43)': devY3res43,'d^2(Y44)': devY3res44,'d^2(Y45)': devY3res45,'d^2(Y46)': devY3res46,'d^2(Y47)': devY3res47,'d^2(Y48)': devY3res48,'d^2(Y49)': devY3res49,'d^2(Y50)': devY3res50
    })
    print(dframe3)
    print("\n")
    print('Training set Y4 deviation square of 50 ideal function')
    dframe4 = pd.DataFrame({'Trainset_Y3': trainset_Y4,
    'd^2(Y1)': devY4res1,'d^2(Y2)': devY4res2,'d^2(Y3)': devY4res3,'d^2(Y4)': devY4res4,'d^2(Y5)': devY4res5,'d^2(Y6)': devY4res6,'d^2(Y7)': devY4res7,'d^2(Y8)': devY4res8,'d^2(Y9)': devY4res9,'d^2(Y10)': devY4res10, 
    'd^2(Y11)': devY4res11,'d^2(Y12)': devY4res12,'d^2(Y13)': devY4res13,'d^2(Y14)': devY4res14,'d^2(Y15)': devY4res15,'d^2(Y16)': devY4res16,'d^2(Y17)': devY4res17,'d^2(Y18)': devY4res18,'d^2(Y19)': devY4res19,'d^2(Y20)': devY4res20,
    'd^2(Y21)': devY4res21,'d^2(Y22)': devY4res22,'d^2(Y23)': devY4res23,'d^2(Y24)': devY4res24,'d^2(Y25)': devY4res25,'d^2(Y26)': devY4res26,'d^2(Y27)': devY4res27,'d^2(Y28)': devY4res28,'d^2(Y29)': devY4res29,'d^2(Y30)': devY4res30,
    'd^2(Y31)': devY4res31,'d^2(Y32)': devY4res32,'d^2(Y33)': devY4res33,'d^2(Y34)': devY4res34,'d^2(Y35)': devY4res35,'d^2(Y36)': devY4res36,'d^2(Y37)': devY4res37,'d^2(Y38)': devY4res38,'d^2(Y39)': devY4res39,'d^2(Y40)': devY4res40,
    'd^2(Y41)': devY4res41,'d^2(Y42)': devY4res42,'d^2(Y43)': devY4res43,'d^2(Y44)': devY4res44,'d^2(Y45)': devY4res45,'d^2(Y46)': devY4res46,'d^2(Y47)': devY4res47,'d^2(Y48)': devY4res48,'d^2(Y49)': devY4res49,'d^2(Y50)': devY4res50
    })
    print(dframe4)
 #########################################################################################################################################################
    """
    Putting the summation of all the training set into a dictionary
    idY1 - idY50 represent summation of deviation of ideal function Y1 to Y50

    """
    # Dictionary of train set Y1, Key = Y1idY1 - Y1idY50 and the value = sumY1res1 - sumY1res50
    trainsetY1Sum = {'Y1idY1':sumY1res1,'Y1idY2':sumY1res2,'Y1idY3':sumY1res3,'Y1idY4':sumY1res4,'Y1idY5':sumY1res5,'Y1idY6':sumY1res6,'Y1idY7':sumY1res7,'Y1idY8':sumY1res8,'Y1idY9':sumY1res9,'Y1idY10':sumY1res10,
    'Y1idY11':sumY1res11,'Y1idY12':sumY1res12,'Y1idY13':sumY1res13,'Y1idY14':sumY1res14,'Y1idY15':sumY1res15,'Y1idY16':sumY1res16,'Y1idY17':sumY1res17,'Y1idY18':sumY1res18,'Y1idY19':sumY1res19,'Y1idY20':sumY1res20,
    'Y1idY21':sumY1res21,'Y1idY22':sumY1res22,'Y1idY23':sumY1res23,'Y1idY24':sumY1res24,'Y1idY25':sumY1res25,'Y1idY26':sumY1res26,'Y1idY27':sumY1res27,'Y1idY28':sumY1res28,'Y1idY29':sumY1res29,'Y1idY30':sumY1res30,
    'Y1idY31':sumY1res31,'Y1idY32':sumY1res32,'Y1idY33':sumY1res33,'Y1idY34':sumY1res34,'Y1idY35':sumY1res35,'Y1idY36':sumY1res36,'Y1idY37':sumY1res37,'Y1idY38':sumY1res38,'Y1idY39':sumY1res39,'Y1idY40':sumY1res40,
    'Y1idY41':sumY1res41,'Y1idY42':sumY1res42,'Y1idY43':sumY1res43,'Y1idY44':sumY1res44,'Y1idY45':sumY1res45,'Y1idY46':sumY1res46,'Y1idY47':sumY1res47,'Y1idY48':sumY1res48,'Y1idY49':sumY1res49,'Y1idY50':sumY1res50 
    }   
    # Dictionary of train set Y2, Key = idY1 - idY50 and the value = sumY2res1 - sumY2res50
    trainsetY2Sum = {'Y2idY1':sumY2res1,'Y2idY2':sumY2res2,'Y2idY3':sumY2res3,'Y2idY4':sumY2res4,'Y2idY5':sumY2res5,'Y2idY6':sumY2res6,'Y2idY7':sumY2res7,'Y2idY8':sumY2res8,'Y2idY9':sumY2res9,'Y2idY10':sumY2res10,
    'Y2idY11':sumY2res11,'Y2idY12':sumY2res12,'Y2idY13':sumY2res13,'Y2idY14':sumY2res14,'Y2idY15':sumY2res15,'Y2idY16':sumY2res16,'Y2idY17':sumY2res17,'Y2idY18':sumY2res18,'Y2idY19':sumY2res19,'Y2idY20':sumY2res20,
    'Y2idY21':sumY2res21,'Y2idY22':sumY2res22,'Y2idY23':sumY2res23,'Y2idY24':sumY2res24,'Y2idY25':sumY2res25,'Y2idY26':sumY2res26,'Y2idY27':sumY2res27,'Y2idY28':sumY2res28,'Y2idY29':sumY2res29,'Y2idY30':sumY2res30,
    'Y2idY31':sumY2res31,'Y2idY32':sumY2res32,'Y2idY33':sumY2res33,'Y2idY34':sumY2res34,'Y2idY35':sumY2res35,'Y2idY36':sumY2res36,'Y2idY37':sumY2res37,'Y2idY38':sumY2res38,'Y2idY39':sumY2res39,'Y2idY40':sumY2res40,
    'Y2idY41':sumY2res41,'Y2idY42':sumY2res42,'Y2idY43':sumY2res43,'Y2idY44':sumY2res44,'Y2idY45':sumY2res45,'Y2idY46':sumY2res46,'Y2idY47':sumY2res47,'Y2idY48':sumY2res48,'Y2idY49':sumY2res49,'Y2idY50':sumY2res50 
    }   
    # Dictionary of train set Y3, Key = Y3idY1 - Y3idY50 and the value = sumY3res1 - sumY3res50
    trainsetY3Sum = {'Y3idY1':sumY3res1,'Y3idY2':sumY3res2,'Y3idY3':sumY3res3,'Y3idY4':sumY3res4,'Y3idY5':sumY3res5,'Y3idY6':sumY3res6,'Y3idY7':sumY3res7,'Y3idY8':sumY3res8,'Y3idY9':sumY3res9,'Y3idY10':sumY3res10,
    'Y3idY11':sumY3res11,'Y3idY12':sumY3res12,'Y3idY13':sumY3res13,'Y3idY14':sumY3res14,'Y3idY15':sumY3res15,'Y3idY16':sumY3res16,'Y3idY17':sumY3res17,'Y3idY18':sumY3res18,'Y3idY19':sumY3res19,'Y3idY20':sumY3res20,
    'Y3idY21':sumY3res21,'Y3idY22':sumY3res22,'Y3idY23':sumY3res23,'Y3idY24':sumY3res24,'Y3idY25':sumY3res25,'Y3idY26':sumY3res26,'Y3idY27':sumY3res27,'Y3idY28':sumY3res28,'Y3idY29':sumY3res29,'Y3idY30':sumY3res30,
    'Y3idY31':sumY3res31,'Y3idY32':sumY3res32,'Y3idY33':sumY3res33,'Y3idY34':sumY3res34,'Y3idY35':sumY3res35,'Y3idY36':sumY3res36,'Y3idY37':sumY3res37,'Y3idY38':sumY3res38,'Y3idY39':sumY3res39,'Y3idY40':sumY3res40,
    'Y3idY41':sumY3res41,'Y3idY42':sumY3res42,'Y3idY43':sumY3res43,'Y3idY44':sumY3res44,'Y3idY45':sumY3res45,'Y3idY46':sumY3res46,'Y3idY47':sumY3res47,'Y3idY48':sumY3res48,'Y3idY49':sumY3res49,'Y3idY50':sumY3res50 
    } 
    # Dictionary of train set Y4, Key = Y4idY1 - Y4idY50 and the value = sumY4res1 - sumY4res50
    trainsetY4Sum = {'Y4idY1':sumY4res1,'Y4idY2':sumY4res2,'Y4idY3':sumY4res3,'Y4idY4':sumY4res4,'Y4idY5':sumY4res5,'Y4idY6':sumY4res6,'Y4idY7':sumY4res7,'Y4idY8':sumY4res8,'Y4idY9':sumY4res9,'Y4idY10':sumY4res10,
    'Y4idY11':sumY4res11,'Y4idY12':sumY4res12,'Y4idY13':sumY4res13,'Y4idY14':sumY4res14,'Y4idY15':sumY4res15,'Y4idY16':sumY4res16,'Y4idY17':sumY4res17,'Y4idY18':sumY4res18,'Y4idY19':sumY4res19,'Y4idY20':sumY4res20,
    'Y4idY21':sumY4res21,'Y4idY22':sumY4res22,'Y4idY23':sumY4res23,'Y4idY24':sumY4res24,'Y4idY25':sumY4res25,'Y4idY26':sumY4res26,'Y4idY27':sumY4res27,'Y4idY28':sumY4res28,'Y4idY29':sumY4res29,'Y4idY30':sumY4res30,
    'Y4idY31':sumY4res31,'Y4idY32':sumY4res32,'Y4idY33':sumY4res33,'Y4idY34':sumY4res34,'Y4idY35':sumY4res35,'Y4idY36':sumY4res36,'Y4idY37':sumY4res37,'Y4idY38':sumY4res38,'Y4idY39':sumY4res39,'Y4idY40':sumY4res40,
    'Y4idY41':sumY4res41,'Y4idY42':sumY4res42,'Y4idY43':sumY4res43,'Y4idY44':sumY4res44,'Y4idY45':sumY4res45,'Y4idY46':sumY4res46,'Y4idY47':sumY4res47,'Y4idY48':sumY4res48,'Y4idY49':sumY4res49,'Y4idY50':sumY4res50 
    } 
    ########################################################################################################################################################################
 
    print("\n")
   ##################################################################################################  
    """
    Getting maximum values and their corresponding ideal function from the 
    trainset Y1 - Y4 

    """
    # fetching the identity of the maximum value from the sum of all y-deviation square of the trainset Y1 to Y4
    # first getting the maximum value's key from their dictionary
    
    max_trainset_Y1_key = square.maximumValue(trainsetY1Sum)
    max_trainset_Y2_key = square.maximumValue(trainsetY2Sum)
    max_trainset_Y3_key = square.maximumValue(trainsetY3Sum)
    max_trainset_Y4_key = square.maximumValue(trainsetY4Sum)

    #declaring variables and lists to hold the key and value from the dictionaries  
    global max_trainset_Y4_value, max_trainset_Y3_value, max_trainset_Y2_value, max_trainset_Y1_value
    trainsetY1Sum_value2 = []; trainsetY2Sum_value2 = []; trainsetY3Sum_value2 = []; trainsetY4Sum_value2 = []
    # getting corresponding maximum value for train set Y1
    for key,value in trainsetY1Sum.items():
        trainsetY1Sum_value2.append(value)
        if key == max_trainset_Y1_key:
            max_trainset_Y1_value = value
    # getting corresponding maximum value for train set Y2
    for key,value in trainsetY2Sum.items():
        trainsetY2Sum_value2.append(value)
        if key == max_trainset_Y2_key:
            max_trainset_Y2_value = value
    # getting corresponding value for train set Y3
    for key,value in trainsetY3Sum.items():
        trainsetY3Sum_value2.append(value)
        if key == max_trainset_Y3_key:
            max_trainset_Y3_value = value
    # getting corresponding value for train set Y4
    for key,value in trainsetY4Sum.items():
        trainsetY4Sum_value2.append(value)
        if key == max_trainset_Y4_key:
            max_trainset_Y4_value = value
    
    #choosing the maximum deviation between the maximum deviation of the slected four ideal functions
    # putting them in a list 
    # maximumDeviation_list = [max_trainset_Y1_value,max_trainset_Y2_value,max_trainset_Y3_value,max_trainset_Y4_value]
    maximumDeviation_list = [max_trainset_Y1_value,max_trainset_Y2_value,max_trainset_Y3_value,max_trainset_Y4_value]
    maximumDeviation = max(maximumDeviation_list)
    print("The maximum deviation is : " + str(maximumDeviation))
    print("\n")
 ##################################################################################################################################   
    
    """
    getting the value of test data X that matches with ideal set X
    the match values of X will use to select the corresponding values of Y 
    from the test.csv
    """
    idealsetX = set(idealX)
    testsetX = set(testX)
    bestFitX = list(testsetX.intersection(idealsetX))
    
        
    """
    using for loop fetch the Y values from the testXYpair dictionary
    the matchin Y values are stored in bestFitY list which will be use to calculate the
    deviation of Test set Y
    """
    bestFitY = [] # a list variable to hold all the values of mapping of Y in the test set
    
    for key,value in testXYpair.items():
        if key in bestFitX:
            
            bestFitY.append(value)
   
    """
    Fetch from the idealfunction table in rows from Y1 to Y50, functions that
    best fit the selected test set X values.
    These values will be kept in another 50 different list and will be used to calcuate the deviation 
    """
    #declaring multiple list to store data from the selected ideal functions from the ideal functiontable in the database
    testIdealY1 = []; testIdealY2 = []; testIdealY3 = []; testIdealY4 = [];  testIdealY5 = [];  testIdealY6 = [];  testIdealY7 = [];  testIdealY8 = [];  testIdealY9 = [];  testIdealY10 = []
    testIdealY11 = []; testIdealY12 = []; testIdealY13 = []; testIdealY14 = [];  testIdealY15 = [];  testIdealY16 = [];  testIdealY17 = [];  testIdealY18 = [];  testIdealY19 = [];  testIdealY20 = []
    testIdealY21 = []; testIdealY22 = []; testIdealY23 = []; testIdealY24 = [];  testIdealY25 = [];  testIdealY26 = [];  testIdealY27 = [];  testIdealY28 = [];  testIdealY29 = [];  testIdealY30 = []
    testIdealY31 = []; testIdealY32 = []; testIdealY33 = []; testIdealY34 = [];  testIdealY35 = [];  testIdealY36 = [];  testIdealY37 = [];  testIdealY38 = [];  testIdealY39 = [];  testIdealY40 = []
    testIdealY41 = []; testIdealY42 = []; testIdealY43 = []; testIdealY44 = [];  testIdealY45 = [];  testIdealY46 = [];  testIdealY47 = [];  testIdealY48 = [];  testIdealY49 = [];  testIdealY50 = []

    # writing query to fetch the data from the database
    bestFitX_len = len(bestFitX)  # adding 1 to the length 
    for i in range(0,bestFitX_len):
        data = int(i)
        dbX = bestFitX[data]
        readData = engine.engine.execute('SELECT * FROM ideal_table where ideal_table.X = :id', id=dbX)
        for row in readData:
            testIdealY1.append(row[1])
            testIdealY2.append(row[2])
            testIdealY3.append(row[3])
            testIdealY4.append(row[4])
            testIdealY5.append(row[5])
            testIdealY6.append(row[6])
            testIdealY7.append(row[7])
            testIdealY8.append(row[8])
            testIdealY9.append(row[9])
            testIdealY10.append(row[10])
            testIdealY11.append(row[11])
            testIdealY12.append(row[12])
            testIdealY13.append(row[13])
            testIdealY14.append(row[14])
            testIdealY15.append(row[15])
            testIdealY16.append(row[16])
            testIdealY17.append(row[17])
            testIdealY18.append(row[18])
            testIdealY19.append(row[19])
            testIdealY20.append(row[20])
            testIdealY21.append(row[21])
            testIdealY22.append(row[22])
            testIdealY23.append(row[23])
            testIdealY24.append(row[24])
            testIdealY25.append(row[25])
            testIdealY26.append(row[26])
            testIdealY27.append(row[27])
            testIdealY28.append(row[28])
            testIdealY29.append(row[29])
            testIdealY30.append(row[30])
            testIdealY31.append(row[31])
            testIdealY32.append(row[32])
            testIdealY33.append(row[33])
            testIdealY34.append(row[43])
            testIdealY35.append(row[35])
            testIdealY36.append(row[36])
            testIdealY37.append(row[37])
            testIdealY38.append(row[38])
            testIdealY39.append(row[39])
            testIdealY40.append(row[40])
            testIdealY41.append(row[41])
            testIdealY42.append(row[42])
            testIdealY43.append(row[43])
            testIdealY44.append(row[44])
            testIdealY45.append(row[45])
            testIdealY46.append(row[46])
            testIdealY47.append(row[47])
            testIdealY48.append(row[48])
            testIdealY49.append(row[49])
            testIdealY50.append(row[50])
        
    readData.close() 
    #########################################################################################################
    """
    Calculating the deviation of the selected Y1 - Y50 values from the ideal function table that
    match with selected test set X values
    """
    #storing the results in a list
    testDevRes1 = square.deviation(bestFitY,testIdealY1)
    testSumRes1 = square.sumDeviation(testDevRes1) 
    testDevRes2 = square.deviation(bestFitY,testIdealY2)
    testSumRes2 = square.sumDeviation(testDevRes2) 
    testDevRes3 = square.deviation(bestFitY,testIdealY3)
    testSumRes3 = square.sumDeviation(testDevRes3) 
    testDevRes4 = square.deviation(bestFitY,testIdealY4)
    testSumRes4 = square.sumDeviation(testDevRes4) 
    testDevRes5 = square.deviation(bestFitY,testIdealY5)
    testSumRes5 = square.sumDeviation(testDevRes5) 
    testDevRes6 = square.deviation(bestFitY,testIdealY6)
    testSumRes6 = square.sumDeviation(testDevRes6) 
    testDevRes7 = square.deviation(bestFitY,testIdealY7)
    testSumRes7 = square.sumDeviation(testDevRes7) 
    testDevRes8 = square.deviation(bestFitY,testIdealY8)
    testSumRes8 = square.sumDeviation(testDevRes8) 
    testDevRes9 = square.deviation(bestFitY,testIdealY9)
    testSumRes9 = square.sumDeviation(testDevRes9) 
    testDevRes10 = square.deviation(bestFitY,testIdealY10)
    testSumRes10 = square.sumDeviation(testDevRes10) 
#----------------------------------------------------------------------
    testDevRes11 = square.deviation(bestFitY,testIdealY11)
    testSumRes11 = square.sumDeviation(testDevRes11) 
    testDevRes12 = square.deviation(bestFitY,testIdealY12)
    testSumRes12 = square.sumDeviation(testDevRes12) 
    testDevRes13 = square.deviation(bestFitY,testIdealY13)
    testSumRes13 = square.sumDeviation(testDevRes13) 
    testDevRes14 = square.deviation(bestFitY,testIdealY14)
    testSumRes14 = square.sumDeviation(testDevRes14) 
    testDevRes15 = square.deviation(bestFitY,testIdealY15) 
    testSumRes15 = square.sumDeviation(testDevRes15) 
    testDevRes16 = square.deviation(bestFitY,testIdealY16)
    testSumRes16 = square.sumDeviation(testDevRes16) 
    testDevRes17 = square.deviation(bestFitY,testIdealY17)
    testSumRes17 = square.sumDeviation(testDevRes17) 
    testDevRes18 = square.deviation(bestFitY,testIdealY18)
    testSumRes18 = square.sumDeviation(testDevRes18) 
    testDevRes19 = square.deviation(bestFitY,testIdealY19)
    testSumRes19 = square.sumDeviation(testDevRes19) 
    testDevRes20 = square.deviation(bestFitY,testIdealY20)
    testSumRes20 = square.sumDeviation(testDevRes20) 
#-----------------------------------------------------------------------
    testDevRes21 = square.deviation(bestFitY,testIdealY21)
    testSumRes21 = square.sumDeviation(testDevRes21) 
    testDevRes22 = square.deviation(bestFitY,testIdealY22)
    testSumRes22 = square.sumDeviation(testDevRes22) 
    testDevRes23 = square.deviation(bestFitY,testIdealY23)
    testSumRes23 = square.sumDeviation(testDevRes23) 
    testDevRes24 = square.deviation(bestFitY,testIdealY24)
    testSumRes24 = square.sumDeviation(testDevRes24) 
    testDevRes25 = square.deviation(bestFitY,testIdealY25)
    testSumRes25 = square.sumDeviation(testDevRes25) 
    testDevRes26 = square.deviation(bestFitY,testIdealY26)
    testSumRes26 = square.sumDeviation(testDevRes26) 
    testDevRes27 = square.deviation(bestFitY,testIdealY27)
    testSumRes27 = square.sumDeviation(testDevRes27) 
    testDevRes28 = square.deviation(bestFitY,testIdealY28)
    testSumRes28 = square.sumDeviation(testDevRes28) 
    testDevRes29 = square.deviation(bestFitY,testIdealY29)
    testSumRes29 = square.sumDeviation(testDevRes29) 
    testDevRes30 = square.deviation(bestFitY,testIdealY30)
    testSumRes30 = square.sumDeviation(testDevRes30) 
#-------------------------------------------------------------------------
    testDevRes31 = square.deviation(bestFitY,testIdealY31)
    testSumRes31 = square.sumDeviation(testDevRes31) 
    testDevRes32 = square.deviation(bestFitY,testIdealY32)
    testSumRes32 = square.sumDeviation(testDevRes32) 
    testDevRes33 = square.deviation(bestFitY,testIdealY33)
    testSumRes33 = square.sumDeviation(testDevRes33) 
    testDevRes34 = square.deviation(bestFitY,testIdealY34)
    testSumRes34 = square.sumDeviation(testDevRes34) 
    testDevRes35 = square.deviation(bestFitY,testIdealY35)
    testSumRes35 = square.sumDeviation(testDevRes35) 
    testDevRes36 = square.deviation(bestFitY,testIdealY36)
    testSumRes36 = square.sumDeviation(testDevRes36) 
    testDevRes37 = square.deviation(bestFitY,testIdealY37)
    testSumRes37 = square.sumDeviation(testDevRes37) 
    testDevRes38 = square.deviation(bestFitY,testIdealY38)
    testSumRes38 = square.sumDeviation(testDevRes38) 
    testDevRes39 = square.deviation(bestFitY,testIdealY39)
    testSumRes39 = square.sumDeviation(testDevRes39) 
    testDevRes40 = square.deviation(bestFitY,testIdealY40)
    testSumRes40 = square.sumDeviation(testDevRes40) 
#----------------------------------------------------------------------
    testDevRes41 = square.deviation(bestFitY,testIdealY41)
    testSumRes41 = square.sumDeviation(testDevRes41) 
    testDevRes42 = square.deviation(bestFitY,testIdealY42)
    testSumRes42 = square.sumDeviation(testDevRes42) 
    testDevRes43 = square.deviation(bestFitY,testIdealY43)
    testSumRes43 = square.sumDeviation(testDevRes43) 
    testDevRes44 = square.deviation(bestFitY,testIdealY44)
    testSumRes44 = square.sumDeviation(testDevRes44) 
    testDevRes45 = square.deviation(bestFitY,testIdealY45)
    testSumRes45 = square.sumDeviation(testDevRes45) 
    testDevRes46 = square.deviation(bestFitY,testIdealY46)
    testSumRes46 = square.sumDeviation(testDevRes46) 
    testDevRes47 = square.deviation(bestFitY,testIdealY47)
    testSumRes47 = square.sumDeviation(testDevRes47) 
    testDevRes48 = square.deviation(bestFitY,testIdealY48)
    testSumRes48 = square.sumDeviation(testDevRes48) 
    testDevRes49 = square.deviation(bestFitY,testIdealY49)
    testSumRes49 = square.sumDeviation(testDevRes49) 
    testDevRes50 = square.deviation(bestFitY,testIdealY50)
    testSumRes50 = square.sumDeviation(testDevRes50) 
    #################################################################################
    """
    Putting the summation of all the test set into a dictionary
    testidY1 - testidY50 represent summation of deviation of test set Y1 to Y50

    """
    # Dictionary of test set Y1, Key = testidY1 - testidY50 and the value = testSumRes1 - testSumRes50
    testSum = {'testidY1':testSumRes1,'testidY2':testSumRes2,'testidY3':testSumRes3,'testidY4':testSumRes4,'testidY5':testSumRes5,'testidY6':testSumRes6,'testidY7':testSumRes7,'testidY8':testSumRes8,'testidY9':testSumRes9,'testidY10':testSumRes10,
    'testidY11':testSumRes11,'testidY12':testSumRes12,'testidY13':testSumRes13,'testidY14':testSumRes14,'testidY15':testSumRes15,'testidY16':testSumRes16,'testidY17':testSumRes17,'testidY18':testSumRes18,'testidY19':testSumRes19,'testidY20':testSumRes20,
    'testidY21':testSumRes21,'testidY22':testSumRes22,'testidY23':testSumRes23,'testidY24':testSumRes24,'testidY25':testSumRes25,'testidY26':testSumRes26,'testidY27':testSumRes27,'testidY28':testSumRes28,'testidY29':testSumRes29,'testidY30':testSumRes30,
    'testidY31':testSumRes31,'testidY32':testSumRes32,'testidY33':testSumRes33,'testidY34':testSumRes34,'testidY35':testSumRes35,'testidY36':testSumRes36,'testidY37':testSumRes37,'testidY38':testSumRes38,'testidY39':testSumRes39,'testidY40':testSumRes40,
    'testidY41':testSumRes41,'testidY42':testSumRes42,'testidY43':testSumRes43,'testidY44':testSumRes44,'testidY45':testSumRes45,'testidY46':testSumRes46,'testidY47':testSumRes47,'testidY48':testSumRes48,'testidY49':testSumRes49,'testidY50':testSumRes50 
    }   
    
    #Displaying the results of the into a pandas dataframe 
    print('Test set deviation square of 50 ideal function')
    dframetestset = pd.DataFrame({'TestsetX': bestFitX,
    'TestDev(Y1)': testSumRes1,'TestDev(Y2)': testSumRes2,'TestDev(Y3)': testSumRes3,'TestDev(Y4)': testSumRes4,'TestDev(Y5)': testSumRes5,'TestDev(Y6)': testSumRes6,'TestDev(Y7)': testSumRes7,'TestDev(Y8)': testSumRes8,'TestDev(Y9)': testSumRes9,'TestDev(Y10)': testSumRes10, 
    'TestDev(Y11)': testSumRes11,'TestDev(Y12)': testSumRes12,'TestDev(Y13)': testSumRes13,'TestDev(Y14)': testSumRes14,'TestDev(Y15)': testSumRes15,'TestDev(Y16)': testSumRes16,'TestDev(Y17)': testSumRes17,'TestDev(Y18)': testSumRes18,'TestDev(Y19)': testSumRes19,'TestDev(Y20)': testSumRes20,
    'TestDev(Y21)': testSumRes21,'TestDev(Y22)': testSumRes22,'TestDev(Y23)': testSumRes23,'TestDev(Y24)': testSumRes24,'TestDev(Y25)': testSumRes25,'TestDev(Y26)': testSumRes26,'TestDev(Y27)': testSumRes27,'TestDev(Y28)': testSumRes28,'TestDev(Y29)': testSumRes29,'TestDev(Y30)': testSumRes30,
    'TestDev(Y31)': testSumRes31,'TestDev(Y32)': testSumRes32,'TestDev(Y33)': testSumRes33,'TestDev(Y34)': testSumRes34,'TestDev(Y35)': testSumRes35,'TestDev(Y36)': testSumRes36,'TestDev(Y37)': testSumRes37,'TestDev(Y38)': testSumRes38,'TestDev(Y39)': testSumRes39,'TestDev(Y40)': testSumRes40,
    'TestDev(Y41)': testSumRes41,'TestDev(Y42)': testSumRes42,'TestDev(Y43)': testSumRes43,'TestDev(Y44)': testSumRes44,'TestDev(Y45)': testSumRes45,'TestDev(Y46)': testSumRes46,'TestDev(Y47)': testSumRes47,'TestDev(Y48)': testSumRes48,'TestDev(Y49)': testSumRes49,'d^2(Y50)': testSumRes50
    })
    print(dframetestset)

    """
    list to store values that are less or equal to the maximum deviation from the trainset 
    and the ideal function 
    looping through the deviated test set to select the qualify values
    """

    selectedTestValues = {key: value for key, value in testSum.items() if value <= maximumDeviation}
    # print(selectedTestValues)
    
    maximumTestSum_values = []
    maximumTestKey = square.maximumValue(testSum)
    # getting corresponding value for train set Y4
    global max_test_value
    for key,value in testSum.items():
        maximumTestSum_values.append(value)
        if key == maximumTestKey:
            max_test_value = value
    
    # print(maximumTestKey)
    # print(max_test_value)
    # print(maximumDeviation) 
    #-----------------------------------------------
    TestValuesChosen = []
    for k,v in selectedTestValues.items():
        TestValuesChosen.append(v)

    """
    Factor square root of the deviation of the difference between 
    trainset(A) and Ideal function (c)
    """
    factor_trainsetY1 = square.factors(trainsetY1Sum_value2)
    print(factor_trainsetY1)
    print("\n factor y2")
    factor_trainsetY2 = square.factors(trainsetY2Sum_value2)
    print(factor_trainsetY2)
    print("\n factor y3")
    factor_trainsetY3 = square.factors(trainsetY3Sum_value2)
    print(factor_trainsetY3)
    print("\n factor y4")
    factor_trainsetY4 = square.factors(trainsetY4Sum_value2)
    print(factor_trainsetY4)
    print("\n factor test")
    factor_testset = square.factors(TestValuesChosen)
    print(factor_testset)
    print("\n maximum factor y1")
    # find max value factor in the factors
    max_factors_trainsetY1 = square.max_factor(factor_trainsetY1)
    print(max_factors_trainsetY1)
    print("\n maximum factor y2")
    max_factors_trainsetY2 = square.max_factor(factor_trainsetY2)
    print(max_factors_trainsetY2)
    print("\n maximum factor y3")
    max_factors_trainsetY3 = square.max_factor(factor_trainsetY3)
    print(max_factors_trainsetY3)
    print("\n maximum factor y4")
    max_factors_trainsetY4 = square.max_factor(factor_trainsetY4)
    print(max_factors_trainsetY4)
    print("\n maximum factor test")
    max_factors_testset = square.max_factor(factor_testset)
    print(max_factors_testset)
   ###########################################################################################
    print("\n finding the values that match")
    #changing the arrays into sets
    f_test = set(max_factors_testset)
    f_y1 = set(max_factors_trainsetY1)
    f_y2 = set(max_factors_trainsetY2)
    f_y3 = set(max_factors_trainsetY3)
    f_y4 = set(max_factors_trainsetY4)
    #declaring lists to store selected values and keys 
    bestfit_test =[]
    bestfit_key = []
    delta_y = []
    #checking if there is a relation between the datasets
    if(f_test.intersection(f_y1)):
        bestfit_test = list(f_test.intersection(f_y1))
        if(bestfit_test):
            for k,v in trainsetY1Sum.items():
                bestfit_key.append(k)
    elif(f_test.intersection(f_y2)):
        bestfit_test = list(f_test.intersection(f_y2))
        if not bestfit_test:
            pass
        # if(bestfit_test):
        #     for k,v in trainsetY2Sum.items():
        #         bestfit_key.append(k)
        else:
            # if(bestfit_test):
            for k,v in trainsetY2Sum.items():
                bestfit_key.append(k)
    elif(f_test.intersection(f_y3)):
        bestfit_test = list(f_test.intersection(f_y3))
        if(bestfit_test):
            for k,v in trainsetY3Sum.items():
                bestfit_key.append(k)
    elif(f_test.intersection(f_y4)):
        bestfit_test = list(f_test.intersection(f_y4))
        if(bestfit_test):
            for k,v in trainsetY4Sum.items():
                bestfit_key.append(k)
    for k,v in testSum.items():
        delta_y.append(k)

    print(bestfit_test)
    # print(len(max_factors_testset))
    print("\n Corresponding of the best fit Keys ")
    print(bestfit_key)
    print("\n")

    ###############################################################
    if(mytables.table_exist("test_data_table")):
        print("Test data table already exit in the database")
    else:

        mytables.test_data_table() #invoking method to create table test data in the database
        no_records_test = 0
        limit = len(delta_y)
        for i in range(0, len(bestFitX)):
            # if(i > len(delta_y)):
                # break
            # else:
            if(i < limit):
                #inserting records from the ideal csv file into the database
                insert_testdata = test_data.insert().values( X_Test_Function = bestFitX[i], Y_Test_Function = bestFitY[i], Delta_Y = delta_y[i], No_of_Ideal_Func = bestfit_key[i] )
                # insert_testdata = test_data.insert().values( X_Test_Function = bestFitX[i], Y_Test_Function = bestFitY[i], Delta_Y = delta_y[0], No_of_Ideal_Func = bestfit_key[0] )
                conn = mytables.engine.connect()
                result = conn.execute(insert_testdata)
                no_records_test += 1
                print("Inserting ideal record no. {}".format(no_records_test))
            else:
                pass  
        #----------------------------------------------------------------
    #############################################################################################
       
    '''
    Plotting the graph of the training set using  Bokeh library
    '''
    #plotting trainset Y1
    graph = plot_graph("train.csv", "trainset_y1.html",'x', 'y1','red', "trainset_y1")
    graph.plotgraph()
    #plotting trainset Y2
    graph = plot_graph("train.csv", "trainset_y2.html",'x', 'y2','blue', "trainset_y2")
    graph.plotgraph()
    #plotting trainset Y3
    graph = plot_graph("train.csv", "trainset_y3.html",'x', 'y3','green', "trainset_y3")
    graph.plotgraph()
    #plotting trainset Y4
    graph = plot_graph("train.csv", "trainset_y4.html",'x', 'y4','orange', "trainset_y4")
    graph.plotgraph()

    #################################################################################### 
    
    '''
    Plotting the graph of the test set using Bokeh library
    '''
    #plotting test set
    graph1 = plot_graph("test.csv", "testset.html",'x', 'y','brown', "Test set")
    graph1.plotgraph()

    ############################################################################################
    '''
    Plotting the graph of the chosen ideal functions using Bokeh library
    '''
   
    idealFunctionX =[]
    counter = len(trainsetY1Sum) + 1
    for i in range(1, counter):
        idealFunctionX.append(i)
    #plotting ideal function 1 and 2
    output_file("ideal_function.html")
    plotFunction=figure(plot_width = 600, plot_height=600,x_axis_label="x axis",y_axis_label="y axis")
    plotFunction.circle_dot(x= idealFunctionX, y = trainsetY1Sum_value2,size=10,color='red',legend="Ideal function 1")
    plotFunction.circle_dot(x = idealFunctionX, y = trainsetY2Sum_value2,size=10,color='green',legend="Ideal function 2")
    show(plotFunction)
    #plotting ideal function 3 and 4
    output_file("ideal_function2.html")
    plotFunction2=figure(plot_width = 600, plot_height=600,x_axis_label="x axis",y_axis_label="y axis")
    plotFunction2.circle_dot(x = idealFunctionX, y = trainsetY3Sum_value2,size=10,color='orange',legend="Ideal function 3")
    plotFunction2.circle_dot(x = idealFunctionX, y = trainsetY4Sum_value2,size=10,color='blue',legend="Ideal function 4")
    show(plotFunction2)

    ############################################################################################

if __name__ == '__main__':
    main() 















