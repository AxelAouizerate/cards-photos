#!/usr/bin/env python3
"""
Echange recto/verso pour la liste d'IDs ci-dessous, dans le dossier courant.
Gere les 4 conventions de nommage : NNN_1.jpg, NNN_01.jpeg, NNN_2.jpg, NNN_02.jpeg.
Utilise un fichier temporaire pour eviter la collision pendant le swap.

Usage :
    cd photos/
    python swap_recto_verso.py
"""

from pathlib import Path

# IDs des cartes a swapper (recto <-> verso). Edite cette liste si besoin.
IDS = [
    60, 121, 246, 305, 308, 310, 318, 319, 322, 326, 327, 415, 442, 454, 511,
    542, 549, 633, 637, 648, 649, 686, 867, 883, 887, 888, 889, 892, 894, 896,
    897, 899, 903,
]


def find_photo(cid: int, slot: int) -> Path | None:
    """Cherche NNN_{slot}.{jpg|jpeg} ou NNN_0{slot}.{jpg|jpeg}."""
    pid = f"{cid:03d}"
    for name in (f"{pid}_{slot}.jpg",
                 f"{pid}_0{slot}.jpeg",
                 f"{pid}_{slot}.jpeg",
                 f"{pid}_0{slot}.jpg"):
        p = Path(name)
        if p.exists(): return p
    return None


def swap(cid: int) -> str:
    p1 = find_photo(cid, 1)
    p2 = find_photo(cid, 2)
    if not p1 and not p2:
        return f"  {cid:>4}  [skip] aucun fichier trouve"
    if not p1: return f"  {cid:>4}  [skip] {cid:03d}_1.* manquant"
    if not p2: return f"  {cid:>4}  [skip] {cid:03d}_2.* manquant"
    tmp = Path(f"{cid:03d}_tmp{p1.suffix}")
    if tmp.exists(): tmp.unlink()
    # Echange noms + extensions (au cas ou recto et verso ont des ext differentes)
    new1 = p1.with_name(p2.name)   # nom de p2
    new2 = p2.with_name(p1.name)   # nom de p1
    p1.rename(tmp)
    p2.rename(new2)
    tmp.rename(new1)
    return f"  {cid:>4}  OK  ({p1.name} <-> {p2.name})"


def main():
    print(f"Swap recto/verso sur {len(set(IDS))} cartes\n")
    ok = skip = 0
    for cid in sorted(set(IDS)):
        msg = swap(cid)
        print(msg)
        if "OK" in msg: ok += 1
        else: skip += 1
    print(f"\n{ok} swapped, {skip} skipped.")


if __name__ == "__main__":
    main()
