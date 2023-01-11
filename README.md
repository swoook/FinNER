# Financial Named Entity Recognition: FinNER

- A repository of things I've learned while applying financial named entity recognition to Korean news

## Quickstart

1. Build an image from the `Dockerfile` at the `<repository_root_directory>`

    ```Bash
    docker build -t <image_name>:<tag_name> .
    ```
    
    - E.g.,
    
    ```Bash
    docker build -t finner:dev .
    ```
    
2. Run a container from the image `<image_name>:<tag_name>` built in step 1

    ```Bash
    docker run -itd --rm --shm-size=<shared_memory_size> --gpus all \
    --entrypoint /bin/bash \
    -v <host_volume>:<container_volume> \
    -p <host_port>:<container_port> \
    --name <container_name> \
    <image>:<tag>
    ```
    
    - E.g.,
    
    ```Bash
    docker run -itd --rm --shm-size=32G --gpus all \
    --entrypoint /bin/bash \
    -v /data/:/host_volume \
    -p 8888:8888 \
    --name FinNER \
    finner:dev
    ```

## Index

1. [Motivation](./examples/01_motivation)
2. [Financial named entities](./examples/02_financial_named_entities)
3. [NER datasets for Korean corpus](./examples/03_korean_ner_datasets)
4. [Pre-trained NER models for Korean corpus](./examples/04_korean_ner_models)
5. [Post-processing for the pre-trained NER models](./examples/05_postprocessing)