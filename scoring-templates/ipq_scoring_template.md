# IPQ Scoring Template
# Instrument: Igroup Presence Questionnaire (IPQ)
# Schubert, Friedmann & Regenbrecht (2001)
# 14 items, 7-point Likert scale (1=fully disagree, 7=fully agree)
# -------------------------------------------------------------------

## STEP 1: Record raw responses (1-7 for each item)

| Item ID | Item Text (abbreviated)                                        | Raw Score (1-7) | Reverse? | Corrected Score |
|---------|----------------------------------------------------------------|-----------------|----------|-----------------|
| GP      | Sense of 'being there' in the computer generated world         |                 | No       |                 |
| SP1     | Sense of acting in the virtual space                           |                 | No       |                 |
| SP2     | Felt present in the virtual space                              |                 | No       |                 |
| SP3     | Did NOT feel present in the virtual space                      |                 | **YES**  | 8 - raw         |
| SP4     | Sense of being there                                           |                 | No       |                 |
| SP5     | Virtual world seemed more realistic than real world            |                 | No       |                 |
| INV1    | Not aware of real environment                                  |                 | No       |                 |
| INV2    | Still paid attention to real environment                       |                 | **YES**  | 8 - raw         |
| INV3    | Completely captivated by the virtual world                     |                 | No       |                 |
| INV4    | VE experience consistent with real world experience            |                 | No       |                 |
| REAL1   | Virtual world seemed real                                      |                 | No       |                 |
| REAL2   | Virtual world was NOT real                                     |                 | **YES**  | 8 - raw         |
| REAL3   | Virtual world seemed realistic                                 |                 | No       |                 |
| REAL4   | Objects in VE did NOT seem real                                |                 | **YES**  | 8 - raw         |

## STEP 2: Compute subscale scores

### Spatial Presence (SP) — 5 items
```
SP = (SP1_corrected + SP2_corrected + SP3_corrected + SP4_corrected + SP5_corrected) / 5
SP Range: 1.0 – 7.0
```

### Involvement (INV) — 4 items  
```
INV = (INV1_corrected + INV2_corrected + INV3_corrected + INV4_corrected) / 4
INV Range: 1.0 – 7.0
```

### Realness (REAL) — 4 items
```
REAL = (REAL1_corrected + REAL2_corrected + REAL3_corrected + REAL4_corrected) / 4
REAL Range: 1.0 – 7.0
```

### General Presence (GP) — 1 item (criterion, not summed)
```
GP = raw score on GP item
GP Range: 1 – 7
```

## STEP 3: Interpretation benchmarks (approximate, from literature)

| Subscale         | Low Presence | Moderate | High Presence |
|------------------|--------------|----------|---------------|
| Spatial Presence | < 3.0        | 3.0-5.0  | > 5.0         |
| Involvement      | < 3.0        | 3.0-5.0  | > 5.0         |
| Realness         | < 2.5        | 2.5-4.5  | > 4.5         |

**Note:** Benchmarks are study-dependent. Always report raw subscale means and SDs. Compare across conditions within your own study rather than to absolute thresholds.

## STEP 4: Validity check
All three subscale scores should correlate positively with GP item. If SP or REAL correlates negatively with GP, check for data entry errors or reverse-scoring mistakes.

## References
- Schubert, T., Friedmann, F., & Regenbrecht, H. (2001). Presence, 10(3), 266-281.
- IPQ website: http://www.igroup.org/pq/ipq/index.php
