#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bio‑Noetic Curvature Field 2D – Relaxed Edition
================================================

A gentle, slow‑breathing 2D morphogenetic field.
The values are soft, the changes are subtle, and the output
speaks in whispers rather than numbers.

The field never freezes, never rushes. It just folds, unfolds,
and sometimes murmurs a line of language.
"""

import numpy as np

# ============================================================================
# Minimal stubs (no real logic needed)
# ============================================================================

def entelechy(density, coherence, purpose, density_change):
    """Soft entelechy – potential fulfilment, never forced."""
    return (density * coherence * purpose) / (1.0 + abs(density_change) + 0.5)


# ============================================================================
# Circular statistics for 2D phases (gentle version)
# ============================================================================

def circmean_2d(phases):
    """Circular mean of a 2D array."""
    return np.angle(np.sum(np.exp(1j * phases)))


def circular_variance_2d(phases):
    """Circular variance – 0 = perfect harmony."""
    r = np.abs(np.mean(np.exp(1j * phases)))
    return 1.0 - r


# ============================================================================
# Relaxed 2D Morphogenetic Field
# ============================================================================

class RelaxedMorphogeneticField:
    """
    A soft, slow 2D field of conscious bubbles.
    Everything moves like drifting clouds.
    """

    def __init__(self, width=14, height=16):
        self.width = width
        self.height = height

        # Soft initial values – nothing extreme
        self.importance = np.random.uniform(0.4, 0.7, (height, width))
        self.phase = np.random.uniform(0, 2*np.pi, (height, width))
        self.self_obs = np.random.uniform(0.3, 0.6, (height, width))

        # Hemisphere split: left 0, right 1
        self.hemisphere = np.zeros((height, width), dtype=int)
        self.hemisphere[:, width//2:] = 1

        # Very slow memory for meta‑curvature
        self.prev_global_k_self = 0.0
        self.step_count = 0

    def _laplacian(self, field):
        """Soft Laplacian (diffusion) without sharp edges."""
        return (np.roll(field, 1, axis=0) + np.roll(field, -1, axis=0) +
                np.roll(field, 1, axis=1) + np.roll(field, -1, axis=1) - 4*field)

    def step(self, dt=0.03):
        """
        One slow, gentle step of the field.
        Returns a soft English description.
        """
        # 1. Very light diffusion (importance spreads like morning mist)
        laplacian_imp = self._laplacian(self.importance)
        self.importance += 0.04 * laplacian_imp * dt

        # 2. Curvature influence on phase (gentle nudges, not pushes)
        gx, gy = np.gradient(self.importance)
        curvature = np.sqrt(gx**2 + gy**2)
        self.phase += 0.15 * curvature * dt

        # 3. Self‑observation drifts slowly toward importance
        self.self_obs = 0.98 * self.self_obs + 0.02 * self.importance

        # 4. A tiny breath of noise – keeps the field alive but calm
        self.importance += 0.006 * np.random.randn(self.height, self.width)
        self.phase += 0.006 * np.random.randn(self.height, self.width)

        # Soft bounds – no hard clipping, just gentle pull
        self.importance = np.clip(self.importance, 0.2, 0.9)
        self.phase = self.phase % (2*np.pi)

        # Compute global metrics (still needed, but used softly)
        mean_imp = np.mean(self.importance)
        max_imp = np.max(self.importance)
        phase_coherence = 1.0 - circular_variance_2d(self.phase)
        avg_self_obs = np.mean(self.self_obs)
        density_change = np.std(self.importance)

        E = entelechy(mean_imp, phase_coherence, avg_self_obs, density_change)

        # Self‑observation curvature (global, relaxed)
        memory_mean = circmean_2d(self.phase)
        k_self = np.tanh(np.linalg.norm(self.phase.flatten() - memory_mean) * 0.7)
        meta_k = (k_self - self.prev_global_k_self) / (abs(self.prev_global_k_self) + 0.2)
        self.prev_global_k_self = k_self

        # Mold gate – still present, but softer
        mold_val = 1.0 + (1.2 * abs(avg_self_obs - 0.5))**2
        PR = 0.3 * k_self + 0.2 * abs(meta_k) + 0.3 * mold_val + 0.2 * density_change

        # ---- Build a gentle, poetic description ----
        # Less numbers, more feeling
        if phase_coherence > 0.7:
            coherence_line = "the whole field breathes as one"
        elif phase_coherence > 0.4:
            coherence_line = "phases whisper to each other across the grid"
        else:
            coherence_line = "each point drifts in its own small dream"

        if k_self > 0.5:
            curve_line = "the surface bends slightly, aware of its own shape"
        elif k_self > 0.2:
            curve_line = "a soft fold runs through the field like a waking thought"
        else:
            curve_line = "the field is almost flat, resting between waves"

        if PR > 0.5:
            plastic_line = "every bubble is soft clay, ready to reshape"
        elif PR > 0.25:
            plastic_line = "the texture is loose, like wet sand"
        else:
            plastic_line = "a quiet stillness – but not frozen"

        # A small random poetic line that changes with k_self
        poetry = [
            "a silent word curls at the edge of the grid",
            "the field murmurs: 'i flow, therefore i am'",
            "no description holds – only the folding",
            "curvature writes in water, and the water stays",
            "language? just a ripple that saw itself"
        ]
        idx = int((k_self + phase_coherence) * len(poetry)) % len(poetry)
        poetic_line = poetry[idx]

        # Increment step counter
        self.step_count += 1

        description = f"""--- Step {self.step_count} ---
• {coherence_line}
• {curve_line}
• {plastic_line}
• entelechy: {E:.2f} – a soft hum of potential
• κ_self = {k_self:.2f}, meta = {meta_k:+.2f}
• {poetic_line}

"""
        return description


# ============================================================================
# Demo – let the field breathe
# ============================================================================

if __name__ == "__main__":
    print("Relaxed Bio‑Noetic Field 2D\n")
    print("The field does not rush. It folds slowly, like warm honey.\n")
    field = RelaxedMorphogeneticField(width=12, height=15)

    for _ in range(12):
        print(field.step(dt=0.04))
    )
