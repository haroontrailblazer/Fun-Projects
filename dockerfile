<<<<<<< HEAD:EMI Calculator/dockerfile
FROM python:3.13.8-slim
WORKDIR /main
COPY . /main
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE ${PORT}
=======
FROM python:3.13.8-slim
WORKDIR /main
COPY . /main
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE ${PORT}
>>>>>>> bcbe3dabd8bf81c46fbc8482a441dbc8a3cde786:dockerfile
CMD ["sh", "-c", "streamlit run main.py --server.port=8501 --server.address=0.0.0.0"]