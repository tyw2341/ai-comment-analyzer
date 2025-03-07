from transformers import pipeline

# 加载情感分析模型
classifier = pipeline('sentiment-analysis')

# 加载智能摘要模型
summarizer = pipeline("summarization")

# 情感分析
def analyze_sentiment(review_text):
    result = classifier(review_text)
    return result

# 智能摘要
def summarize_review(review_text):
    summary = summarizer(review_text, max_length=50, min_length=25, do_sample=False)
    return summary[0]['summary_text']
