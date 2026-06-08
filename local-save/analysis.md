# Measuring Presence in VR: Subjective Scales vs. Physiological Signals

**Comparing IPQ, ITC-SOPI, EEG, and GSR**

---

## 1. Overview

Presence — the subjective sense of "being there" inside a virtual environment — is the central dependent variable in VR research. Measuring it reliably is non-trivial because presence is simultaneously a cognitive, emotional, and bodily state. Two broad families of methods exist: **self-report questionnaires** (IPQ, ITC-SOPI) and **physiological/neuroimaging signals** (EEG, GSR/EDA). Each captures a different facet of the construct, and they are rarely interchangeable.

---

## 2. The iGroup Presence Questionnaire (IPQ)

### 2.1 Origins & Structure
Developed by Schubert, Friedmann & Regenbrecht (2001), the IPQ emerged from a factor-analytic study of VR presence. It contains **14 items** distributed across four subscales:

| Subscale | Items | What it captures |
|---|---|---|
| **SP** – Spatial Presence | 5 | Sense of physically inhabiting the VE |
| **INV** – Involvement | 4 | Attentional focus directed toward the VE |
| **REAL** – Experienced Realism | 4 | Perceived plausibility and fidelity |
| **G** – General Presence | 1 | Global anchor item (not in composite) |

Items use **bipolar 7-point scales** (0–6 in the canonical online version; 1–7 in some published adaptations). Six items are **reverse-scored** (`scored = 6 − raw`) to counteract acquiescence bias.

### 2.2 Scoring
- Each subscale score = **mean of its scored items** (range 0–6 or 1–7).
- A **composite total presence score** = mean of SP + INV + REAL (G excluded).
- Cronbach's α ≈ 0.87 across studies; SP is typically the strongest predictor of overall presence ratings.
- Interpretation guidelines: scores ≤ 2 = low presence; 2–4 = moderate; ≥ 4 = high (on a 0–6 scale).

### 2.3 What It Measures
The IPQ primarily captures **spatial and cognitive presence**: does the user feel they are *located in* the VE, and are their cognitive resources allocated there rather than to the physical room? REAL adds a plausibility dimension — whether the VE was consistent with real-world physics and appearance. The instrument is administered **post-exposure** (takes ~3 minutes) and is therefore a retrospective snapshot, not a continuous measure.

---

## 3. The ITC-Sense of Presence Inventory (ITC-SOPI)

### 3.1 Origins & Structure
Developed by Lessiter, Freeman, Keogh & Davidoff (2001) at the Independent Television Commission, the ITC-SOPI was designed to generalise across media (TV, film, VR), not just VR headsets. It contains **44 items** across four factors:

| Factor | Items | What it captures |
|---|---|---|
| **Physical Space** | 16 | Sense of being in the depicted environment |
| **Engagement** | 14 | Involvement, interest, enjoyment |
| **Ecological Validity / Naturalness** | 8 | Believability of depicted entities and physics |
| **Negative Effects** | 6 | Discomfort, nausea, disorientation |

Items use a **5-point Likert scale** (1 = Strongly Disagree → 5 = Strongly Agree). There are **no reverse-scored items** in the standard version; higher scores always indicate more of the construct.

### 3.2 Scoring
- Each factor score = **mean of its items** (range 1–5).
- No single composite is recommended; factors are treated independently.
- Negative Effects is typically reported separately as a measure of **cybersickness**, not presence per se.
- Cronbach's α ranges from 0.76 (Ecological Validity) to 0.92 (Physical Space).

### 3.3 What It Measures
The ITC-SOPI is broader than the IPQ. **Physical Space** overlaps strongly with IPQ's SP subscale. **Engagement** overlaps with IPQ's INV. However, the **Ecological Validity** factor specifically probes whether depicted objects and agents behaved naturalistically — a dimension the IPQ's REAL subscale partially covers but with fewer items. Crucially, the **Negative Effects** factor captures the dark side of immersion (nausea, dizziness), which the IPQ ignores entirely. The ITC-SOPI is also post-exposure and takes ~8–10 minutes.

---

## 4. Comparing IPQ and ITC-SOPI

| Dimension | IPQ | ITC-SOPI |
|---|---|---|
| **Item count** | 14 | 44 |
| **Response scale** | 7-point bipolar | 5-point Likert |
| **Reverse scoring** | Yes (6 items) | No |
| **Subscales** | SP, INV, REAL, G | Physical Space, Engagement, Eco. Validity, Neg. Effects |
| **Composite score** | Yes (SP+INV+REAL) | Not recommended |
| **Cybersickness** | Not assessed | Assessed (Neg. Effects) |
| **Media generality** | VR-centric | Cross-media |
| **Admin time** | ~3 min | ~8–10 min |
| **Validated α** | ~0.87 | 0.76–0.92 |

**Key convergence:** Both scales agree that presence has a spatial/location component and an attentional/engagement component. Correlations between IPQ-SP and ITC-SOPI Physical Space are typically r ≈ 0.60–0.75.

**Key divergence:** The ITC-SOPI captures **negative effects** and is **media-agnostic**; it can compare a cinema experience to a VR headset. The IPQ is leaner, faster, and more focused on the VR spatial experience specifically, making it the dominant choice in HCI and VR research.

---

## 5. Physiological Measures: EEG

### 5.1 What It Measures
Electroencephalography (EEG) records **electrical potentials at the scalp** generated by synchronised cortical neuronal activity. In VR presence research, the signals of interest include:

- **Alpha power (8–13 Hz):** Suppression of alpha (event-related desynchronisation, ERD) at parietal/occipital electrodes correlates with increased visual attention and immersion. Higher alpha suppression → more attentional engagement with the VE.
- **Theta power (4–8 Hz):** Frontal theta increases with cognitive load and emotional engagement; elevated frontal theta has been linked to higher presence ratings.
- **Gamma (>30 Hz):** Associated with feature binding and perceptual integration; some studies find gamma increases in high-presence conditions.
- **Event-related potentials (ERPs):** P300 amplitude decreases when stimuli are VE-congruent (participant is "absorbed"), serving as an implicit marker of attention allocation.

### 5.2 Item / Signal Structure
EEG has no "items" — it is a **continuous multivariate time series** (typically 32–256 channels × thousands of samples/second). Analysis pipelines involve:
1. **Preprocessing:** bandpass filtering, ICA artifact rejection (eye movements, muscle noise).
2. **Epoching:** segmenting around events.
3. **Feature extraction:** power spectral density (PSD), coherence, connectivity metrics.
4. **Dimensionality reduction / classification:** often machine-learning-based.

### 5.3 Advantages & Limitations
- ✅ **Continuous, millisecond-resolution** — can track fluctuations in presence during exposure.
- ✅ **Cannot be faked** — not subject to demand characteristics or social desirability bias.
- ❌ **High noise** — motion artifacts are severe in active VR tasks.
- ❌ **Complex preprocessing** — results are pipeline-dependent.
- ❌ **Indirect** — no EEG signature maps cleanly onto "presence" as a unitary construct.

---

## 6. Physiological Measures: GSR / EDA

### 6.1 What It Measures
Galvanic Skin Response (GSR), now more commonly termed **Electrodermal Activity (EDA)**, measures **sweat gland activity** driven by the sympathetic branch of the autonomic nervous system. It has two components:

- **Tonic level (Skin Conductance Level, SCL):** Slow baseline shifts reflecting general arousal.
- **Phasic responses (Skin Conductance Responses, SCRs):** Rapid transient peaks (latency ~1–3 s) following discrete stimuli or emotional events.

In VR presence research, higher SCL and more frequent SCRs during VR exposure (vs. a 2D control) are interpreted as markers of **heightened autonomic arousal** consistent with greater immersion. For example, exposure to a virtual height or threat scenario typically produces larger SCRs in participants who later report higher presence.

### 6.2 Signal Structure
Like EEG, GSR is a **continuous time series** (typically sampled at 4–64 Hz). Analysis involves:
1. **Low-pass filtering** to separate tonic from phasic components.
2. **SCR detection:** amplitude threshold or convolution-based decomposition (e.g., Ledalab, NeuroKit2).
3. **Feature extraction:** SCR count, peak amplitude, rise time, SCL mean.

### 6.3 Advantages & Limitations
- ✅ **Simple, affordable hardware** — wrist-worn sensors widely available.
- ✅ **Robust signal** — less susceptible to motion artifact than EEG.
- ✅ **Sensitive to emotional valence and arousal** — complements cognitive presence measures.
- ❌ **Measures arousal, not presence specifically** — fear, excitement, and cognitive effort all increase GSR.
- ❌ **Slow temporal resolution** — cannot distinguish second-by-second presence fluctuations.
- ❌ **Inter-individual variability** is large; normalisation is critical.

---

## 7. Cross-Method Comparison Summary

| Criterion | IPQ | ITC-SOPI | EEG | GSR/EDA |
|---|---|---|---|---|
| **Construct targeted** | Spatial/cognitive presence | Broad presence + wellbeing | Attention, arousal, neural engagement | Autonomic arousal |
| **Temporal resolution** | Post-hoc (static) | Post-hoc (static) | Continuous (ms) | Continuous (s) |
| **Subjectivity** | Self-report (conscious) | Self-report (conscious) | Objective (implicit) | Objective (implicit) |
| **Demand characteristics risk** | High | High | None | None |
| **Ecological validity in VR** | High (VR-specific) | Moderate (cross-media) | Moderate (motion artifacts) | High |
| **Ease of administration** | Very easy | Easy | Complex | Moderate |
| **Cost** | Free | Free | High (hardware + expertise) | Low–Moderate |
| **What presence dimension?** | "Being there" cognitively | "Being there" + comfort | Neural correlates of attention | Emotional/arousal correlates |

---

## 8. Methodological Recommendations

1. **Triangulate methods.** No single measure captures all facets of presence. The gold-standard design combines IPQ or ITC-SOPI (for cognitive/spatial presence) with GSR (for emotional arousal) and optionally EEG (for continuous attentional tracking).

2. **Match scale to research question.** Use the IPQ when comparing VR systems on spatial immersion. Use the ITC-SOPI when comparing across media or when cybersickness is a concern. Use EEG when you need moment-to-moment presence dynamics. Use GSR when measuring emotional engagement or threat responses.

3. **Account for reverse scoring in IPQ.** Six items require `scored = 6 − raw` before computing subscale means. A common error is computing means on raw scores, which deflates SP and INV.

4. **Normalise physiological signals per-participant.** Both EEG power and SCL vary enormously across individuals; z-scoring or baseline-normalisation is essential before between-subjects comparisons.

5. **Report all IPQ subscales separately.** The composite total presence score masks important dissociations — e.g., a system might score high on REAL but low on INV, which has different theoretical implications than a uniformly moderate score.

---

## 9. References

- Schubert, T., Friedmann, F., & Regenbrecht, H. (2001). The experience of presence: Factor analytic insights. *Presence: Teleoperators and Virtual Environments, 10*(3), 266–281.
- Lessiter, J., Freeman, J., Keogh, E., & Davidoff, J. (2001). A cross-media presence questionnaire: The ITC-Sense of Presence Inventory. *Presence: Teleoperators and Virtual Environments, 10*(3), 282–297.
- Slobounov, S. M., Ray, W., Johnson, B., Slobounov, E., & Newell, K. M. (2015). Modulation of cortical activity in 2D versus 3D virtual reality environments: An EEG study. *International Journal of Psychophysiology, 95*(3), 254–260.
- Boucsein, W. (2012). *Electrodermal Activity* (2nd ed.). Springer.
- Makowski, D., et al. (2021). NeuroKit2: A Python toolbox for neurophysiological signal processing. *Behavior Research Methods, 53*, 1689–1696.
- iGroup IPQ online scoring tool: https://www.igroup.org/pq/ipq/index.php
