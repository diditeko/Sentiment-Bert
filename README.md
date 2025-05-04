# Sentiment BERT Tweet

A BERT model fine-tuned for Indonesian tweet sentiment classification.  
This model classifies tweets into three sentiment categories:

- **Positive**
- **Negative**
- **Neutral**

## How to Use

```python
from transformers import pipeline

model = pipeline("text-classification", model="VIOLET21/sentiment-bert-indo")
result = model("Saya sangat senang hari ini!")
print(result)
```

or you can use space huggingface

https://huggingface.co/spaces/VIOLET21/Sentiment_Tweet
