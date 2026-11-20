# Tiny Chess — a chess engine in 4 KB of Python

A complete, deterministic chess engine squeezed into a single
**4,064-byte** Python file (the competition entry packs this readable
source with lzma + base85; what you see here is the exact logic that
plays).

## What's inside

- 0x88 board representation
- Negamax alpha-beta search with PVS (principal variation search),
  quiescence (captures + check evasions), transposition table with
  incremental Zobrist hashing, null-move pruning, LMR, killer moves
  and MVV-LVA ordering, iterative deepening to a fixed node budget
  (85k nodes/move — deterministic, never clock-based)
- Evaluation: **tapered PeSTO** — canonical middlegame/endgame
  piece-square tables for all six piece types with incremental
  MG/EG accumulators and phase interpolation (the tables are stored
  as quantized strings to fit the byte cap), plus pawn structure

Perft-verified on the standard suite (startpos, kiwipete, en-passant
pin, promotion, position 5), including accumulator state-restore
invariants. Round 5 (the PeSTO rewrite) measured, on the make.fun kit
trial protocol: 1654 / 1545 / 1654 Elo across three trials against
the previous version's 1545 / 1364 / 1654, and beat that version
17 wins – 8 losses – 15 draws head-to-head (≈ +80 Elo, 90% lower
bound > 0). The server's own trial of the submitted entry scored
**1680 Elo** (5 wins, 1 draw, 0 losses vs the Sunfish-4K baseline;
90% CI [1513, 1846]).

## Run

`engine.py` is the readable form of the engine; it speaks the
make.fun trial protocol (HTTP against `$MAKEFUN_ENV_URL`). The shipped
competition file is the same source, compressed to fit the 4 KB cap.

MIT licensed.
