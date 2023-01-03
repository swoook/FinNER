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
    - However, it's not available on transformers latest version (See the Requirements)
    - Specifically, [`KoELECTRA-Pipeline.ner_pipeline.NerPipeline`](https://github.com/monologg/KoELECTRA-Pipeline/blob/65f465419d0fffcac2c8df709dc57bf671dc39cd/ner_pipeline.py#L110) is not available on transformers latest version
    - Confirmed it works on `transformers==3.3.1`

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
    - It uses the original label id for the first token of the word, and padding ids for the remaining tokens
    - Refer to [here](https://github.com/monologg/KoELECTRA/blob/024fbdd600e653b6e4bdfc64ceec84181b5ce6c4/finetune/processor/ner.py#L82) for more details
    
4. Elapsed time
    | model | elapsed time (ms) |
    | --- | --- |
    | monologg/koelectra-small-finetuned-naver-ner | 21.6 |
    | monologg/koelectra-base-v3-naver-ner | 23.3 |

    - I measured the elapsed times of NER pipeline (NOT model) on NVIDIA TITAN RTX
    - They are not significantly different
    - TODO: Does pre/post-processing time overwhelm inference time?
    
5. Sample

    | monologg/koelectra-small-finetuned-naver-ner  | monologg/koelectra-base-v3-naver-ner |
    | --- | --- |
    | [{'entity': 'ORG-B', 'score': 0.9981120824813843, 'word': '애플'},<br />{'entity': 'TRM-B', 'score': 0.9973036646842957, 'word': '아이폰14'},<br />{'entity': 'O', 'score': 0.8423691987991333, 'word': '프로'},<br />{'entity': 'O', 'score': 0.9999445676803589, 'word': '생산'},<br />{'entity': 'O', 'score': 0.9998543858528137, 'word': '속도'},<br />{'entity': 'O', 'score': 0.9992532730102539, 'word': '회복'},<br />{'entity': 'O', 'score': 0.999006450176239, 'word': '중…"생산'},<br />{'entity': 'O', 'score': 0.9994794130325317, 'word': '능력'},<br />{'entity': 'NUM-B', 'score': 0.9899680018424988, 'word': '70%로'},<br />{'entity': 'O', 'score': 0.9998534917831421, 'word': '회복"'}] | [{'entity': 'ORG-B', 'score': 0.9999739527702332, 'word': '애플'},<br />{'entity': 'TRM-B', 'score': 0.9998205900192261, 'word': '아이폰14'},<br />{'entity': 'TRM-I', 'score': 0.9996592998504639, 'word': '프로'},<br />{'entity': 'O', 'score': 0.999998927116394, 'word': '생산'},<br />{'entity': 'O', 'score': 0.9999986290931702, 'word': '속도'},<br />{'entity': 'O', 'score': 0.9999985098838806, 'word': '회복'},<br />{'entity': 'O', 'score': 0.9998188018798828, 'word': '중…"생산'},<br />{'entity': 'O', 'score': 0.9999990463256836, 'word': '능력'},<br />{'entity': 'O', 'score': 0.5029545426368713, 'word': '70%로'},<br />{'entity': 'O', 'score': 0.9999988079071045, 'word': '회복"'}] |
    | [{'entity': 'ORG-B', 'score': 0.9995225667953491, 'word': '모건스탠리'},<br />{'entity': 'LOC-B', 'score': 0.9457388520240784, 'word': '"테슬라,'},<br />{'entity': 'LOC-B', 'score': 0.8066743612289429, 'word': 'EV'},<br />{'entity': 'O', 'score': 0.9996775984764099, 'word': '시장서'},<br />{'entity': 'O', 'score': 0.9999493956565857, 'word': '격차'},<br />{'entity': 'O', 'score': 0.9990318417549133, 'word': '벌릴'},<br />{'entity': 'O', 'score': 0.9764936566352844, 'word': '것"…테슬라'},<br />{'entity': 'O', 'score': 0.9995763897895813, 'word': '주가'},<br />{'entity': 'NUM-B', 'score': 0.9981926083564758, 'word': '8%'},<br />{'entity': 'O', 'score': 0.5355684161186218, 'word': '이상'},<br />{'entity': 'O', 'score': 0.9906592965126038, 'word': '상승'},<br />{'entity': 'O', 'score': 0.9990622997283936, 'word': '반전'}] | [{'entity': 'ORG-B', 'score': 0.9999749660491943, 'word': '모건스탠리'},<br />{'entity': 'ORG-B', 'score': 0.9999773502349854, 'word': '"테슬라,'},<br />{'entity': 'TRM-B', 'score': 0.9999140501022339, 'word': 'EV'},<br />{'entity': 'O', 'score': 0.9999972581863403, 'word': '시장서'},<br />{'entity': 'O', 'score': 0.9999962449073792, 'word': '격차'},<br />{'entity': 'ORG-B', 'score': 0.9999645352363586, 'word': '벌릴'},<br />{'entity': 'ORG-B', 'score': 0.9997900128364563, 'word': '것"…테슬라'},<br />{'entity': 'O', 'score': 0.9999978542327881, 'word': '주가'},<br />{'entity': 'NUM-B', 'score': 0.999990701675415, 'word': '8%'},<br />{'entity': 'O', 'score': 0.999993622303009, 'word': '이상'},<br />{'entity': 'O', 'score': 0.9999980330467224, 'word': '상승'},<br />{'entity': 'O', 'score': 0.9999988079071045, 'word': '반전'}] |
    | [{'entity': 'ORG-B', 'score': 0.9976840615272522, 'word': 'GE'},<br />{'entity': 'CVL-B', 'score': 0.9095185399055481, 'word': '헬스케어,'},<br />{'entity': 'DAT-B', 'score': 0.999757707118988, 'word': '1월'},<br />{'entity': 'DAT-I', 'score': 0.9994773864746094, 'word': '4일부터'},<br />{'entity': 'O', 'score': 0.9999690651893616, 'word': '별도'},<br />{'entity': 'O', 'score': 0.9999524354934692, 'word': '주식으로'},<br />{'entity': 'O', 'score': 0.999963641166687, 'word': '거래'}] | [{'entity': 'ORG-B', 'score': 0.9999684691429138, 'word': 'GE'},<br />{'entity': 'ORG-I', 'score': 0.9996752142906189, 'word': '헬스케어,'},<br />{'entity': 'DAT-B', 'score': 0.9999707937240601, 'word': '1월'},<br />{'entity': 'DAT-I', 'score': 0.999958336353302, 'word': '4일부터'},<br />{'entity': 'O', 'score': 0.9999973177909851, 'word': '별도'},<br />{'entity': 'O', 'score': 0.9999961853027344, 'word': '주식으로'},<br />{'entity': 'O', 'score': 0.9999985694885254, 'word': '거래'}] |
    | [{'entity': 'PER-B', 'score': 0.9979043006896973, 'word': '머스크'},<br />{'entity': 'DAT-B', 'score': 0.9984976053237915, 'word': '"연말까지'},<br />{'entity': 'LOC-B', 'score': 0.9663654565811157, 'word': '테슬라'},<br />{'entity': 'O', 'score': 0.5941041111946106, 'word': '배송'},<br />{'entity': 'CVL-B', 'score': 0.5018539428710938, 'word': '도와달라"'},<br />{'entity': 'CVL-B', 'score': 0.9628623723983765, 'word': '직원에'},<br />{'entity': 'TRM-B', 'score': 0.8786627054214478, 'word': '이메일'}] | [{'entity': 'PER-B', 'score': 0.9999598860740662, 'word': '머스크'},<br />{'entity': 'DAT-B', 'score': 0.9998950958251953, 'word': '"연말까지'},<br />{'entity': 'ORG-B', 'score': 0.9999812245368958, 'word': '테슬라'},<br />{'entity': 'O', 'score': 0.9999945163726807, 'word': '배송'},<br />{'entity': 'O', 'score': 0.9999900460243225, 'word': '도와달라"'},<br />{'entity': 'CVL-B', 'score': 0.9999874234199524, 'word': '직원에'},<br />{'entity': 'TRM-B', 'score': 0.9949198365211487, 'word': '이메일'}] |
    | [{'entity': 'ORG-B', 'score': 0.9994351863861084, 'word': '삼성'},<br />{'entity': 'O', 'score': 0.8921143412590027, 'word': '‘더'},<br />{'entity': 'O', 'score': 0.9925846457481384, 'word': '프레임’으로'},<br />{'entity': 'O', 'score': 0.9982132911682129, 'word': '모나리자'},<br />{'entity': 'O', 'score': 0.9982662796974182, 'word': '감상'}] | [{'entity': 'ORG-B', 'score': 0.9999852776527405, 'word': '삼성'},<br />{'entity': 'TRM-B', 'score': 0.5907562375068665, 'word': '‘더'},<br />{'entity': 'TRM-I', 'score': 0.7688044905662537, 'word': '프레임’으로'},<br />{'entity': 'PER-B', 'score': 0.9969599843025208, 'word': '모나리자'},<br />{'entity': 'O', 'score': 0.9998710751533508, 'word': '감상'}] |
    | [{'entity': 'PER-B', 'score': 0.9986163377761841, 'word': '모나리자,'},<br />{'entity': 'O', 'score': 0.727386474609375, 'word': '‘알쏭달쏭'},<br />{'entity': 'O', 'score': 0.9996838569641113, 'word': '캐치!'},<br />{'entity': 'PER-B', 'score': 0.9948994517326355, 'word': '티니핑’'},<br />{'entity': 'O', 'score': 0.9993060231208801, 'word': '캐릭터'},<br />{'entity': 'O', 'score': 0.9952626824378967, 'word': '콜라보'},<br />{'entity': 'O', 'score': 0.625251829624176, 'word': '미용티슈·물티슈'},<br />{'entity': 'O', 'score': 0.999923586845398, 'word': '선봬'}] | [{'entity': 'PER-B', 'score': 0.9999591112136841, 'word': '모나리자,'},<br />{'entity': 'O', 'score': 0.9979546666145325, 'word': '‘알쏭달쏭'},<br />{'entity': 'O', 'score': 0.8788185715675354, 'word': '캐치!'},<br />{'entity': 'PER-B', 'score': 0.8239721059799194, 'word': '티니핑’'},<br />{'entity': 'O', 'score': 0.9997508525848389, 'word': '캐릭터'},<br />{'entity': 'O', 'score': 0.9999932050704956, 'word': '콜라보'},<br />{'entity': 'O', 'score': 0.9397523403167725, 'word': '미용티슈·물티슈'},<br />{'entity': 'O', 'score': 0.9999947547912598, 'word': '선봬'}] |
    | [{'entity': 'O', 'score': 0.7511236071586609, 'word': '"반토막"'},<br />{'entity': 'ORG-B', 'score': 0.9995559453964233, 'word': '마이크론'},<br />{'entity': 'O', 'score': 0.8277828693389893, 'word': '주가…아거스'},<br />{'entity': 'O', 'score': 0.9992302060127258, 'word': '"매수할'},<br />{'entity': 'O', 'score': 0.9999534487724304, 'word': '타이밍'},<br />{'entity': 'O', 'score': 0.9999535083770752, 'word': '아니다"'}] | [{'entity': 'O', 'score': 0.9579496383666992, 'word': '"반토막"'},<br />{'entity': 'ORG-B', 'score': 0.9999145269393921, 'word': '마이크론'},<br />{'entity': 'O', 'score': 0.8285893201828003, 'word': '주가…아거스'},<br />{'entity': 'O', 'score': 0.9999950528144836, 'word': '"매수할'},<br />{'entity': 'O', 'score': 0.999996542930603, 'word': '타이밍'},<br />{'entity': 'O', 'score': 0.9999969005584717, 'word': '아니다"'}] |

