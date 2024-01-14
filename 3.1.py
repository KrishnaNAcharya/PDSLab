import pandas as pd
data= {
    'A':10, 'B':20, 'C':30, 'D':40
}
mydata=pd.Series(data)

print(mydata['A'])
print(mydata[0])
