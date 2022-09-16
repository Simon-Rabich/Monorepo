#!/usr/bin/env python3

# import sys

# print("Starting prepare-commit-msg.py hook")
#
# sys.exit(0)
"""
Git hook to automatically prefix a git commit message with an issue number
(e.g. Jira ticket number) from the current branch name.
"""
import re
import sys
from subprocess import check_output


commit_msg_filepath = sys.argv[1]
branch = (
    check_output(["git", "symbolic-ref", "--short", "HEAD"]).decode("utf-8").strip()
)
regex = r"(chore|feature|fix|hotfix)\/(\w+-\d+)"

if re.match(regex, branch):
    issue_number = re.match(regex, branch).group(2)
    with open(commit_msg_filepath, "r+") as f:
        commit_msg = f.read()
        f.seek(0, 0)  # correctly positions issue_number when writing commit message
        f.write(f"[{issue_number}] {commit_msg}")