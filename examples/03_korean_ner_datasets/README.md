# NER datasets for Korean corpus

## Datasets

| Dataset | #sentences | #tags | 조사 in tag |
| --- | --- | --- | --- |
| [kmounlp NER](https://github.com/kmounlp/NER) | 23964 | 10 | No |
| [NAVER x Changwon NER](http://air.changwon.ac.kr/?page_id=10) | 82393 | 14 | Yes |
| [전문분야 말뭉치](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=110) | >=1.5M | 15 | No |
| [국립국어원 개체명 분석 말뭉치 개체 연결 2021](https://corpus.korean.go.kr/) | --- | 15(150) | No |

## Tags

| kmounlp NER | NAVER x Changwon NER | 전문분야 말뭉치 |
| --- | --- | --- |
| PER | PER | PS |
| ORG | ORG | OG |
| LOC | LOC | LC |
| POH | DAT | DT |
| DAT | TIM | TI |
| TIM | FLD | TR |
| DUR | AFW | FD |
| MNY | CVL | AF |
| PNT | NUM | CV |
| NOH | EVT | QT |
|  | ANM | EV |
|  | PLT | AM |
|  | MAT | PT |
|  | TRM | MT |
|  |  | TM |

- Refer to the links below for more details:
1. [NER Guideline (ver 1.0).pdf, pp.2-9 in kmounlp NER (GitHub)](https://github.com/kmounlp/NER/blob/1e557de738b8e6215c7cacac116e735518c0f680/NER%20Guideline%20(ver%201.0).pdf)
2. [개체명인식 with Naver &#8211; 창원대 적응지능연구실](http://air.changwon.ac.kr/?page_id=10)
3. [전문분야 말뭉치 설명서](https://aihub.or.kr/file/down.do?fileSn=7995&dataMnlFileSn=7995&dataSetSn=110)

## Postposition

- The NAVER x Changwon NER doesn't exclude 조사 (postposition) from the tags
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

- On the other hand, the kmounlp NER and 전문분야 말뭉치 excludes 조사 from the tags
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

## Noun phrases

- Some named entities belong to noun phrases
- E.g., `월드컵 결승전 EVT`
- NAVER x Changwon NER represents them by using `B` and `I`
- E.g., 월드컵 결승전 → `월드컵 EVT_B` and `결승전 EVT_I`

## Korpora

- [Korpora](https://ko-nlp.github.io/Korpora/) is a Python package which supports features to download and pre-process some open source Korean corpus datasets
- It also supports the NAVER x Changwon NER