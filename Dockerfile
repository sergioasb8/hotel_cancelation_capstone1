FROM python:3.11-slim

RUN pip install pipenv --no-cache-dir

WORKDIR /app
COPY ["Pipfile","Pipfile.lock","./"]

RUN pipenv install --deploy --system && \
    rm -rf /root/.cache

COPY ["predict.py","train.py","dv.pkl","xgboost_model.pkl","./"]

EXPOSE 9696 

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "predict:app"] 