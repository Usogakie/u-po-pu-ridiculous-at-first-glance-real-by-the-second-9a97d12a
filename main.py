"""One-sentence startup pitch for make.fun.

The program writes a single fixed pitch sentence to entry.txt inside
the output directory. It is fully deterministic: no network, no clock,
no randomness, and it writes nowhere except the output directory.
"""

import os

PITCH = (
    "We lease retired grandmothers to lonely professionals for Sunday "
    "dinner: $60 buys home cooking, unsolicited advice, and a hug \u2014 "
    "and the grandmothers earn more than their pensions."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
