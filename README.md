# Tiny Chess — a chess engine in 4 KB of Python

A complete, deterministic chess engine squeezed into a single
**4,046-byte** Python file (the competition entry packs this readable
source with lzma + base85; what you see here is the exact logic that
plays).

## What's inside

- 0x88 board representation
- Negamax alpha-beta search with quiescence (captures + check evasions)
- Transposition table with incremental Zobrist hashing
- Null-move pruning, MVV-LVA move ordering, iterative deepening to a
  fixed node budget (85k nodes/move — deterministic, never clock-based)
- History heuristic + killer moves, piece lists, persistent TT with
  TT-move ordering
- Evaluation: material, piece-square tables, pawn structure, bishop
  pair, king-safety/endgame blend by game phase

Perft-verified on the standard suite (startpos, kiwipete, en-passant
pin, promotion, position 5). On the make.fun kit trial protocol it
scores ≈ 1545 Elo, and beat the previous version of this engine
23 wins – 1 loss – 13 draws in a 37-game head-to-head.

## Run

`engine.py` is the readable form of the engine; it speaks the
make.fun trial protocol (HTTP against `$MAKEFUN_ENV_URL`). The shipped
competition file is the same source, compressed to fit the 4 KB cap.

MIT licensed.
