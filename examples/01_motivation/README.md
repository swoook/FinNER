# Motivation

- There is a non-negligible number of homonyms in financial named entities such as company names
- Assume we simply check if specific patterns like financial named entities are contained within a corpus
- Then we are likely to find a significant number of false positives by homonyms. 

## Example: Company names

### Proportion

![Figure 1: Proportions of company names which are homonymous or non-homonymous](./imgs/figure_01.png)

- E.g., 6.3% of the Korean company names are homonymous
- I retreived a list of the company names by using [josw123/dart-fss (GitHub)](https://github.com/josw123/dart-fss)

### Length

![Figure 2: A distribution of lengths of the homonymous company names](./imgs/figure_02.png)

- Most of the homonymous company names are between 2 and 4 in length

![Figure 3: A distribution of lengths of the non-homonymous company names](./imgs/figure_03.png)

- On the other hand, the non-homonymous company names have quite different characteristic

### `품사` (Part-Of-Speech, POS)

![Figure 4: A distribution of `품사` (Part-Of-Speech, POS) of the homonymous company names](./imgs/figure_04.png)

- Of course, most of the homonyms are NNP or NNG (almost 90%)

### `소스` (source `.csv` in which the vocabulary exists)

![Figure 5: A distribution of `품사` (Part-Of-Speech, POS) of the homonymous company names](./imgs/figure_05.png)

