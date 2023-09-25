
import json
#from transformers import pipeline

# Load the sentiment analysis model
#nlp = pipeline("sentiment-analysis")


with open('../../files/GLM/formalized_ad_reviews.json', 'r') as f:
    data = json.load(f)


# Classify each sentence and print the result
for key in data:
    for id in data[key]:
        #print(data[key][id]['review'])
        # sentiment = nlp(data[key][id]['review'])
        sentiment=1
        data[key][id]['sentiment']=sentiment

with open('../../files/GLM/formalized_ad_reviews.json', 'w') as f:
    json.dump(data, f, indent=4)