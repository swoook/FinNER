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
## 1
## 예컨대 유대치는 이동인의 소개를 받아 직접 오촌의 원산 포교당으로 찾아갔다.
## 예컨대 <유대치:PER>는 <이동인:PER>의 소개를 받아 직접 <오촌:LOC>의 <원산 포교당:LOC>으로 찾아갔다.
예컨대	예컨데	MAG	O
_	_	_	O
유대치	유대치	NNP	B-PER
는	는	JX	O
_	_	_	O
이동인	이동인	NNP	B-PER
의	의	JKG	O
_	_	_	O
소개	소개	NNG	O
를	를	JKO	O
_	_	_	O
받	받	VV	O
아	아	EC	O
_	_	_	O
직접	직접	MAG	O
_	_	_	O
오촌	오촌	NNG	B-LOC
의	의	JKG	O
_	_	_	O
원산	원산	NNP	B-LOC
_	_	_	I-LOC
포교당	포교당	NNG	I-LOC
으로	으로	JKB	O
_	_	_	O
찾아갔	찾아가+았	VV+EP	O
다	다	EF	O
.	.	SF	O
```

## References

1. https://nanum.etri.re.kr/share/aiacademy/nerdatasets?lang=ko_KR