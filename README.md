This is a simple command line chat using MLX to generate and display text from a local model.

Use HuggingFace.co to download a model. This implementation makes use of Safetensors, so be sure the model has .safetensors included.

e.g. to use Mistral 7B Instruct:

git lfs install

git clone https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2

----------

Place your llm in the models folder. The folder should look like this for mistral:

-localchat

\---->mlxfiles

\---->models

\\\\--->Mistral-7B-Instruct-v0.2

\\\\\\\\\\--->config.json

\\\\\\\\\\--->generation_config.json

\\\\\\\\\\---> etc...

codechat.py

requirements.txt

----------

Using the terminal:

>> cd localchat

>> pip install -r requirements.txt

>> python codechat.py
