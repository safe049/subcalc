# SubCalc — Subjective Time Calculator

A lightweight command-line tool to estimate **subjective time perception** based on cognitive and emotional states.  
Inspired by psychological models of time perception, it quantifies how focus, novelty, arousal, and flow alter your sense of duration.

---

## 📦 Installation

Use the install script[to uninstall,use the another script]:

```bash
sudo ./install.sh
```

> Ensure `/usr/lib` is in your `PYTHONPATH`

---

## 🚀 Usage

```bash
subcalc {custom,single,range} [OPTIONS]
```

### Modes

| Mode      | Description |
|-----------|-------------|
| `single`  | Compute subjective time for **1 unit** (second/hour/day) with given `[c,n,a,f]`. |
| `custom`  | Compute for **`t` units** with one set of `[c,n,a,f]`. |
| `range`   | Compute total subjective time for a **sequence** of states, each lasting `t` units. |

### Parameters (`c`, `n`, `a`, `f`)

All values must be in `[0.0, 1.0]`:

- `-c`, `--concentration`: Attentional focus  
- `-n`, `--novelty`: Stimulus novelty / information density  
- `-a`, `--arousal`: Emotional/physiological activation  
- `-f`, `--flow`: Immersion depth (Csíkszentmihályi’s flow state)

### Examples

```bash
# Single hour in deep coding flow
subcalc single -c 0.95 -n 0.2 -a 0.1 -f 0.9

# 2.5 hours of moderate engagement
subcalc custom -t 2.5 -c 0.6 -n 0.4 -a 0.3 -f 0.5

# Full day segmented into 3 activities (each 1 hour)
subcalc range -t 1 --seq "[[0.9,0.2,0.1,0.85],[0.3,0.1,0.1,0.0],[0.85,0.7,0.4,0.9]]"
```

> 💡 The `--seq` argument accepts a **JSON-formatted list of lists**. Use double quotes to wrap the entire sequence.

---

## 🔬 Model Details

Subjective time is computed as:

\[
T_s = T_r \cdot k, \quad \text{where} \quad
k = \operatorname{clamp}\left(1 - 0.6c + 0.8n + 0.5a - 1.2f,\ 0.1,\ 3.0\right)
\]

- **Baseline**: When all factors are 0, \(k = 1\) → subjective = objective time.
- **Flow & Focus**: Compress time (\(k < 1\)).
- **Novelty & Arousal**: Expand time (\(k > 1\)).

Weights are empirically tuned for typical human experience but can be adjusted in `utils.py`.

---

## 🛠️ Requirements

- Python 3.6+
- Standard library only (`argparse`, `json`)

---

## 📝 Notes

- This tool is **unit-agnostic**: if `t = 1` means "1 hour", output is in subjective hours.
- Designed for **personal introspection**, not clinical or scientific use.
- Some part of this README is written by AI Qwen3-Max [Not a Ad!]

---
