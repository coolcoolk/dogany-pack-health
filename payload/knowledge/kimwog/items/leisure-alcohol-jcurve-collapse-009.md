---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (leisure domain opening).
# The owner's 취미 area explicitly includes 술, so the domain must be able to
# speak about alcohol. This is the item where the evidence base moved most in
# the last decade, and it is carried at the CURRENT state, not the 2015 one.
# Lane: @drinking-epidemiology (VC-B).
id: leisure/alcohol-jcurve-collapse-009
domain: leisure
grade: "B (that the protective association of low-volume drinking with all-cause mortality does not survive correction for abstainer/former-drinker bias and study quality); B (that genetic-instrument evidence in East Asian and UK cohorts shows no protective threshold for blood pressure, stroke or coronary artery disease); C (any exact intake threshold, which differs by sex, endpoint and cohort)"
lane: "@drinking-epidemiology"
locale: universal
as_of: 2019-2023
contested: yes
sources:
  - "Zhao, J., Stockwell, T., Naimi, T., Churchill, S., Clay, J. and Sherk, A. (2023). Association Between Daily Alcohol Intake and Risk of All-Cause Mortality: A Systematic Review and Meta-analyses. JAMA Network Open 6(3), e236185. https://doi.org/10.1001/jamanetworkopen.2023.6185"
  - "Millwood, I. Y., Walters, R. G., Mei, X. W., Guo, Y., Yang, L., Bian, Z., et al. (2019). Conventional and genetic evidence on alcohol and vascular disease aetiology: a prospective study of 500 000 men and women in China. The Lancet 393(10183), 1831-1842. https://doi.org/10.1016/S0140-6736(18)31772-0"
  - "Biddinger, K. J., Emdin, C. A., Haas, M. E., Wang, M., Hindy, G., Ellinor, P. T., et al. (2022). Association of Habitual Alcohol Intake With Risk of Cardiovascular Disease. JAMA Network Open 5(3), e223849. https://doi.org/10.1001/jamanetworkopen.2022.3849"
  - "Stockley, C. S., Hendriks, H. F. J. and Ellison, R. C. (2024). ISFAR Reiterates Its Defense of Moderate Alcohol Consumption's Health Benefits. Journal of Studies on Alcohol and Drugs 85(1), 136-140. https://doi.org/10.15288/jsad.23-00293"
  - "exercise/funding-coi-check-004"
  - "framework:GRADE -- three independent lines converge: a 107-study meta-analysis with explicit bias adjustment, and two Mendelian randomisation analyses in cohorts of 512715 and 371463 people. Mendelian randomisation is the strongest available design here because genotype is fixed at conception and cannot be caused by illness or lifestyle. Held at the observational band rather than higher because MR carries its own assumptions and the meta-analysis has a published industry-funded dissent."
applicability:
  axes:
    - key: sex
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: pregnancy_status
      type: categorical
      role: hard
      unknown_policy: block_specifics
      gate:
        allowed: [not_pregnant, none]
    - key: medication_list
      type: categorical
      role: hard
      unknown_policy: block_specifics
    - key: cardiovascular_condition
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      What the meta-analysis found, stated exactly. 107 cohort studies published
      1980 to July 2021, 724 risk estimates, 4838825 participants, 425564
      deaths. In models adjusting for sampling variation, former-drinker bias and
      other prespecified study-quality criteria: occasional drinkers (>0 to <1.3
      g ethanol/day) relative risk 0.96 (95 percent CI 0.86-1.06, p = .41) and
      low-volume drinkers (1.3-24.0 g/day) RR 0.93 (p = .07) versus lifetime
      nondrinkers -- neither significant. Risk was significantly elevated at 45-64
      g/day (RR 1.19) and 65+ g/day (RR 1.35), both p < .001, with 25-44 g/day
      non-significantly elevated (RR 1.05). Female drinkers showed significantly
      higher risk versus female lifetime nondrinkers (RR 1.22, p = .03).
    grade: B
  - note: >
      Why the old J-curve appeared, mechanically. The comparison group in the
      classic studies was "non-drinkers", which mixes lifetime abstainers with
      people who STOPPED drinking, often because they became ill. Sick quitters
      raise the mortality of the reference group, which manufactures an apparent
      benefit for moderate drinkers out of nothing. Correcting for former-drinker
      bias is what removes the curve. This is a study-design artefact with a
      name, not a disagreement between findings.
    grade: B
  - note: >
      The genetic evidence, which is why this is not merely another cohort
      squabble. In 512715 Chinese adults with 161498 genotyped for ALDH2-rs671
      and ADH1B-rs1229984, self-reported intake showed the familiar U-shaped
      associations with ischaemic stroke, intracerebral haemorrhage and
      myocardial infarction -- but genotype-predicted intake, which cannot be
      caused by illness, showed NO U-shape. Instead it showed a continuously
      positive log-linear association with stroke (RR per 280 g/week 1.58, 95
      percent CI 1.36-1.84 for intracerebral haemorrhage; 1.27, 1.13-1.43 for
      ischaemic stroke) and no significant association with myocardial
      infarction (0.96, 0.78-1.18). The authors' interpretation: the apparently
      protective effects of moderate intake against stroke are largely
      non-causal.
    grade: B
  - note: >
      The second genetic analysis, in a Western cohort, agrees and adds shape.
      In 371463 UK Biobank participants, light-to-moderate drinking was
      associated with healthier lifestyle factors, adjustment for which
      attenuated the apparent cardioprotection. Linear Mendelian randomisation
      gave 1.3-fold higher hypertension risk and 1.4-fold higher coronary artery
      disease risk per SD of genetically predicted intake; nonlinear analysis
      showed minimal increases at light intake and EXPONENTIAL increases at
      heavier intake, including within amounts accepted by current national
      guidelines.
    grade: B
  - note: >
      The exponential shape is the practically important part and it cuts BOTH
      ways. It means the difference between light and moderate drinking is small
      in absolute risk, and the difference between moderate and heavy is not.
      An honest statement is therefore not "any amount is dangerous" -- it is
      that risk starts near zero and accelerates, so where a person sits on the
      curve matters far more than whether they are on it.
    grade: C
  - note: >
      THE CONTESTED FLAG IS EARNED AND SO IS ITS DISCOUNT. A defence of moderate
      drinking's benefits was published in reply to the 2023 meta-analysis
      (Stockley, Hendriks and Ellison, 2024). It is a genuine peer-reviewed
      comment and the disagreement is live. It is also authored by the
      International Scientific Forum on Alcohol Research, and the published
      conflict-of-interest statement discloses extensive past funding and
      consultancy from wine, brewing and spirits interests. Both facts are
      carried together, per exercise/funding-coi-check-004: the objection is
      recorded, and so is who is making it.
    grade: C
  - note: >
      DO NOT MORALISE. Nothing above is an instruction about how anyone should
      live. It is a correction to a specific empirical claim -- that moderate
      drinking is good for you -- which was widely believed, is not supported,
      and is still repeated. Someone who drinks socially and knows this is
      making an informed choice, which is the whole objective.
    grade: B
claim: >
  The moderate-drinking health benefit did not survive better methods, and the
  current state of the evidence is not the 2015 consensus. Zhao et al. (2023)
  meta-analysed 107 cohort studies (4838825 participants, 425564 deaths) and,
  after adjusting for sampling variation and former-drinker bias, found no
  significant mortality reduction for occasional drinkers (RR 0.96, 95 percent CI
  0.86-1.06) or low-volume drinkers at 1.3-24.0 g ethanol/day (RR 0.93, p = .07)
  versus lifetime nondrinkers, with significantly raised risk from 45 g/day
  upward and a significantly raised risk among female drinkers overall (RR 1.22).
  The mechanism that produced the old J-curve is identified: the reference group
  in classic studies mixed lifetime abstainers with people who had quit, often
  because they were already ill. Two Mendelian randomisation analyses -- 512715
  adults in China using ALDH2 and ADH1B variants, and 371463 UK Biobank
  participants -- both remove the U-shape when genotype rather than self-report
  predicts intake, showing instead a log-linear increase in stroke risk (RR per
  280 g/week 1.58 for intracerebral haemorrhage, 1.27 for ischaemic stroke), no
  significant effect on myocardial infarction, and exponential increases in
  hypertension and coronary artery disease at heavier intake including within
  currently permitted guideline amounts. The dispute is live: a defence of
  moderate drinking's benefits was published in reply (Stockley et al., 2024) by
  authors whose disclosed funding history is extensively alcohol-industry linked,
  and both the objection and its provenance are carried. Two things this item
  does NOT say: it does not put a single safe threshold on the table, because
  thresholds differ by sex, endpoint and cohort; and it does not moralise. The
  shape is what matters -- risk starts near zero and accelerates, so where
  someone sits on the curve matters far more than whether they are on it.
reasoning: >
  Alcohol is the part of this domain where the evidence moved most in the last
  decade and where a warehouse built on older sources would be actively wrong, so
  the item is constructed around the reason the old answer was wrong rather than
  around the new number. Former-drinker bias is a named, mechanical study-design
  artefact, and explaining it is what makes the correction stick; a reader who
  understands why the reference group was contaminated does not need to trust
  the meta-analysis on authority. Mendelian randomisation is given equal weight
  because it answers the objection the meta-analysis cannot -- that moderate
  drinkers might simply be healthier people -- since genotype is fixed at
  conception and cannot be caused by illness, wealth or lifestyle. That two MR
  analyses in populations as different as rural China and the UK Biobank agree is
  the strongest fact in the item. It is held at the observational band rather than
  higher for two disclosed reasons: MR has its own assumptions, and there is a
  published dissent. That dissent is carried rather than suppressed, because
  suppressing a peer-reviewed objection is how a warehouse becomes propaganda,
  and its funding disclosure is carried alongside for exactly the same reason.
  The no-moralising instruction is written into the item because the failure mode
  here is not getting the epidemiology wrong, it is delivering it as a verdict on
  somebody's evening; the owner's own taxonomy files 술 under 취미, and an agent
  that treats a hobby as a health violation has misread the person it works for.
---

# leisure/alcohol-jcurve-collapse-009

The finding that a drink or two a day is good for you is one of the best-known
health facts of the last thirty years, and it is not holding up.

Start with why it looked true. In the classic studies, moderate drinkers were
compared against "non-drinkers" -- and that group quietly contained two very
different populations. People who never drank, and people who had stopped. A lot
of people stop drinking because they have become ill. Put the sick quitters in
the comparison group and its mortality goes up, which makes everyone else look
protected. The benefit was, to a large extent, an artefact of who was standing on
the other side of the comparison.

When a 2023 meta-analysis of a hundred and seven cohort studies -- nearly five
million people, over four hundred thousand deaths -- adjusted for that
contamination and for study quality, the protective effect went away. Occasional
drinking: no significant difference. Low-volume drinking, up to about two
standard drinks a day: no significant difference. Risk rose clearly from around
three drinks a day upward, and women showed elevated risk overall relative to
women who had never drunk.

Then there is the evidence that settles the "but moderate drinkers are just
healthier people" objection, and it is the strongest thing in this item. Some
people carry gene variants that make drinking physically unpleasant, and those
variants are assigned at conception -- they cannot be caused by illness, income
or lifestyle. Using them as the measure of how much someone drinks, in half a
million adults in China, the U-shape vanishes. What is left is a straight
upward line for stroke, steeper for bleeding strokes than for clot strokes, and
no detectable effect either way on heart attacks. A separate analysis of three
hundred and seventy thousand UK Biobank participants found the same collapse of
the apparent benefit, plus the shape of what remains: risk barely moves at light
intake and then climbs exponentially -- including inside amounts that current
national guidelines still permit.

That shape is the useful part, and it cuts in both directions. It does not say
that any amount is dangerous. It says the distance between light and moderate is
small and the distance between moderate and heavy is not. Where someone sits on
the curve matters far more than whether they are on it at all.

The argument is not over. A defence of moderate drinking's benefits was published
in reply to the 2023 meta-analysis in a peer-reviewed journal, and it deserves to
be recorded rather than ignored. So does the fact that its authors' disclosed
funding history runs extensively through the wine, brewing and spirits
industries. Both go in the file together.

Last, and it matters more than any of the numbers: none of this is a verdict on
anybody's evening. It is a correction to a specific claim that a lot of people
believe and that turns out not to be true. Someone who drinks with friends and
knows what the evidence actually says is making an informed choice, and that was
the entire objective.
