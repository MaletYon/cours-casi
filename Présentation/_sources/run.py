"""Construit les présentations : python run.py CASI 1 3 5   (ou: python run.py CASI all)."""
import sys, os, importlib.util
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slides import Deck
from courses import ALL

LABS = {
    "CASI": {
        "LAB-01": "Prise de connaissance et risques de SIDÉPENSE",
        "LAB-02": "Évaluer le contrôle interne du MINÉQUIR",
        "LAB-03": "Habilitations de SIDÉPENSE",
        "LAB-04": "Chronologie du double paiement",
        "LAB-05": "Intégrité d'une extraction de paie (CAPNO)",
        "LAB-06": "Agents fictifs et doublons dans la paie (CAPNO)",
        "LAB-07": "Loi de Benford et fractionnement",
        "LAB-08": "Changements et sauvegardes d'e-RECETTES",
        "LAB-09": "Tester des contrôles d'application",
        "LAB-10": "Rédiger un constat et classer la déficience",
    },
}

HERE = os.path.dirname(os.path.abspath(__file__))


def load(sigle, name):
    path = os.path.join(HERE, "specs", sigle, name + ".py")
    spec = importlib.util.spec_from_file_location(f"{sigle}_{name}", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.SPEC


def complete(sigle, day, spec):
    c = ALL[sigle]
    theme, contenu, ateliers, labs = c["jours"][day]
    for d in spec:
        if d["k"] == "maison":
            d.setdefault("ateliers", [f"**Atelier {a}** : fiche CAS3401-FICHE-{a}" for a in ateliers])
            d.setdefault("labs", [f"**CAS3401-{l}** : {LABS[sigle][l]}" for l in labs])
    return spec


def build_day(sigle, day):
    c = ALL[sigle]
    spec = complete(sigle, day, load(sigle, f"J{day:02d}"))
    deck = Deck(c, day)
    out = os.path.join(c["dossier"], f"{sigle}_J{day:02d}.pptx")
    n = deck.build(spec, out)
    print(f"{out}  ({n} diapositives)")


def build_global(sigle):
    c = ALL[sigle]
    spec = load(sigle, "J00")
    deck = Deck(c, None)
    out = os.path.join(c["dossier"], f"{sigle}_00_vision_globale.pptx")
    n = deck.build(spec, out)
    print(f"{out}  ({n} diapositives)")


if __name__ == "__main__":
    sigle = sys.argv[1]
    days = sys.argv[2:]
    if days == ["all"]:
        days = ["0"] + [str(i) for i in range(1, ALL[sigle].get("n_jours", 15) + 1)]
    for dd in days:
        if int(dd) == 0:
            build_global(sigle)
        else:
            build_day(sigle, int(dd))
