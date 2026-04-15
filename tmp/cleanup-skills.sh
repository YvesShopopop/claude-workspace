#!/bin/bash
# cleanup-skills.sh
# Supprime les fichiers .skill temporaires dans tmp/ si le skill correspondant
# est déjà installé et plus récent que le fichier temporaire.
#
# Usage : bash cleanup-skills.sh
# Appelé automatiquement au début de tout travail sur les skills.

# Détection automatique du répertoire workspace (parent de ce script)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"

# Répertoire des skills installés par Cowork
SKILLS_INSTALL_DIR="$(dirname "$WORKSPACE_DIR")/.claude/skills"

TMP_DIR="$SCRIPT_DIR"

echo "=== Nettoyage des skills temporaires ==="
echo "tmp/        : $TMP_DIR"
echo "skills      : $SKILLS_INSTALL_DIR"
echo ""

found=0
deleted=0
kept=0

for skill_file in "$TMP_DIR"/*.skill; do
    [ -f "$skill_file" ] || continue
    found=$((found + 1))

    skill_name=$(basename "$skill_file" .skill)
    installed_skill_dir="$SKILLS_INSTALL_DIR/$skill_name"

    if [ ! -d "$installed_skill_dir" ]; then
        echo "⚠️  $skill_name.skill — skill non trouvé dans .claude/skills/, conservé"
        kept=$((kept + 1))
        continue
    fi

    # Timestamp du fichier .skill temporaire
    tmp_mtime=$(stat -c %Y "$skill_file" 2>/dev/null)

    # Timestamp du skill installé (SKILL.md ou le dossier lui-même)
    installed_mtime=$(stat -c %Y "$installed_skill_dir/SKILL.md" 2>/dev/null \
                   || stat -c %Y "$installed_skill_dir" 2>/dev/null)

    if [ -z "$tmp_mtime" ] || [ -z "$installed_mtime" ]; then
        echo "⚠️  $skill_name.skill — impossible de lire les dates, conservé"
        kept=$((kept + 1))
        continue
    fi

    if [ "$installed_mtime" -gt "$tmp_mtime" ]; then
        rm "$skill_file"
        echo "🗑️  $skill_name.skill supprimé (skill installé plus récent)"
        deleted=$((deleted + 1))
    else
        echo "⏳ $skill_name.skill conservé (pas encore installé ou plus récent que le skill actuel)"
        kept=$((kept + 1))
    fi
done

if [ "$found" -eq 0 ]; then
    echo "Aucun fichier .skill trouvé dans tmp/ — rien à faire."
fi

echo ""
echo "=== Résultat : $deleted supprimé(s), $kept conservé(s) ==="
