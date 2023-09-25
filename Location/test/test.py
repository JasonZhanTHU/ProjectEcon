import pandas


df = pandas.read_excel('../processed_sample.xlsx')


for i in range(0, 500):

    developer = df.loc[i, 'developer']
    individual = df.loc[i, 'individual']

    print(developer, ' ',individual)