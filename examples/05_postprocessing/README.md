# Post-processing

## Morpheme analysis

- The NER models from the monologg/KoELECTRA are trained on the NAVER x Changwon NER
- Recall that the NAVER x Changwon NER doesn't exclude 조사 (postposition) from the tags:
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

- `의` is postposition, but it's included in the tag `예산결산특별위원회의	ORG_B`
- So the models generally include postposition in named entities
- we need to check whether a postposition exists in named entities and remove it if we use monologg/KoELECTRA models fine-tuned on the NAVER x Changwon NER
- We can address this issue by applying morpheme analysis on the named entities
- One of the most famous korean morpheme analysis packages is **mecab-ko**
- However, we need to create a user dictionary and add it into the mecab-ko to make it recognize the company names as proper names
- Main challenge of this process is adjusting a priority of each company name
- Because the priorities are highly related to solving ambiguity of vocabulary