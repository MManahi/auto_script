# import required modules
import pandas as pd

dataFrame = pd.read_csv('result.csv', header= None, encoding= 'utf-8-sig')
dataFrame = dataFrame.drop(dataFrame.columns[[1]], axis=1)
dataFrame= dataFrame.tail(-1)
#dataFrame.columns = ['source_a', 'source_b', 'similairtiy']
#dataFrame.columns[[1]] = dataFrame.columns[[2]].str.replace(r"\((.*)\)", "").str.extract("([A-Z]+)", expand=True)

dataFrame.to_csv('result_modified.csv', index= False)