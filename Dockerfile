FROM pytorch/pytorch:1.12.1-cuda11.3-cudnn8-devel

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV FINNER=/opt/finner
ENV PATH="$FINNER/bin:$PATH"
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64

RUN apt-get update --fix-missing && \
    apt-get install -y build-essential git wget curl g++ default-jdk make && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
    
RUN python3 -m venv $FINNER
RUN $FINNER/bin/pip install --upgrade pip
RUN $FINNER/bin/pip install transformers seqeval fastprogress attrdict tqdm pandas pandarallel dart-fss ipywidgets matplotlib jupyterlab jupyterlab-git
RUN echo ". $FINNER/bin/activate" >> ~/.bashrc