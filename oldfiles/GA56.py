import plotly.express as px 
import pandas as pd



def ExamplePlot(d):
  df = pd.DataFrame(data=d)

  fig = px.bar(df, x='Age Quantile', y='Instances',color = 'Test1',text='VariableName')
  fig.show()
  


assignmentdataset = {'Instances': [334,315,366,294,281,319,359,380,313,299], 
                      'Age Quantile': [0,2,4,5,6,7,9,11,13,14], 
                      'Test1': ["Y","N","Y","N","Y","N","N","Y","N","Y"], 
                      'VariableName': ["Here","you","can","put","text","to","be","shown","tilburg","eindhoven"]}

ExamplePlot(assignmentdataset)
  
