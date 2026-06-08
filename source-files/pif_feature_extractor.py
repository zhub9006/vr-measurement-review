# -*- coding: utf-8 -*-
"""
pif/feature_extractor.py  —  SOURCE FILE COPY
=============================================
Original: zhub9006/perception-immersion-framework
SHA: c704457561a5f28b500da68e629350b0ba67e7db
Retrieved: 2026-06-08

Hemodynamic and spectral feature extraction stubs.

Modalities handled:
  - fNIRS : HbO/HbR channel statistics, slope, peak amplitude
  - EEG   : Band power (delta, theta, alpha, beta, gamma), alpha/theta ratio
  - GSR   : SCR peaks, tonic level, area under curve
  - Eye   : Pupil dilation mean/std, fixation duration, saccade rate
"""

from __future__ import annotations
import numpy as np
from .config import PifConfig


class FeatureExtractor:
    """Extract modality-specific features from raw physiological signals."""

    def __init__(self, config: PifConfig) -> None:
        self.config = config
        self._dispatch = {
            "fnirs": self.extract_fnirs,
            "eeg": self.extract_eeg,
            "gsr": self.extract_gsr,
            "eye": self.extract_eye,
        }

    def extract(self, signal: np.ndarray) -> np.ndarray:
        modality = self.config.modality
        if modality not in self._dispatch:
            raise ValueError(f"Unsupported modality '{modality}'.")
        return self._dispatch[modality](signal)

    # fNIRS: mean, std, slope, peak_amplitude per channel
    def extract_fnirs(self, signal: np.ndarray) -> np.ndarray:
        features = []
        for ch in signal:
            features.extend([ch.mean(), ch.std(), self._linear_slope(ch), ch.max() - ch.min()])
        return np.array(features, dtype=float)

    # EEG: band power (delta/theta/alpha/beta/gamma) + alpha/theta ratio per channel
    def extract_eeg(self, signal: np.ndarray, fs: float = 256.0) -> np.ndarray:
        bands = {"delta": (1, 4), "theta": (4, 8), "alpha": (8, 13), "beta": (13, 30), "gamma": (30, 45)}
        features = []
        for ch in signal:
            band_powers = {}
            for band, (lo, hi) in bands.items():
                band_powers[band] = self._band_power(ch, fs, lo, hi)
                features.append(band_powers[band])
            at_ratio = (band_powers["alpha"] / band_powers["theta"]
                        if band_powers["theta"] > 0 else 0.0)
            features.append(at_ratio)
        return np.array(features, dtype=float)

    # GSR: tonic SCL, phasic SCR peak count, area under curve
    def extract_gsr(self, signal: np.ndarray) -> np.ndarray:
        peaks = self._count_peaks(signal)
        tonic = signal.mean()
        auc = np.trapz(signal)
        return np.array([tonic, peaks, auc], dtype=float)

    # Eye-tracking: pupil mean, std, range, dilation peak count
    def extract_eye(self, signal: np.ndarray) -> np.ndarray:
        return np.array([signal.mean(), signal.std(), signal.max() - signal.min(),
                         self._count_peaks(signal)], dtype=float)

    @staticmethod
    def _linear_slope(x: np.ndarray) -> float:
        n = len(x)
        if n < 2:
            return 0.0
        t = np.arange(n, dtype=float)
        return float(np.polyfit(t, x, 1)[0])

    @staticmethod
    def _band_power(x: np.ndarray, fs: float, lo: float, hi: float) -> float:
        fft_vals = np.abs(np.fft.rfft(x)) ** 2
        freqs = np.fft.rfftfreq(len(x), d=1.0 / fs)
        mask = (freqs >= lo) & (freqs < hi)
        return float(fft_vals[mask].mean()) if mask.any() else 0.0

    @staticmethod
    def _count_peaks(x: np.ndarray, min_height_factor: float = 0.5) -> int:
        threshold = x.mean() * min_height_factor
        peaks = 0
        for i in range(1, len(x) - 1):
            if x[i] > x[i - 1] and x[i] > x[i + 1] and x[i] > threshold:
                peaks += 1
        return peaks
