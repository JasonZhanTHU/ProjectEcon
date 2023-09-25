import pandas
import json

df = pandas.read_excel('files/random_sample.xlsx')

search_info=['payment','location','birth','gender','phone','email','device','education','profession','ip','history','photo','contact']

df['Payment'] = None
df['Location'] = None
df['Birth'] = None
df['Gender'] = None
df['Phone'] = None
df['Email'] = None
df['Address'] = None
df['Education'] = None
df['Profession'] = None
df['IP'] = None
df['History'] = None
df['Photo'] = None
df['Contact'] = None

with open('files/response2.json') as f:
    response = json.load(f)

for i in range(0, 500):
    if str(i) in response:
        print(i," has following privacy permissions")
        if(response[str(i)][:3]!="I'm"):
            for info in search_info:
                if info in response[str(i)].lower():
                    print(info,end=' ')
        print('\n')

# import pandas as pd
#
# # Create a sample DataFrame
# data = {'Name': ['Alice', 'Bob', 'Charlie'],
#         'Age': [25, 30, 22]}
# df = pd.DataFrame(data)
#
# # Create a new row
# new_row = {'Name': 'David', 'Age': 28}
#
# # Concatenate the new row to the DataFrame
# df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
#
# print(df)


'''
Name, A ge, Date of birth, Gender
Phone number, Email address, Physical address
Education information, Professional informationDevice identifier
IP address, Browsing and search history, Purchasinghistory
Audio, Photo
Contact list
'''