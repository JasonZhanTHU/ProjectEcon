
import json
import os
#from transformers import pipeline

# Load the sentiment analysis model
#nlp = pipeline("sentiment-analysis")


#folder_path = os.path.expanduser("~/autodl-tmp/all_reviews")
folder_path = os.path.expanduser("~/Downloads/all_reviews")

file_names = os.listdir(folder_path)

count=0

batch_size = 10

batches = [file_names[i:i+batch_size] for i in range(0, len(file_names), batch_size)]

flag=0
for batch in batches:

    processed=[]

    for file in batch:
        file_path = os.path.join(folder_path, file)
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            for item in data:
                if 'sentiment' in item:
                    break
                processed.append(item['review'][:512])


    sentiment = nlp(processed)

    at=0
    for file in batch:
        file_path = os.path.join(folder_path, file)
        flag=0
        with open(file_path, 'r') as f:
            data = json.load(f)
        res=[]
        for item in data:
            if 'sentiment' in item:
                flag=1
                break
            item['sentiment']=sentiment[at]
            at+=1
            res.append(item)
        if flag==0:
            with open(file_path, 'w') as f:
                json.dump(res, f, indent=4)