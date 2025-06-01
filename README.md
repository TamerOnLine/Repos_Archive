# Repos_Archive

📦 A simple yet powerful Python script to archive GitHub repositories (public and private), with automatic organization by programming language and metadata generation via `info.json`.

---

## 🚀 Features

- Fetches all **public repositories** for a given GitHub user.
- Optionally fetches **private repositories** using a GitHub Token.
- Clones each repository into a structured folder based on its primary language.
- Generates an `info.json` file with metadata for each project (name, description, language, creation date, etc.).

---

## 🧰 Requirements

- Python 3.7+
- Git installed on your system
- `requests` Python package (`pip install requests`)

---

## ⚙️ Usage

### 🔹 1. Clone the script

```bash
git clone https://github.com/TamerOnLine/Repos_Archive.git
cd Repos_Archive
```

### 🔹 2. Run the script

#### ✅ Archive public repositories only:
```bash
python myarchive.py <github-username>
```

#### 🔐 Archive public + private repositories:
```bash
python myarchive.py <github-username> --token ghp_XXXXXXX
```

> 🔒 Ensure the token has the following scopes: `repo`, `read:org` (if needed).

---

## 🗂️ Output Directory Structure

```
Repos_Archive/
├── Python/
│   └── flask-shop/
│       ├── .git/
│       └── info.json
├── JavaScript/
│   └── react-app/
...
```

---

## 📦 Output Per Project

Each archived repository will include:

- A full clone of the repository
- An `info.json` file like this:

```json
{
  "name": "project-name",
  "description": "short description",
  "language": "Python",
  "created_at": "2023-01-01T00:00:00Z",
  "archived_at": "2025-06-01",
  "github": "https://github.com/username/project-name"
}
```

---

## 📄 License

Apache License 2.0 — see [LICENSE](LICENSE) for full details.

---

## ✨ Future Enhancements (optional)

- Auto-zip each archived repo
- Export metadata to CSV/Excel
- Build a GUI to browse the archive visually

---

## 🙋‍♂️ Contributions

Contributions are welcome! Feel free to fork and submit a pull request.
