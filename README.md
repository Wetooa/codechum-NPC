## NPC 2025 Writeup

This repository collects concise writeups and reference implementations for the NPC 2025 group-stage semifinal problems. Each solution is a standalone Python script focused on demonstrating the core insight as quickly as possible, with inline commentary that captures the reasoning process.

### Structure

- `group-stage-semifinals/1.py` – Longest plateau detection via `itertools.groupby`.
- `group-stage-semifinals/2.py` – String rotation checker using brute-force rotations.
- `group-stage-semifinals/3.py` – Longest bitwise-AND chain computed with a single pass.
- `group-stage-semifinals/4.py` – Optimal string rotation minimizing adjacent ASCII deltas.
- `group-stage-semifinals/5.py` – Compact string encoder combining run-length encoding and digit grouping.
- `group-stage-semifinals/6.py` – Rotational edit-distance minimization with reusable distance helper.
- `group-stage-semifinals/7.py` – Alternating-parity snake traversal using decomposition and parity simulation.
- `group-stage-semifinals/8.py` – Matrix-zero transformation via strategic row/column flips.

### Requirements

- Python 3.9+ (standard library only).

### Running a Solution

```bash
python group-stage-semifinals/3.py
```

Each script prompts for its own input (matching CodeChum/NPC problem statements) and prints the required output directly.

### Problem Highlights

1. **Longest Plateau**  
   Treats identical consecutive elements as groups; takes the maximum group length after stripping the sentinel input.

2. **String Rotation Checker**  
   Compares every left rotation of the first string to the second, leveraging Python slicing for clarity since constraints are tiny.

3. **Bitwise AND Chain**  
   Maintains a running chain length whenever adjacent numbers share a non-zero AND result, mirroring sliding-window logic.

4. **Optimal String Rotation**  
   Precomputes a scoring helper (`calc_score`) to sum adjacent ASCII differences, then brute-forces all rotations while tracking the minimum.

5. **Compact String Encoder**  
   Uses `groupby` twice: letters collapse via run-length encoding while digits accumulate in temporary buckets that become bracketed blocks.

6. **Rotational Edit Distance**  
   Rotates one string left, recomputes Hamming distance with `calc_distance`, and records the best rotation-specific edit count.

7. **Alternating Parity Snake**  
   Splits the work into snake traversal (row-wise zigzag flattening) and parity alignment, evaluating both possible starting parities.

8. **Matrix Zero Transformation**  
   Selects column flips based on the first row, then checks whether subsequent rows can be resolved via optional row flips; also tries the inverted first row to cover the alternative column configuration.

### Notes

- Solutions prioritize fast comprehension over exhaustive optimization because NPC inputs are small.
- Inline comments in each script expand on the reasoning, trade-offs, and small tricks (e.g., rotation via slicing, `zip` for adjacent pairs).

