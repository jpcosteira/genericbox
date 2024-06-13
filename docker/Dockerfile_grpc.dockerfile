
# --------------------------------------
# Builder stage to generate .proto files
# --------------------------------------
ARG WORKSPACE="/protos"
FROM python:3.8.7-slim-buster 

ENV SERVICE_NAME=" "
# Path for the protos folder to copy
ARG WORKSPACE
RUN pip install --upgrade pip && \
    pip install grpcio==1.35.0 grpcio-tools==1.35.0 protobuf==3.14.0

WORKDIR ${WORKSPACE}
ENV WORKSPACE=${WORKSPACE}

# Compile proto file and remove it
CMD ["python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=.","${SERVICE_NAME}"]

