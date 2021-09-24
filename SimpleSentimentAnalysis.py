from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#Read data from the file into the text variable
file = open("read.txt","r")
text = file.read()
file.close()

#Apply sentiment analysis through VADER
analyzer = SentimentIntensityAnalyzer()
score = analyzer.polarity_scores(text)
negative = (score["neg"] * 100)
neutral = (score["neu"] * 100)
positive = (score["pos"] * 100)

#Function for getting overall aggregate sentiment.
def get_result():
    if score["neg"] > score["pos"]:
        return "Negative"
    elif score["neg"] < score["pos"]:
        return "Positive"
    else:
        return "Neutral"

#Print results of sentiment analysis
print(f"This text was {negative}% negative, {neutral}% neutral, and {positive}% positive.")
print("This text would generally be considered " + get_result() + ".")