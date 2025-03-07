from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# 创建 FastAPI 应用
app = FastAPI()

# 初始化情感分析模型
classifier = pipeline('sentiment-analysis')
summarizer = pipeline('summarization')

# 创建请求模型
class Review(BaseModel):
    text: str

# 情感分析 API
@app.post("/analyze_sentiment/")
async def analyze_sentiment(review: Review):
    result = classifier(review.text)
    return {"sentiment": result}

# 智能摘要 API
@app.post("/summarize/")
async def summarize_review(review: Review):
    summary = summarizer(review.text, max_length=50, min_length=25, do_sample=False)
    return {"summary": summary[0]['summary_text']}