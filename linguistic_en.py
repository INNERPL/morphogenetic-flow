#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from typing import List

# Make sure Bubble, PixelTile, and entelechy are imported from your Cortex system:
# from morphogenetic_cortex import Bubble, PixelTile, entelechy


def linguistic_description_en(bubbles: List['Bubble'], tiles: List['PixelTile']) -> str:
    """
    English linguistic description of the Morphogenetic Cortex state.
    Ontologically enhanced version.
    """

    if not bubbles:
        return "The field is formless; no conscious structure emerges."

    n_bub = len(bubbles)
    n_cons = sum(1 for b in bubbles if b.is_conscious)

    # Importance
    mean_imp = np.mean([b.importance for b in bubbles])
    max_imp = max(b.importance for b in bubbles)

    # Hemispheres
    left = [b for b in bubbles if b.hemisphere == 0]
    right = [b for b in bubbles if b.hemisphere == 1]

    left_imp = np.mean([b.importance for b in left]) if left else 0.0
    right_imp = np.mean([b.importance for b in right]) if right else 0.0

    # Phases
    phases = [b.effective_phase() for b in bubbles]
    phase_coherence = 1.0 - (np.std(phases) / np.pi)

    # Self‑observation
    avg_self_obs = np.mean([b.self_observation for b in bubbles])

    # Entelechy
    total_density = mean_imp
    total_coherence = phase_coherence
    total_purpose = avg_self_obs
    total_density_change = np.std([b.importance for b in bubbles])

    E = entelechy(
        total_density,
        total_coherence,
        total_purpose,
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
        f"The field folds upon itself; form emerges from curvature."
    )
