import pandas as pd
import numpy
import quandl


df = quandl.get('WIKI/GOOGL')

print(df.head())
