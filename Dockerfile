# pull python base image
FROM python:3.10
# copy application files
RUN pwd && ls -lrth
ADD /model_api /model_api/
RUN pwd && ls -lrth
ADD /model_training/trained_models model_api/model_training/trained_models
RUN pwd && ls -lrth
ADD /model_training/encoder_models model_api/model_training/encoder_models
RUN pwd && ls -lrth model_api/model_training
RUN pwd && ls -lrth model_api/model_training/trained_models
RUN pwd && ls -lrth model_api/model_training/encoder_models
# specify working directory
WORKDIR /model_api
RUN pwd && ls -lrth
# update pip
RUN pip install --upgrade pip
# install dependencies
RUN pip install -r requirements.txt
# expose port for application
EXPOSE 8001
# start fastapi application
CMD ["python", "app/main.py"]