# 🎭 Playwright Python BDD Automation Framework

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Playwright](https://img.shields.io/badge/Playwright-Latest-green.svg)
![Allure Report](https://img.shields.io/badge/Report-Allure-orange.svg)

---

<p align="center">
<a href="#-english-documentation">🇬🇧 English</a> | <a href="#-documentation-en-français">🇫🇷 Français</a>
</p>

---


<a name="-english-documentation"></a>
# 🇬🇧 English

Scalable Test Automation Framework using **Python**, **Playwright**, and **pytest-bdd**. Features a modular **Feature-based POM** structure, **Allure** reporting, and secure `.env` configuration
## 🚀 Prerequisites

Before you begin, ensure you have the following installed:

1.  **Python 3.12** (Recommended stable version).
    * *Note: Python 3.14 (Alpha) is currently not fully supported by Playwright dependencies.*
2.  **Java JDK 8+** (Required only for Allure Report generation).
3.  **Scoop** (Windows only - optional but recommended for installing Allure).

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone [https://github.com/Bout-Gabouz-LeMasle/Playwright-Python.git](https://github.com/Bout-Gabouz-LeMasle/Playwright-Python.git)
cd Playwright-Python
```
### 2. Create and Activate Virtual Environment

***Windows (PowerShell):***
```bash
# Create virtual environment (Force Python 3.12 if you have multiple versions)
py -3.12 -m venv venv


# Activate the environment
.\venv\Scripts\activate
```

**Mac / Linux (Bash):**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers
This command downloads the required browser binaries (Chromium, Firefox, Webkit).
```bash
playwright install
```

## ⚙️ Configuration (.env)
Security is paramount. We use a `.env` file to store sensitive data (credentials). **You must create this file manually** at the project root, as it is ignored by Git for security reasons.

1. Create a file named `.env` in the root folder.
2. Add the following content (replace with your test credentials):

```ini
USER_NAME=standard_user
PASSWORD=secret_sauce
```

## 🖥️ Running Tests
**Run all tests (Headless mode by default)**
```bash
pytest
```

**Run with visible browser (Headed) & Slow motion**
Great for debugging to see what's happening live.
```bash
python -m pytest --headed --slowmo 1000
```

**Run specific feature**
```bash
pytest tests/features/login.feature
```

## 📊 Reporting (Allure)
This framework uses **Allure** for professional reporting.

### 1. Install Allure Commandline (If not installed)
**Windows (via Scoop):**

```bash
# Open PowerShell as Administrator
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex
scoop install allure
```

**Mac (via Homebrew):**
```bash
brew install allure
```

### 2. Generate and View Report
Run the tests with the allure directory option, then serve the results.
```bash
# 1. Run tests and save results to 'allure-results' folder
python -m pytest --headed --alluredir=allure-results

# 2. Generate and open the HTML report in your browser
allure serve allure-results
```

## 📂 Project Structure

```text
Playwright-Python/
├── pages/                 # Page Object Model (Logic & Methods)
│   ├── __init__.py        # Exposes modules
│   ├── base_page.py       # Shared methods (Wrapper)
│   │
│   └── home/              # Home Feature Module
│       ├── __init__.py    # Simplifies imports
│       ├── home_page.py   # Home logic & actions
│       └── home_locators.py # Home selectors
│
├── tests/                 # Tests & Configuration
│   ├── __init__.py        # Test package marker
│   ├── conftest.py        # Pytest Fixtures (Setup/Teardown)
│   ├── test_home_bdd.py   # Step Definitions
│   │
│   └── features/          # Gherkin Feature Files (BDD)
│       └── login.feature  # Login scenarios
│
├── .env                   # Secrets (Ignored by Git)
├── .gitignore             # Files to ignore
├── pytest.ini             # Configuration (Base URL, BDD paths)
├── README.md              # Documentation
└── requirements.txt       # Dependencies list
```

<a name="-documentation-en-français"></a>

# 🇫🇷 Français
Framework d'automatisation de tests évolutif utilisant **Python**, **Playwright** et **pytest-bdd**. Intègre une structure **POM modulaire par fonctionnalité**, des rapports **Allure** et une configuration sécurisée via `.env`.

## 🚀 Prérequis
Avant de commencer, assurez-vous d'avoir installé :

1.  **Python 3.12** (Version stable recommandée).
    * *Note: Python 3.14 (Alpha) n'est pas encore entièrement supporté par certaines dépendances.*
2.  **Java JDK 8+** (Requis uniquement pour la génération du rapport Allure).
3.  **Scoop** (Windows uniquement - optionnel mais recommandé pour installer Allure facilement).

## 🛠️ Installation
### 1. Cloner le dépôt
```bash
git clone [https://github.com/Bout-Gabouz-LeMasle/Playwright-Python.git](https://github.com/Bout-Gabouz-LeMasle/Playwright-Python.git)
cd Playwright-Python
```

### 2. Créer et Activer l'Environnement Virtuel
**Windows (PowerShell) :**
```bash
# Créer l'environnement (Forcer Python 3.12 si plusieurs versions installées)
py -3.12 -m venv venv

# Activer l'environnement
.\venv\Scripts\activate
```

**Mac / Linux :**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```
### 4. Installer les navigateurs Playwright
Cette commande télécharge les binaires des navigateurs (Chromium, Firefox, Webkit).
```bash
playwright install
```

## ⚙️ Configuration (.env)
La sécurité est primordiale. Nous utilisons un fichier `.env` pour stocker les données sensibles (identifiants). **Vous devez créer ce fichier manuellement** à la racine du projet, car il est ignoré par Git.

1. Créez un fichier nommé `.env` à la racine.

2. Ajoutez le contenu suivant (remplacez par vos identifiants de test) :

```ini
USER_NAME=standard_user
PASSWORD=secret_sauce
```

## 🖥️ Lancer les Tests
**Lancer tous les tests (Mode sans tête / Headless par défaut)**
```bash
pytest
```

**Lancer avec navigateur visible (Headed) & Ralenti**
Idéal pour le débogage pour voir l'exécution en temps réel.
```bash
python -m pytest --headed --slowmo 1000
```

**Lancer une fonctionnalité spécifique (Feature)**
```bash
pytest tests/features/login.feature
```

## 📊 Rapports (Allure)
Ce framework utilise **Allure** pour des rapports professionnels et détaillés.

### 1. Installer Allure Commandline (Si pas encore installé)
**Windows (via Scoop) :**
```bash
# Ouvrir PowerShell en tant qu'administrateur
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex
scoop install allure
```

**Mac (via Homebrew) :**
```bash
brew install allure
```

### 2. Générer et Voir le Rapport
Lancez les tests avec l'option `alluredir`, puis servez les résultats.
```bash
# 1. Lancer les tests et sauvegarder les résultats dans le dossier 'allure-results'
python -m pytest --headed --alluredir=allure-results

# 2. Générer et ouvrir le rapport HTML dans le navigateur
allure serve allure-results
```

## 📂 Structure du Projet

```text
Playwright-Python/
├── pages/                 # 📄 Page Object Model (Logic & Methods / Logique & Méthodes)
│   ├── __init__.py        # 🔗 Exposes modules / Expose les modules
│   ├── base_page.py       # 🛠️ Shared methods (Wrapper) / Méthodes partagées
│   │
│   └── home/              # 🏠 Home Feature Module / Module de la page d'accueil
│       ├── __init__.py    # 🔗 Simplifies imports / Simplifie les imports
│       ├── home_page.py   # 🧠 Home logic & actions / Logique & actions de l'accueil
│       └── home_locators.py # 📍 Home selectors / Sélecteurs de l'accueil
│
├── tests/                 # 🧪 Tests & Configuration
│   ├── __init__.py        # 📦 Test package marker / Marqueur du package de test
│   ├── conftest.py        # ⚙️ Pytest Fixtures (Setup/Teardown)
│   ├── test_home_bdd.py   # 🧩 Step Definitions / Définitions des étapes
│   │
│   └── features/          # 🥒 Gherkin Feature Files (BDD)
│       └── login.feature  # 📝 Login scenarios / Scénarios de connexion
│
├── .env                   # 🔒 Secrets (Ignored by Git / Ignoré par Git)
├── .gitignore             # 🙈 Files to ignore / Fichiers à ignorer
├── pytest.ini             # 🛠️ Configuration (Base URL, BDD paths)
├── README.md              # 📖 Documentation
└── requirements.txt       # 📦 Dependencies list / Liste des dépendances
```