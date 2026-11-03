import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

BASE_MODEL_NAME = "Qwen/Qwen3-0.6B"
TOKENIZER = AutoTokenizer.from_pretrained(BASE_MODEL_NAME)
BASE_MODEL = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL_NAME, device_map="auto", dtype=torch.bfloat16
)
DEVICE = "cuda" if torch.cuda.is_available() else "mps"