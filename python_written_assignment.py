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
Creating a class that holds method to connect of database
"""
class dbconnect(object):
    def __init__(self, engine, meta, echo):
        self.engine = create_engine(engine) 
        self.meta = meta
        self.echo = echo
        
   
    
    # method connectDB() holds the connecting string to connect to sqlite database through sqlAlchemy
   
        
"""
Creating a class table to hold all the methods of
that will be use to create tables in the database

This class will inherite from dbconnect to get the connecting 
string to the database

"""

class tables(dbconnect):
    def __init__(self, engine, meta, echo):
        super().__init__(engine,meta,echo)

    # def display(self, gift):
    #     print(self.first_name + self.lastname + gift)    
    #first method to create table for the training data set
    def trainingset_table(self):
        print("Creating table.......")
        try:
            
            traintable = Table(
                'train_table', self.meta, 
                Column('X', Float, primary_key = True), 
                Column('Y1', Float), 
                Column('Y2', Float),
                Column('Y3', Float),
                Column('Y4', Float),
            )
            self.meta.create_all(self.engine)
            print("Finish creating train_table")
        except SQLAlchemyError as error:
            print(error)
    
        
          

#main function for method calling
def main():
    # invoking tainingset_table() from tables class
    mytables = tables('sqlite:///writtenassignmentdatabase.db',MetaData(),True)
    mytables.trainingset_table()


if __name__ == '__main__':
    main() 















