# Chantier — Dashboard Destinataire (données consolidées)

## Contexte

Objectif : avoir un dashboard unique pour suivre les données destinataires issues de plusieurs sources.
Approche : itérations successives, une source à la fois.

---

## État au 16 avril 2026

### ✅ Fait

- **Dashboard HTML v1** généré et validé (`outputs/html/dashboard-destinataire-YYYY-MM-DD.html`)
- **Skill installé** : `dashboard-destinataire` — génère le dashboard à la demande en fetchant les données fraîches depuis Qlik
- **Source active** : Qlik — board "KPI SHIFT destinataires" (Delivery analysis_dev)
  - App : `a162cc42-bf4e-4804-969a-0b0e8a261454`
  - Sheet : `84e7e14e-680a-47b6-9eff-414b8243604a`
  - Chart : `dYYhhYL` (table "All indicators")

### 📊 Indicateurs actuellement affichés (données depuis déc. 2025)

- KPI max et moyenne de décalages destinataire / semaine
- Taux de décalage destinataire (% / Nb LAD)
- Temps de décalage moyen (h)
- % de décalages destinataire suivis d'un re-décalage SC
- Ratio décalages destinataire / Robopop
- Ratio décalages destinataire / SC

---

## 🔜 Prochaines itérations

| Priorité | Source | Données à intégrer | Notes |
|----------|--------|-------------------|-------|
| 1 | **Qlik** (autres boards) | À identifier — explorer les sheets disponibles | Boards pertinents à définir avec Yves |
| 2 | **Zendesk** | Tickets destinataires — volume, motifs, délais | Un board Qlik Zendesk existe déjà (`5ddb7d31`) |
| 3 | **Clarity** | Données de tracking comportemental | Pas encore de connecteur disponible |
| 4 | **Base de prod** | Données opérationnelles destinataires | À confirmer l'accès / pertinence |

---

## Références

- Dashboard Qlik Zendesk (déjà dans Qlik) : `5ddb7d31-9b81-49d9-9dc9-ad383bca679b` (space : Sales)
- Skill à modifier pour ajouter une source : suivre la procédure dans `workspace-structure.md`
