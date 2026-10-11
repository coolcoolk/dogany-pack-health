---
# Shopping / decision sprint 2026-10-07 (dispatch task kw-sh-product-choice-overload).
# de Langhe 2016 and Powell 2017 abstracts read at the publisher / PubMed;
# Luca and Zervas read in the authors' accepted-manuscript PDF; Hu, Zhang and
# Pavlou 2009 read at indexed abstract text only (CACM returned 403). The KR
# disclosure rule was read via press reports of the KFTC announcement, not
# the guideline text itself -- see the note on it.
id: spending-saving/star-rating-weak-quality-signal-031
domain: spending-saving
grade: C (large observational datasets and one experiment; US platforms, mostly pre-2015 data)
lane: "@household-behavioral"
locale: universal
as_of: 2009-2017 (KR disclosure rule 2020-09-01)
contested: no
sources:
  - "de Langhe, B., Fernbach, P. M. and Lichtenstein, D. R. (2016). Navigating by the Stars: Investigating the Actual and Perceived Validity of Online User Ratings. Journal of Consumer Research 42(6), 817-833. https://doi.org/10.1093/jcr/ucv047 -- 1,272 products in 120 vertically differentiated categories: average user ratings lack convergence with Consumer Reports scores, are often based on insufficient sample sizes, do not predict resale prices, and are higher for expensive products and premium brands controlling for Consumer Reports; consumers nonetheless weight the average heavily and do not adjust for sample size (abstract read)."
  - "Hu, N., Zhang, J. and Pavlou, P. A. (2009). Overcoming the J-shaped Distribution of Product Reviews. Communications of the ACM 52(10), 144-147. https://doi.org/10.1145/1562764.1562800 -- online ratings are J-shaped (mostly 5, some 1, few between) because of purchasing bias (those who expect to like it buy) and under-reporting bias (the very satisfied and very dissatisfied write); the mean is therefore a biased estimator of quality (indexed abstract read; full text 403)."
  - "Luca, M. and Zervas, G. (2016). Fake It Till You Make It: Reputation, Competition, and Yelp Review Fraud. Management Science 62(12), 3412-3427. https://doi.org/10.1287/mnsc.2015.2304 -- roughly 16 percent of Boston restaurant reviews on Yelp were filtered as suspicious; filtered reviews are more extreme; fraud is more likely when reputation is weak (few or recently bad reviews) and less likely for chains (accepted manuscript read)."
  - "Powell, D., Yu, J., DeWolf, M. and Holyoak, K. J. (2017). The Love of Large Numbers: A Popularity Bias in Consumer Choice. Psychological Science 28(10), 1432-1442. https://doi.org/10.1177/0956797617711291 -- against a statistical model built on Amazon review priors, participants under some conditions preferred the product with more reviews even when the model said the one with fewer was likely better; their judgements did not reflect meaningful statistical inference (PubMed abstract read)."
  - "공정거래위원회 (2020). 추천·보증 등에 관한 표시·광고 심사지침 개정, 2020-09-01 시행 -- 금전·할인·협찬 등 경제적 이해관계가 있는 추천·후기는 그 사실을 소비자가 알기 쉽게 표시해야 함 (read via press reports of the KFTC announcement, e.g. etoday.co.kr/news/view/1909454; guideline text not read)."
refraction_notes:
  - note: >
      THE CONSUMER REPORTS COMPARISON IS ONE BENCHMARK. Lab-tested scores
      measure performance on the tester's criteria, not satisfaction, fit or
      taste. The defensible reading is that the star average carries little of
      the information a lab test carries, not that it carries nothing.
    grade: C
  - note: >
      THE 16 PERCENT IS ONE PLATFORM'S FILTER IN ONE CITY. It is a proxy for
      fraud (Yelp's own classifier), on Boston restaurants. It is not a fake
      rate for Korean shopping platforms and is never quoted as one. What
      transfers is the pattern: fraud concentrates where reputation is thin.
    grade: C
  - note: >
      KR DISCLOSURE IS A RULE, NOT A GUARANTEE. The KFTC guideline requires
      paid or sponsored reviews to say so; it does not mean undisclosed ones
      are absent. The guideline text itself was not read in this pass, so only
      its announced principle is carried.
    grade: D
claim: >
  A product's average star rating is a weak and biased signal of its quality,
  and people over-trust it. Across 1,272 products in 120 categories, average
  user ratings did not converge with lab-tested quality scores, were often
  computed from too few ratings to be informative, did not predict resale
  value, and ran higher for expensive and premium-brand products at the same
  tested quality. Ratings pile up at 5 and 1 because buyers self-select and the
  extremes are the ones who write, so the mean is a biased estimate. A visible
  share of reviews can be fraudulent -- about 16 percent of one city's
  restaurant reviews on one platform were filtered -- and fraud concentrates
  where a business has few or recently bad reviews. People nonetheless lean on
  the average and on the review count, even preferring the more-reviewed
  product when the evidence favours the other. For a find-things skill:
  treat the star average as a tie-breaker inside a candidate set, not a quality
  ranking across it; discount small review counts; read the content of
  mid-range and negative reviews for the user's own axes; and treat a young or
  thin review profile with unusually extreme scores as a reason for caution,
  not confidence.
reasoning: >
  Graded in the observational band: the de Langhe dataset is large but its
  benchmark is one testing organisation, the J-shape work is partly analytical,
  the fraud estimate is a classifier proxy on one platform, and the popularity
  bias is one experiment. Together they agree in direction from four
  different angles -- validity, distribution, manipulation and consumer
  inference -- and that convergence is what the item carries. None of the
  numbers are Korean and none are transported; the KR row is the one legal
  fact available, carried at the band its reading supports. The operational
  content is a set of discounts the skill applies when it uses ratings to
  build or annotate a candidate set, and those are listed in the companion
  rules item.
---

# spending-saving/star-rating-weak-quality-signal-031 -- 별점은 약한 품질 신호다

**한 줄 그림:** 별점 평균은 품질을 잘 말해 주지 못하는데 사람들은 많이 믿는다. 후보 사이 동점 정리용으로
쓰고, 품질 순위로 쓰지 않는다.

Researchers lined up the average user rating of 1,272 products against lab
test scores for the same products. The two barely agreed. Averages were often
computed from too few ratings to mean much, they did not predict what the
product resold for, and pricier and premium-brand products got higher stars
than their tested quality earned. Shoppers still weighted the average more
than price or the number of ratings, and did not trust a small sample any
less.

Why the average is off: ratings bunch at 5 and 1, because people who expect to
like something are the ones who buy it, and people who loved or hated it are
the ones who write. The middle goes quiet.

Some of it is fake. On one platform in one city, about one restaurant review in
six was filtered as suspicious, the filtered ones were more extreme, and
businesses with few or recently bad reviews were the likeliest to fake. People
also prefer the product with more reviews even when the arithmetic says the
other is probably better.

In Korea, sponsored or paid reviews must say so under the KFTC's
endorsement-advertising guideline (in force 2020-09-01). That rule makes
disclosed ads visible; it does not remove undisclosed ones.

## Rating-use rule

| Situation | Do | Basis |
|---|---|---|
| ranking candidates across a set | do not rank by star average | de Langhe 2016 |
| two candidates otherwise close | star average may break the tie | weak signal, still a signal |
| review count small | say the average is uncertain; do not present it as a score | insufficient sample (de Langhe), Powell 2017 |
| need to judge fit | read 2-4 star review text for the user's own axes | J-shape: the middle carries the information |
| new listing, few reviews, mostly 5 or 1 | flag as low-confidence | Luca and Zervas 2016 pattern |
| KR review marked 협찬/광고/제공 | treat as advertising, not a user report | KFTC guideline |

## 한국어 요약 (답변용)

- 별점 평균은 실험실 품질 점수와 거의 맞지 않았다(1,272개 제품). 평가 수가 적은 경우가 많고, 중고
  가격도 예측하지 못하며, 비싸고 유명한 브랜드일수록 같은 품질에서도 별점이 높았다.
- 별점은 5점과 1점에 몰린다. 마음에 들 것 같은 사람이 사고, 아주 좋았거나 아주 싫었던 사람이 쓰기
  때문이다. 그래서 평균은 품질을 치우치게 보여 준다.
- 가짜 후기도 있다. 한 도시 한 플랫폼에서 식당 후기의 약 16%가 의심 후기로 걸러졌다. 후기가 적거나
  최근 평이 나쁜 곳에서 더 많았다. 이 숫자를 한국 쇼핑몰 가짜 후기 비율로 말하지 않는다.
- 사람들은 후기 수가 많은 쪽을 고르는 경향이 있다. 통계적으로는 후기가 적은 쪽이 더 나을 때도 그렇다.
- 별점은 후보끼리 비슷할 때 동점 정리에만 쓴다. 맞는지 판단할 때는 2~4점 후기 내용을 사용자 기준으로
  읽는다.
- 한국에서는 협찬·광고 후기는 그 사실을 표시해야 한다(공정위 추천·보증 심사지침, 2020-09-01 시행).
  표시된 후기는 광고로 본다. 다만 표시 안 된 광고가 없다는 뜻은 아니다.
