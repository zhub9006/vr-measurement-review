# ITC-SOPI Scoring Template
# Instrument: ITC Sense of Presence Inventory
# Lessiter, Freeman, Keogh & Davidoff (2001)
# 44 items, 5-point Likert scale (1=strongly disagree, 5=strongly agree)
# -------------------------------------------------------------------

## Overview of Subscales

| Subscale                | Abbrev | Items | Scale | Higher Score Means         |
|-------------------------|--------|-------|-------|----------------------------|
| Sense of Physical Space | SPS    | 13    | 1-5   | More spatial presence      |
| Engagement              | ENG    | 11    | 1-5   | More engaged / enjoyment   |
| Naturalness             | NAT    | 11    | 1-5   | More naturalistic/coherent |
| Negative Effects        | NE     | 9     | 1-5   | More adverse effects       |

## STEP 1: Administer items (consult original Lessiter et al. 2001 paper for full item list)

### Sense of Physical Space (SPS) — 13 items
Key item examples:
- "I had a strong sense of being in the environment shown."
- "I felt I was visiting the places shown."
- "I felt I could reach out and touch things in the presentation."
- "The sense of 'being there' was strong."
- "I felt my body was 'in' the environment shown."

### Engagement (ENG) — 11 items
Key item examples:
- "I was interested in what was going on."
- "I found the experience enjoyable."
- "I was involved in the presentation."
- "The experience was intense."
- "I enjoyed myself."

### Naturalness (NAT) — 11 items
Key item examples:
- "The way things moved was consistent with real-life expectations."
- "The environment seemed natural."
- "The objects looked like real objects."
- "The sounds seemed to come from the right places."

### Negative Effects (NE) — 9 items
Key item examples:
- "I felt dizzy."
- "I felt nauseous."
- "I felt disorientated."
- "My eyes felt strained."
- "I felt uncomfortable."

## STEP 2: Compute subscale means

```
SPS_score = mean(SPS_1 ... SPS_13)    [range 1.0-5.0]
ENG_score = mean(ENG_1 ... ENG_11)    [range 1.0-5.0]
NAT_score = mean(NAT_1 ... NAT_11)    [range 1.0-5.0]
NE_score  = mean(NE_1  ... NE_9)      [range 1.0-5.0]
```

**Note on reverse-scoring:** Consult the original scoring key from Lessiter et al. (2001). Some items within subscales are negatively worded and must be reversed (5 - raw + 1 = 6 - raw) before computing the mean.

## STEP 3: Interpretation

| Subscale | Low        | Moderate   | High       | Note                             |
|----------|------------|------------|------------|----------------------------------|
| SPS      | 1.0 – 2.0  | 2.0 – 3.5  | 3.5 – 5.0  | Higher = more "being there"      |
| ENG      | 1.0 – 2.0  | 2.0 – 3.5  | 3.5 – 5.0  | Higher = more engaged            |
| NAT      | 1.0 – 2.5  | 2.5 – 3.5  | 3.5 – 5.0  | Higher = more natural/coherent   |
| NE       | 1.0 – 1.5  | 1.5 – 2.5  | 2.5 – 5.0  | Higher = more adverse effects    |

**Important:** NE scores should ideally be LOW. High NE may confound presence scores — participants experiencing sickness may report lower presence not because presence is genuinely lower, but due to discomfort. Always report NE separately and consider it a moderating variable.

## STEP 4: Cross-media comparison note
ITC-SOPI was validated across TV, cinema, and VR. When comparing across media, use the same 44-item form without modification. The instrument intentionally excludes hardware-specific items to remain media-agnostic.

## References
- Lessiter, J., Freeman, J., Keogh, E., & Davidoff, J. (2001). Presence, 10(3), 282-297.
- Freeman, J., Lessiter, J., & IJsselsteijn, W. (2001). An introduction to presence. The Psychologist, 14, 190-194.
