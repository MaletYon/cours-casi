# Contrôle et Audit des Systèmes d'Information (CASI)

[← Tous les cours de MaletYon](https://github.com/maletyon) · [Livre (PDF)](CASI_main.pdf) · [Présentations](Présentation/) · [Fiches par chapitre](fiches/) · [Corrigés](correction/README.md)

**UE CAS3401** · Programme Supérieur de Spécialisation en Finances Publiques (PSSFP), Université de Yaoundé II · Master professionnel en finances publiques, spécialité Audit et Contrôle, niveau 5 · 8 journées de 4 heures (30 heures effectives)
Auteur : MINKA MI NGUIDJOÏ Thierry Emmanuel, enseignant-chercheur (LIMSI, ENSPY) · contact : maletyon@proton.me · année académique 2026-2027

> *Le contrôle interne ne disparaît pas quand l'administration s'informatise ; il change de place, et l'auditeur doit le suivre.*

Ce cours s'adresse aux auditeurs et aux contrôleurs des finances publiques qui commencent à exercer dans des environnements numériques. Son cœur est le **système de contrôle interne** et son **évaluation** : le décrire, le questionner, le tester, classer ses déficiences, conclure sur son efficacité. La théorie est brève ; la pratique et le métier sont densifiés. Au Cameroun, dans le secteur public, c'est le **Contrôle Supérieur de l'État** qui a la compétence explicite du contrôle des systèmes d'information (décret n° 2013/287 du 4 septembre 2013, art. 2, al. 3) ; l'**ANTIC** conduit les audits de sécurité (loi n° 2010/012) ; la **Chambre des Comptes** s'y retrouve par extension, à travers les comptes que ces systèmes produisent. Trois dossiers fictifs servent de fil rouge : le MINÉQUIR (double paiement), la CAPNO (paie de Garoua) et e-RECETTES (recette des finances de Bafoussam).

## Ce que contient ce dépôt

| Élément | Où | Description |
|---|---|---|
| Le livre du cours | [`CASI_main.pdf`](CASI_main.pdf) | Traité complet (prologue, six parties, 15 chapitres, annexes), compilé depuis [`CASI_main.tex`](CASI_main.tex) |
| Les présentations | [`Présentation/`](Présentation/) | 9 présentations PowerPoint : vision d'ensemble et 8 journées, avec notes du présentateur |
| Les fiches d'exercices | [`fiches/`](fiches/) | 16 fiches de 40 questions au format texte, une par chapitre (prologue compris) |
| Le livret de correction | [`correction/`](correction/) | Accès réservé : voir la page du dossier |
| Les sources LaTeX | `front/`, `partie0/` à `partie5/`, `annexes/`, `bibliographie/`, `figures/`, [`Style_CASI.sty`](Style_CASI.sty) | Sources du livre |

## Organisation du cours (8 journées de 4 heures)

| Jour | Contenu | Chapitres |
|---|---|---|
| J01 | Le paiement du 28 décembre · Contrôler et auditer un SI public | P00, C01 |
| J02 | Le système de contrôle interne · Évaluer le contrôle interne | C02, C03 |
| J03 | Qui contrôle les SI publics au Cameroun · Normes et référentiels | C04, C05 |
| J04 | La mission : principes, préparation, décomposition · Collecter la preuve : OUI, NON, NEK | C06, C07 |
| J05 | Mesurer, conclure, rapporter, suivre · Accès et habilitations | C08, C09 |
| J06 | Changements, exploitation, continuité · Contrôles d'application | C10, C11 |
| J07 | Analyse de données et fraude · Gouvernance, projets, prestataires | C12, C13 |
| J08 | Cas intégrateur et ouverture sur la recherche (2 heures), puis 2 heures offertes | C14, C15 |

Annexes : A. Glossaire · B. Outils · C. Papiers de travail types · D. Textes juridiques et normatifs · E. Bibliographie commentée · F. Contacts. Les fiches et les labs se font hors des heures de cours.

## NDAP SUKULU, la salle de classe compagnon

*Ndap sukulu* signifie « la salle de classe » en bassa, et *Malet Yon* « ton enseignant ». Le code de cours est **CAS3401**.

> **NDAP SUKULU en local.** La version téléchargeable et installable sur votre poste, avec un module autonome pour ce cours, est en cours de finalisation. En attendant, les fiches d'auto-évaluation de chaque chapitre (40 questions) sont fournies au format texte dans [`fiches/`](fiches/).

| Lab | Chapitre | Sujet |
|---|---|---|
| CAS3401-LAB-01 | 6 | Prise de connaissance et risques de SIDÉPENSE |
| CAS3401-LAB-02 | 3 | Évaluer le contrôle interne du MINÉQUIR |
| CAS3401-LAB-03 | 9 | Habilitations de SIDÉPENSE |
| CAS3401-LAB-04 | 7 | Chronologie du double paiement |
| CAS3401-LAB-05 | 7 | Intégrité d'une extraction de paie |
| CAS3401-LAB-06 | 12 | Agents fictifs et doublons dans la paie |
| CAS3401-LAB-07 | 12 | Loi de Benford et fractionnement |
| CAS3401-LAB-08 | 10 | Changements et sauvegardes d'e-RECETTES |
| CAS3401-LAB-09 | 11 | Tester des contrôles d'application |
| CAS3401-LAB-10 | 8 | Rédiger un constat et classer la déficience |

## Compiler le livre

Avec une distribution LaTeX : `pdflatex CASI_main`, `biber CASI_main`, `makeindex CASI_main`, puis deux fois `pdflatex CASI_main`.
Les présentations se régénèrent avec `python Présentation/_sources/gen_specs.py` puis `python Présentation/_sources/run.py CASI all` (Python 3 et python-pptx).

## Recherche

La démarche de mission (Partie III) et le chapitre 15 reposent sur deux prépublications de l'auteur déposées sur HAL : *Vers l'auditologie* (A0, `hal-05701007`) et l'instrument OUI/NON/NEK (A1, `hal-05701270`). Les autres appuis sont des normes et des travaux publiés, listés dans la bibliographie du livre.
