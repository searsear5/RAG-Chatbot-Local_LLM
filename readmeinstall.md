install python 3.11

py -3.11 -m venv venv

.\venv\Scripts\Activate #for activate venv

pip install -r requirements.txt

install Ollama

ollama pull llama3.2

ollama pull mxbai-embed-large #  use embedding model for generate document to vector and  send to vector database

ollama serve

docker compose up -d

docker ps


