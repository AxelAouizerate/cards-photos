#!/usr/bin/env python3
"""
Echange les noms NNN_1.jpg <-> NNN_2.jpg dans le dossier courant pour la
liste d'IDs ci-dessous. Utilise un fichier temporaire intermediaire pour
eviter la collision pendant le swap.

Usage :
    cd photos/
    python swap_recto_verso.py
"""

from pathlib import Path

# IDs des cartes a swapper (recto <-> verso). Edite cette liste si besoin.
IDS = [
    64,    # Guardian Angel Joan (IOC)
    98, 99, 100,   # Bete Fantome Meca Hamstrat (LTGY) - 3 copies
    121,   # Corne du Paradis (MRD)
    246, 542, 882, # Dragon Yamata (DB2) - 3 copies
    283, 888,      # Seigneur Ancestral Zerato (AST) - 2 copies
    322,   # Le Dragon Aile de Ra (G4)
    326,   # Makyura le Destructeur (DL2)
    327, 915,      # Raigeki (DP22) - 2 copies
    328,   # Obelisk le Tourmenteur (G4)
    442, 449, 510, 549,            # Yubel (PTDN)
    511, 512, 548,                 # Yubel Terreur Incarnee (PTDN)
    454,   # Appel de l'Etre Hante (SDP-F)
    605, 803,      # Magicienne des Tenebres (LART) - 2 copies
    637, 640,      # Loup de Guerre Geno Perverti (STON) - 2 copies
    648,   # Neos Flamboyant Heros Elementaire (POTD)
    686,   # Unity (JUMP)
    867,   # Snatch Steal (MRL)
    887,   # Dandylion (SD8-KRDS1) / Chimeratech Over-Dragon (POTD) - meme id
    899,   # Number 39 Utopia the Envoy of the Light (LOCH-JP)
    903,   # Crimson Dragon Quetzacoatl (LOCR-JP)
    1096,  # Chimeratech Over-Dragon (POTD)
]

def swap(cid: int) -> str:
    """Echange NNN_1.jpg et NNN_2.jpg. Retourne un message d'etat."""
    pid = f"{cid:03d}"
    p1 = Path(f"{pid}_1.jpg")
    p2 = Path(f"{pid}_2.jpg")
    if not p1.exists() and not p2.exists():
        return f"  {cid:>4}  [skip] ni {p1.name} ni {p2.name} trouves"
    if not p1.exists():
        return f"  {cid:>4}  [skip] {p1.name} manquant (rien a swap)"
    if not p2.exists():
        return f"  {cid:>4}  [skip] {p2.name} manquant (rien a swap)"
    tmp = Path(f"{pid}_tmp.jpg")
    if tmp.exists(): tmp.unlink()
    p1.rename(tmp)
    p2.rename(p1)
    tmp.rename(p2)
    return f"  {cid:>4}  OK  ({p1.name} <-> {p2.name})"

def main():
    print(f"Swap recto/verso sur {len(set(IDS))} cartes\n")
    ok = skip = 0
    for cid in sorted(set(IDS)):
        msg = swap(cid)
        print(msg)
        if msg.strip().startswith(f"{cid}  OK"): ok += 1
        else: skip += 1
    print(f"\n{ok} swapped, {skip} skipped.")

if __name__ == "__main__":
    main()
