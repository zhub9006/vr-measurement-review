# Measuring Presence in VR: Subjective Scales vs. Physiological Signals

## Overview

Presence — the psychological sense of "being there" in a virtual environment — is the central dependent variable in most VR research. Two broad families of measurement have emerged: **self-report questionnaires** (chiefly the IPQ and ITC-SOPI) and **physiological/neurological signals** (chiefly EEG and GSR). Each family captures a different layer of the presence experience and carries its own structural logic, scoring conventions, and interpretive limitations.

---

## 1. The iGroup Presence Questionnaire (IPQ)

### Origin and Theoretical Basis
Developed by Schubert, Friedmann, and Regenbrecht (2001), the IPQ is grounded in a cognitive–constructivist model of presence. It treats presence as a multidimensional mental construction rather than a unitary sensation.

### Item Structure
The IPQ contains **14 items** across **three subscales** plus one standalone global item:

| Subscale | Items | What it probes |
|---|---|---|
| **Spatial Presence (SP)** | 5 items | The felt sense of being physically *inside* the VE; bodily self-location |
| **Involvement (INV)** | 4 items | Attentional capture; awareness of VE vs. real world |
| **Experienced Realism (REAL)** | 4 items | Perceived plausibility and fidelity of the VE |
| **General (G)** | 1 item | Global "being there" anchor |

All items use a **7-point bipolar Likert scale** (1 = fully disagree/not at all → 7 = fully agree/very much). One item (INV4) is **reverse-coded**: "How aware were you of the *real* world?" is recoded as `8 − raw score` before averaging, because high real-world awareness reflects low presence.

### Scoring
Each subscale score is the **arithmetic mean** of its constituent items (after reverse-coding). Scores are reported as three separate means — SP, INV, REAL — plus the G item; collapsing to a single total is discouraged because the three factors are theoretically and empirically distinct. Published benchmarks (igroup.org normative database, N > 3,000) give typical means of SP ≈ 3.9, INV ≈ 3.7, REAL ≈ 2.8 on the 1–7 scale.

### Psychometric Properties
- Cronbach α: SP = 0.88, INV = 0.70, REAL = 0.66
- Three-factor CFA confirmed; convergent validity against the SUS scale
- Administered **post-exposure only** (~3 min); vulnerable to memory decay and demand characteristics

---

## 2. The ITC Sense of Presence Inventory (ITC-SOPI)

### Origin and Theoretical Basis
Developed by Lessiter, Freeman, Keogh, and Davidoff (2001) at ITC/Goldsmiths, the ITC-SOPI adopts a broader phenomenological frame. It was designed to generalise across media (TV, cinema, VR, audio), making it media-agnostic where the IPQ is VR-specific.

### Item Structure
The ITC-SOPI contains **44 items** across **four subscales**:

| Subscale | Items | What it probes |
|---|---|---|
| **Sense of Physical Space** | 14 items | Spatial presence; sense of being inside the depicted environment |
| **Engagement** | 13 items | Emotional involvement; interest; attention |
| **Ecological Validity / Naturalness** | 10 items | Perceived naturalness and believability of depicted events |
| **Negative Effects** | 7 items | Discomfort, nausea, disorientation (cybersickness proxy) |

Items use a **5-point Likert scale** (1 = strongly disagree → 5 = strongly agree). Several items are reverse-coded.

### Scoring
Each subscale is scored as the **mean of its items** (after reverse-coding). Unlike the IPQ, the ITC-SOPI explicitly models negative effects as a fourth dimension rather than treating them as confounds. Higher scores on the first three subscales indicate greater presence; higher scores on Negative Effects indicate more discomfort. No validated composite total is recommended.

### Psychometric Properties
- Internal consistency: α = 0.87–0.92 across subscales
- Cross-media validity demonstrated in cinema, TV, and VR samples
- Administered post-exposure (~8–10 min); longer than IPQ, more detailed coverage of engagement

---

## 3. IPQ vs. ITC-SOPI: Direct Comparison

| Dimension | IPQ | ITC-SOPI |
|---|---|---|
| **Total items** | 14 + 1 global | 44 |
| **Response scale** | 7-point Likert | 5-point Likert |
| **Subscales** | SP, INV, REAL (+ G) | Physical Space, Engagement, Ecological Validity, Negative Effects |
| **Media scope** | VR-specific | Cross-media |
| **Cybersickness** | Excluded (separate SSQ recommended) | Included as subscale |
| **Administration time** | ~3 min | ~8–10 min |
| **Granularity** | Moderate | High |
| **Best for** | Quick VR-specific presence snapshots | Detailed media-comparison studies |

Both scales are **post-hoc** and **introspective**: they ask participants to reflect on a completed experience, introducing potential recall bias, social desirability, and demand characteristics. Neither can capture moment-to-moment fluctuations in presence during immersion.

---

## 4. Physiological Approaches: EEG

### What EEG Measures
Electroencephalography records cortical electrical activity via scalp electrodes, typically at 250–2000 Hz. For VR presence research, key signals include:

- **Alpha suppression (8–12 Hz):** Reduced alpha power, especially over occipital and parietal regions, correlates with visual engagement and spatial attention — a neural correlate of the attentional capture component of presence.
- **Theta oscillations (4–8 Hz):** Frontal theta increases with cognitive engagement and navigation; linked to spatial memory and the sense of self-location.
- **Gamma bursts (30–80 Hz):** Associated with perceptual binding; increased gamma has been reported during high-presence moments.
- **Event-related potentials (ERPs):** P300 amplitude and latency have been used to probe how much cognitive resources the VE commands vs. the real world.

### Item/Signal Structure
EEG has no "items" in the questionnaire sense. The "structure" is the **frequency band × electrode region × time window** space. Typical pipelines involve:
1. Artefact rejection (eye blinks, muscle noise via ICA)
2. Band-pass filtering per frequency band of interest
3. Power spectral density or event-related synchronisation/desynchronisation (ERS/ERD) computation
4. Source localisation (optional)

### Scoring
EEG presence indices are typically **continuous, relative measures** — e.g., alpha ERD expressed as percentage change from a resting baseline. There is no agreed single "presence score"; different labs use different band/region combinations, making cross-study comparison difficult.

### Strengths and Limitations
- **Strengths:** Millisecond temporal resolution; continuous; not susceptible to introspective bias; can detect subconscious engagement
- **Limitations:** Expensive; motion-sensitive (VR locomotion causes artefacts); no standardised presence-specific protocol; high inter-individual variability; requires expert analysis

---

## 5. Physiological Approaches: GSR / EDA

### What GSR Measures
Galvanic Skin Response (GSR), also called Electrodermal Activity (EDA), measures sweat gland activity via skin conductance. It is controlled by the sympathetic branch of the autonomic nervous system and is a reliable index of **arousal** and **emotional activation**.

In VR presence research, GSR is used to operationalise the **autonomic / emotional engagement** component of presence — the idea that a truly present participant will respond physiologically to virtual stimuli as they would to real ones (Slater's "place illusion" and "plausibility illusion" framework).

### Signal Structure
GSR signals decompose into:
- **Skin Conductance Level (SCL):** Slow tonic baseline; reflects general arousal state
- **Skin Conductance Responses (SCRs):** Fast phasic peaks (latency 1–5 s post-stimulus); event-locked responses to specific VE events

### Scoring
- **SCL** is typically reported as mean conductance (µS) over a time window
- **SCR amplitude** (peak − onset, µS) and **SCR frequency** (SCRs per minute) are the standard event-locked metrics
- Presence is inferred when SCR amplitude/frequency to virtual stimuli approaches that seen for equivalent real-world stimuli, or when SCRs predict post-hoc questionnaire scores

### Strengths and Limitations
- **Strengths:** Inexpensive; robust; wearable sensors available; continuous; directly indexes emotional arousal
- **Limitations:** Measures *arousal*, not presence per se — fear, excitement, and presence all elevate GSR; confounded by physical activity and temperature; no validated GSR-specific presence threshold

---

## 6. Cross-Method Synthesis

### What Each Method Actually Measures

| Method | Primary Construct | Temporal Resolution | Subjectivity |
|---|---|---|---|
| IPQ (SP) | Retrospective spatial self-location | Post-hoc | High |
| IPQ (INV) | Retrospective attentional involvement | Post-hoc | High |
| IPQ (REAL) | Retrospective plausibility judgement | Post-hoc | High |
| ITC-SOPI | Retrospective multidimensional presence + discomfort | Post-hoc | High |
| EEG (alpha/theta) | Online cortical engagement & spatial attention | ~50 ms | None |
| GSR (SCR) | Online autonomic arousal / emotional activation | ~1–5 s | None |

### Convergence and Divergence
Research comparing self-report and physiological measures of presence shows **weak to moderate correlations** (r ≈ 0.2–0.4 in most studies). This is not necessarily a failure of either approach — it may reflect genuine construct divergence:

- Questionnaires capture **conscious, narrative presence**: the participant's post-hoc story about how present they felt
- EEG captures **online perceptual and attentional processing**: what the brain was actually doing during immersion
- GSR captures **autonomic reactivity**: how much the body treated virtual stimuli as real threats or rewards

A participant can score high on IPQ-SP (consciously felt very present) while showing modest GSR (low autonomic arousal), e.g., in a calm, exploratory VE. Conversely, a frightening VE may spike GSR without the participant endorsing high REAL scores.

### Recommendations for Study Design

1. **Use IPQ or ITC-SOPI as the primary presence measure** in most VR studies — they are validated, fast, and directly measure the construct of interest.
2. **Add GSR when emotional/arousal reactivity to virtual events is the key hypothesis** — it provides an online, bias-free index of how physiologically "real" events felt.
3. **Add EEG when spatial attention, cognitive load, or moment-to-moment presence fluctuations are hypotheses** — but budget for substantial preprocessing and artefact management.
4. **Use IPQ and ITC-SOPI together** only when the study needs both VR-specific (IPQ) and media-comparative (ITC-SOPI) benchmarks, or when the Negative Effects subscale of ITC-SOPI is needed alongside presence scores.
5. **Never use GSR or EEG alone as a presence measure** — they require concurrent self-report for construct validation.

---

## References

- Schubert, T., Friedmann, F., & Regenbrecht, H. (2001). The experience of presence: Factor analytic insights. *Presence: Teleoperators and Virtual Environments*, 10(3), 266–281.
- Lessiter, J., Freeman, J., Keogh, E., & Davidoff, J. (2001). A cross-media presence questionnaire: The ITC-Sense of Presence Inventory. *Presence*, 10(3), 282–297.
- Slater, M. (2009). Place illusion and plausibility can lead to realistic behaviour in immersive virtual environments. *Philosophical Transactions of the Royal Society B*, 364(1535), 3549–3557.
- Baumgartner, T., Valko, L., Esslen, M., & Jäncke, L. (2006). Neural correlate of spatial presence in an arousing and noninteractive virtual reality: An EEG and psychophysiology study. *CyberPsychology & Behavior*, 9(1), 30–45.
- Meehan, M., Insko, B., Whitton, M., & Brooks, F. P. (2002). Physiological measures of presence in stressful virtual environments. *ACM Transactions on Graphics*, 21(3), 645–652.
- Vorderer, P., Wirth, W., Gouveia, F. R., Biocca, F., Saari, T., Jäncke, F., & Zillmann, D. (2004). MEC Spatial Presence Questionnaire (MEC-SPQ). Report to the European Community, Project Presence: MEC (IST-2001-37661).
