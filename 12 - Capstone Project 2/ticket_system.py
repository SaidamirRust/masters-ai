from github import Github
import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")       # GitHub personal access token
GITHUB_REPO = os.getenv("GITHUB_REPO")         # e.g., "username/linux-support-tickets"

def create_github_issue(title: str, body: str) -> str:
    """Create a GitHub issue and return its URL."""
    gh = Github(GITHUB_TOKEN)
    repo = gh.get_repo(GITHUB_REPO)
    issue = repo.create_issue(title=title, body=body)
    return issue.html_url