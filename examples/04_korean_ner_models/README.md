# Pre-trained NER models for Korean corpus

## Overview

| model | trained on |
| --- | --- |
| [monologg/KoELECTRA (GitHub)](https://github.com/monologg/KoELECTRA) | Naver NER |
| [toriving/naver-nlp-challenge-2018 (GitHub)](https://github.com/toriving/naver-nlp-challenge-2018) | Naver NER |
| [eagle705/pytorch-bert-crf-ner (GitHub)](https://github.com/eagle705/pytorch-bert-crf-ner) | kmounlp NER |
| [monologg/KoBERT-NER (GitHub)](https://github.com/monologg/KoBERT-NER) | Naver NER |
| [monologg/HanBert-Transformers (GitHub)](https://github.com/monologg/HanBert-Transformers) | Naver NER |
| [monologg/DistilKoBERT (GitHub)](https://github.com/monologg/DistilKoBERT) | Naver NER |

## monologg/KoELECTRA

1. [monologg/KoELECTRA-Pipeline (GitHub)](https://github.com/monologg/KoELECTRA-Pipeline)
    - monologg/KoELECTRA-Pipeline (GitHub) supports NER pipeline for the monologg/KoELECTRA
    - However, it's not available in transformers latest version (See the Requirements)
    - Specifically, [`KoELECTRA-Pipeline.ner_pipeline.NerPipeline`](https://github.com/monologg/KoELECTRA-Pipeline/blob/65f465419d0fffcac2c8df709dc57bf671dc39cd/ner_pipeline.py#L110) is not available in transformers latest version
    - Confirmed it works in `transformers==3.3.1`

2. [monologg/koelectra-base-v3-naver-ner](https://huggingface.co/monologg/koelectra-base-v3-naver-ner)
    - `transformers==3.3.1` can't find [monologg/koelectra-small-finetuned-naver-ner](https://huggingface.co/monologg/koelectra-base-v3-naver-ner), so I cloned it directly

3. Labels
    - Recall that NAVER x Changwon NER represents named entity belonging to a noun phrase by using `B` and `I`:
        ```
        - Some named entities belong to noun phrases
        - E.g., `월드컵 결승전 EVT`
        - NAVER x Changwon NER represents them by using `B` and `I`
        - E.g., 월드컵 결승전 → `월드컵 EVT_B` and `결승전 EVT_I`
        ```
    - Then, how the monologg/KoELECTRA respresents the labels of their tokens?
    - It Uses the original label id for the first token of the word, and padding ids for the remaining tokens
    - Refer to [here](https://github.com/monologg/KoELECTRA/blob/024fbdd600e653b6e4bdfc64ceec84181b5ce6c4/finetune/processor/ner.py#L82) for more details
    
4. Elapsed time
    | model | elapsed time (ms) |
    | --- | --- |
    | monologg/koelectra-small-finetuned-naver-ner | 21.6 |
    | monologg/koelectra-base-v3-naver-ner | 23.3 |

    - I measured the elapsed times of NER pipeline (NOT model) on NVIDIA TITAN RTX
    - They are not significantly different