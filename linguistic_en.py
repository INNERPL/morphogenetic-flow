#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from typing import List

# from morphogenetic_cortex import Bubble, PixelTile, entelechy


# -----------------------------
# New Bio‑Noetic Curvature Layer
# -----------------------------

def self_observation_curvature(state_vec, memory_mean):
    """Curvature of self-observation: tanh(||Ψ − <Ψ>||)."""
    diff = np.linalg.norm(state_vec - memory_mean)
    return np.tanh(diff)


def meta_curvature(k_prev, k_curr, eps=1e-6):
    """Depth of curvature: nonlinear ratio of Δκ."""
    return (k_curr - k_prev) / (abs(k_prev) + eps)


def mold_gate(r):
    """Morphogenetic gate: amplifies extremes, compresses mid-range."""
    return 1 + (2 * abs(r - 0.5))**2


def plastic_relaxation(k_self, L, mold, delta):
    """Plastic relaxation operator (PR)."""
    return 0.4 * k_self + 0.3 * L + 0.2 * mold + 0.1 * delta


# -----------------------------
# Main Linguistic Description
# -----------------------------

def linguistic_description_en(bubbles: List['Bubble'], tiles: List['PixelTile']) -> str:
    """
    English linguistic description of the Morphogenetic Cortex state.
    Enhanced with curvature metrics, meta-curvature, mold gates,
    and plastic relaxation indicators.
    """

    if not bubbles:
        return "The field is formless; no conscious structure emerges."

    n_bub = len(bubbles)
    n_cons = sum(1 for b in bubbles if b.is_conscious)

    # Importance
    importances = np.array([b.importance for b in bubbles])
    mean_imp = float(np.mean(importances))
    max_imp = float(np.max(importances))

    # Hemispheres
    left = [b for b in bubbles if b.hemisphere == 0]
    right = [b for b in bubbles if b.hemisphere == 1]

    left_imp = np.mean([b.importance for b in left]) if left else 0.0
    right_imp = np.mean([b.importance for b in right]) if right else 0.0

    # Phases
    phases = np.array([b.effective_phase() for b in bubbles])
    phase_coherence = 1.0 - (np.std(phases) / np.pi)

    # Self‑observation
    self_obs = np.array([b.self_observation for b in bubbles])
    avg_self_obs = float(np.mean(self_obs))

    # Entelechy
    total_density = mean_imp
    total_coherence = phase_coherence
    total_purpose = avg_self_obs
    total_density_change = float(np.std(importances))

    E = entelechy(
        total_density,
        total_coherence,
        total_purpose,
        total_density_change
    )

    # -----------------------------
    # New curvature metrics
    # -----------------------------

    memory_mean = np.mean(phases)
    k_self = self_observation_curvature(phases, memory_mean)

    # meta-curvature (placeholder: using same value for prev/curr)
    meta_k = meta_curvature(k_self, k_self)

    # mold gate
    mold_val = mold_gate(np.mean(self_obs))

    # plastic relaxation
    PR = plastic_relaxation(
        k_self,
        meta_k,
        mold_val,
        total_density_change
    )

    return (
        f"There are {n_bub} bubbles, of which {n_cons} are conscious.\n"
        f"Mean importance (Wint): {mean_imp:.3f}, maximum: {max_imp:.3f}.\n"
        f"Left hemisphere: {len(left)} bubbles (mean importance {left_imp:.3f}).\n"
        f"Right hemisphere: {len(right)} bubbles (mean importance {right_imp:.3f}).\n"
        f"Phase coherence: {phase_coherence:.2f} (1 = full synchrony).\n"
        f"Mean self‑observation: {avg_self_obs:.3f}.\n"
        f"Entelechy (potential fulfillment): {E:.3f}.\n"
        f"Self‑observation curvature: {k_self:.3f}.\n"
        f"Meta‑curvature depth: {meta_k:.3f}.\n"
        f"Morphogenetic gate (mold): {mold_val:.3f}.\n"
        f"Plastic relaxation index: {PR:.3f}.\n"
        f"The field folds upon itself; form emerges from curvature and bio‑noetic tension."
    )
