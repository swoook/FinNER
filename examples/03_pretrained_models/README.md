# Pre-trained models

## Overview

| model | trained on |
| --- | --- |
| [monologg/KoELECTRA (GitHub)](https://github.com/monologg/KoELECTRA) | Naver NER |
| [toriving/naver-nlp-challenge-2018 (GitHub)](https://github.com/toriving/naver-nlp-challenge-2018) | Naver NER |
| [eagle705/pytorch-bert-crf-ner (GitHub)](https://github.com/eagle705/pytorch-bert-crf-ner) | kmounlp NER |
| [monologg/KoBERT-NER (GitHub)](https://github.com/monologg/KoBERT-NER) | Naver NER |
| [monologg/HanBert-Transformers (GitHub)](https://github.com/monologg/HanBert-Transformers) | Naver NER |
| [monologg/DistilKoBERT (GitHub)](https://github.com/monologg/DistilKoBERT) | Naver NER |


| Dataset | #sentences | #tags | 조사 in tag |
| --- | --- | --- | --- |
| kmounlp NER | 23964 | 10 | No |
| Naver NER | 82393 | 14 | Yes |

## Datasets

- The Naver NER doesn't exclude 조사 (postposition) from the tags
- E.g.,

``` txt
1	그런	-
2	예산결산특별위원회의	ORG_B
3	의도는	-
4	요즘	-
5	6연승을	NUM_B
6	첫부분으로	-
7	맞아	-
8	떨어져가고	-
9	있다	-
10	.	-
```

- On the other hand, the kmounlp NER excludes 조사 from the tags
- E.g.,

``` txt
1	그런	-
2	예산결산특별위원회의	ORG_B
3	의도는	-
4	요즘	-
5	6연승을	NUM_B
6	첫부분으로	-
7	맞아	-
8	떨어져가고	-
9	있다	-
10	.	-
```

## References

1. https://nanum.etri.re.kr/share/aiacademy/nerdatasets?lang=ko_KR