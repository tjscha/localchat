from utils import load, generate

model, tokenizer = load("../../../mixtral/Mixtral-8x7B-v0.1-hf-4bit-mlx")
response = generate(model, tokenizer, prompt="hello", verbose=True)
