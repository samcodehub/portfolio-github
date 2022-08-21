import pandas as pd


data = {'Name':['Sam', 'jack', 'Bob', 'John'],
        'Age':[22,33,44,55],
        'Address':['us', 'uk', 'ger', 'fr'],
        'Jobs':['programmer', 'editor', 'manager', 'scientist']}

df = pd.DataFrame(data)
print(df)