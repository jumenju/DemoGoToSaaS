# Go to SaaS — Démonstration

Site de démonstration utilisé lors de l'atelier de formation GoTo SaaS.  
Le changelog du site se met à jour automatiquement à chaque contribution mergée.

**Site en ligne :** https://jumenju.github.io/DemoGoToSaaS/

---

## Comment contribuer

### 1. Forker le dépôt

Cliquez sur le bouton **Fork** en haut à droite de cette page.  
Cela crée une copie personnelle du dépôt sur votre compte GitHub.

### 2. Cloner votre fork en local

```bash
git clone https://github.com/VOTRE-PSEUDO/DemoGoToSaaS.git
cd DemoGoToSaaS
```

### 3. Créer une branche pour votre modification

Chaque contribution doit être faite sur une branche dédiée, jamais directement sur `main`.

```bash
git checkout -b ma-contribution
```

Choisissez un nom de branche explicite, par exemple : `ajout-section-contact`, `fix-couleur-header`.

### 4. Faire vos modifications

Éditez les fichiers souhaités (principalement `index.html`).

### 5. Commiter vos changements

```bash
git add .
git commit -m "Description courte et claire de la modification"
```

Un bon message de commit répond à la question : *"Qu'est-ce que ce commit apporte ?"*  
Exemples : `Ajoute une section À propos`, `Corrige la couleur du titre`.

### 6. Pousser la branche sur GitHub

```bash
git push origin ma-contribution
```

### 7. Ouvrir une Pull Request

1. Rendez-vous sur votre fork sur GitHub
2. Cliquez sur **Compare & pull request**
3. Remplissez le titre et la description de votre PR
4. Cliquez sur **Create pull request**

Votre contribution sera relue avant d'être intégrée. Une fois mergée, elle apparaîtra automatiquement dans le changelog du site.

---

## Règles de contribution

- Une PR = une modification ciblée (ne mélangez pas plusieurs changements indépendants)
- Le titre de la PR doit être en français et décrire clairement le changement
- Ne modifiez pas le script de chargement du changelog (`loadChangelog`)
- Respectez la structure HTML existante

---

## Structure du projet

```
DemoGoToSaaS/
└── index.html   # Page unique du site
```

---

## Technologies utilisées

| Outil | Usage |
|---|---|
| GitHub Pages | Hébergement du site |
| GitHub API | Chargement dynamique du changelog |
| Bootstrap 5 | Mise en page et styles (via Cloudflare cdnjs) |
