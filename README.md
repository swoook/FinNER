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