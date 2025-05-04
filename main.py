from transformers import pipeline

model = pipeline("text-classification", model="VIOLET21/sentiment-bert-tweetx")
result = model("Saya sangat senang hari ini!")
print(result)