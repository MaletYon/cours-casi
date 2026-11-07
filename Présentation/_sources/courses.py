"""Métadonnées du cours CASI (CAS3401, PSSFP) et répartition des 8 journées de 4 heures.

Le cours est donné en 8 journées de 4 heures (32 h au programme) ; les deux
dernières heures du jour 8 sont offertes, soit 30 h effectives. Le jour 8
commence par 2 heures de cas intégrateur en salle.
"""

COURS = r"C:\Users\Thierry MINKA\OneDrive\Documents\COURS"

CASI = {
    "sigle": "CASI",
    "code": "CAS3401",
    "titre": "Contrôle et Audit des Systèmes d'Information",
    "sous_titre": "Évaluer le contrôle interne des finances publiques dans un environnement numérique",
    "master": "Master professionnel en finances · Spécialité Audit et Contrôle · Niveau 5",
    "bandeau": "Université de Yaoundé II",
    "logo_g": "uy2",
    "logo_d": "pssfp",
    "n_jours": 8,
    "heures": 4,
    "annee": "2026-2027",
    "dossier": COURS + r"\PSSFP\CAS3401\Présentation",
    "fil_rouge": "MINÉQUIR, CAPNO, e-RECETTES",
    "parties": [
        ("Prologue", "Le paiement du 28 décembre", "P00"),
        ("Partie I", "Fondements et contrôle interne", "C01–C03"),
        ("Partie II", "Cadre institutionnel et normatif", "C04–C05"),
        ("Partie III", "Démarche de mission", "C06–C08"),
        ("Partie IV", "Domaines d'audit", "C09–C13"),
        ("Partie V", "Synthèse : cas intégrateur", "C14"),
        ("Partie VI", "Ouverture sur la recherche : l'auditologie", "C15"),
    ],
    # jour : (thème court, contenu détaillé, ateliers, labs)
    "jours": {
        1: ("Ouverture · auditer un SI public", "Prologue + C01", ["P00", "C01"], []),
        2: ("Le système de contrôle interne et son évaluation", "C02 + C03", ["C02", "C03"], ["LAB-02"]),
        3: ("Qui contrôle quoi, selon quelles normes", "C04 + C05", ["C04", "C05"], []),
        4: ("La mission, la décomposition · OUI, NON, NEK", "C06 + C07", ["C06", "C07"], ["LAB-01", "LAB-04", "LAB-05"]),
        5: ("Mesurer, conclure, suivre · les accès", "C08 + C09", ["C08", "C09"], ["LAB-10", "LAB-03"]),
        6: ("Exploitation · contrôles d'application", "C10 + C11", ["C10", "C11"], ["LAB-08", "LAB-09"]),
        7: ("Données et fraude · gouvernance et projets", "C12 + C13", ["C12", "C13"], ["LAB-06", "LAB-07"]),
        8: ("Cas intégrateur · ouverture sur la recherche", "C14 + C15", ["C14", "C15"], []),
    },
}

ALL = {"CASI": CASI}
