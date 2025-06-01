import os
import subprocess
import requests
import json
import argparse
from datetime import datetime

ARCHIVE_DIR = "Repos_Archive"

def create_archive_dir(path):
    """Create the archive directory if it doesn't exist.

    Args:
        path (str): The path to the archive directory.
    """
    os.makedirs(path, exist_ok=True)

def fetch_repositories(username, token=None):
    """Fetch public or private GitHub repositories for a user.

    Args:
        username (str): GitHub username.
        token (str, optional): GitHub token for private repositories.

    Returns:
        list: A list of repository metadata dictionaries.
    """
    headers = {'Authorization': f'token {token}'} if token else {}
    page = 1
    repos = []

    while True:
        if token:
            url = (
                f"https://api.github.com/user/repos?per_page=100"
                f"&page={page}&affiliation=owner"
            )
        else:
            url = (
                f"https://api.github.com/users/{username}/repos?"
                f"per_page=100&page={page}"
            )

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Error connecting to GitHub: {response.status_code}")
            break

        data = response.json()
        if not data:
            break

        repos.extend(data)
        page += 1

    return repos

def archive_repository(repo, archive_dir):
    """Clone a GitHub repository and store metadata.

    Args:
        repo (dict): Metadata of the GitHub repository.
        archive_dir (str): Base directory for archiving.
    """
    name = repo['name']
    clone_url = repo['clone_url']
    description = repo.get('description', '')
    language = repo.get('language', 'Unknown')
    created_at = repo.get('created_at', '')
    html_url = repo['html_url']

    repo_path = os.path.join(archive_dir, language or "Other", name)
    os.makedirs(repo_path, exist_ok=True)

    if not os.path.exists(os.path.join(repo_path, ".git")):
        print(f"Cloning {name}...")
        subprocess.run(["git", "clone", clone_url, repo_path])

    info = {
        "name": name,
        "description": description,
        "language": language,
        "created_at": created_at,
        "archived_at": datetime.now().strftime("%Y-%m-%d"),
        "github": html_url
    }

    with open(os.path.join(repo_path, "info.json"), "w", encoding="utf-8") as f:
        json.dump(info, f, indent=4, ensure_ascii=False)

def main():
    """Main function to handle argument parsing and archiving process."""
    parser = argparse.ArgumentParser(
        description="Archive GitHub repositories (public and private)."
    )
    parser.add_argument("username", help="GitHub username")
    parser.add_argument(
        "--token",
        help="GitHub token to access private repositories (optional)",
        default=None
    )
    args = parser.parse_args()

    github_username = args.username
    github_token = args.token

    print(f"\nStarting repository archiving for user: {github_username}")
    if github_token:
        print("Access to private repositories enabled\n")
    else:
        print("Fetching public repositories only\n")

    create_archive_dir(ARCHIVE_DIR)
    repos = fetch_repositories(github_username, github_token)

    for repo in repos:
        archive_repository(repo, ARCHIVE_DIR)

    print("\nAll repositories have been archived.")

if __name__ == "__main__":
    main()
