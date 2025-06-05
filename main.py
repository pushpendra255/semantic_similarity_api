from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer, util

app = FastAPI()
model = SentenceTransformer('all-MiniLM-L6-v2')

class TextPair(BaseModel):
    text1: str
    text2: str

@app.post("/similarity")
def get_similarity(pair: TextPair):
    emb1 = model.encode(pair.text1, convert_to_tensor=True)
    emb2 = model.encode(pair.text2, convert_to_tensor=True)
    score = util.cos_sim(emb1, emb2).item()
    return {"similarity_score": round(score, 3)}
