# pos_container_deposit_list (Odoo 16)

> **In English —** Shows the `pos_container_deposit` (OCA) fields as optional columns in the product list, to review deposit settings in bulk. Superseded by [product_template_list_extra](https://github.com/benvala-png/product_template_list_extra), which includes these columns; kept for reference.

*Documentation below is in French.*

Petit addon Odoo 16, écrit pour IPELLE, qui expose les champs `is_deposit` et
`deposit_product_id` (ajoutés par `pos_container_deposit`) comme **colonnes
optionnelles** dans la liste des fiches produit — pour pouvoir les voir et les
éditer en masse sans ouvrir chaque fiche une par une.

---

## Fonctionnalités

| Fonctionnalité | Description |
|---|---|
| Colonne « Is Deposit » | Affiche/édite si un produit est un contenant consigné, directement dans la liste |
| Colonne « Deposit Product » | Affiche/édite le produit de consigne associé, directement dans la liste |
| Masquées par défaut | Les deux colonnes n'apparaissent que si on les active via le bouton de colonnes optionnelles (icône en haut à droite de la liste) |

---

## Installation

1. Copier le dossier `pos_container_deposit_list` dans un répertoire présent dans `addons_path`
2. **Dépendance obligatoire : `pos_container_deposit`** — l'installer d'abord (il ajoute les deux champs)
3. Redémarrer Odoo
4. **Apps > Mettre à jour la liste des applications**
5. Rechercher `POS Container Deposit List` et cliquer sur **Installer**

---

## Utilisation

Sur n'importe quelle vue liste de `product.template` (ex. Inventaire >
Produits) : cliquer sur le bouton **colonnes optionnelles** (icône à droite
des en-têtes de colonne) et cocher **Is Deposit** / **Deposit Product**. Les
deux se remplissent directement en ligne, sans ouvrir la fiche.

Utile pour vérifier ou compléter en masse quelles fiches ont leur consigne
liée — au 2026-09-05, seulement 56 fiches sur 2 336 l'ont (voir README de
`pos_container_deposit`).

---

## Structure du module

```
pos_container_deposit_list/
├── __init__.py
├── __manifest__.py
├── README.rst                       # Doc d'origine (anglais), conservée
└── views/
    └── product_template_list.xml    # Les deux colonnes optionnelles
```
