# Git Troubleshooting – Day 2

## Introduction

During Day 2 of my Python DevOps Automation challenge, I faced several Git errors while working with branches, commits, stashes, and GitHub.

This document explains:
- What errors I faced.
- Why the errors occurred.
- How I resolved them.
- Which Git commands I used.

The explanations are written in simple language for beginners.

---

## 1. Error: Cannot delete a branch

**Command used:**
```bash
git branch -d function1
```

**Error:**
```text
error: cannot delete branch 'function1'
used by worktree
```

**Why did this happen?**

Git does not allow us to delete a branch that is currently being used by another working directory (worktree).

**How did I resolve it?**

I checked the available branches:

```bash
git branch
```

Then I switched to another branch:

```bash
git switch main
```

After confirming that the branch was no longer being used by the worktree, I could delete it safely.

**Important commands:**
```bash
git branch
git worktree list
git switch main
git branch -d function1
```

---

## 2. Error: Invalid branch name

**Command used:**
```bash
git switch funtion-2
```

**Error:**
```text
fatal: invalid reference: funtion-2
```

**Why did this happen?**

I made a spelling mistake. The actual branch name was `function-2`, but I typed `funtion-2`.

**How did I resolve it?**

First, I checked the available branches:

```bash
git branch
```

Then I switched using the correct branch name:

```bash
git switch function-2
```

**Lesson learned:** Always check the branch name before switching.

---

## 3. Error: Branch already exists

**Command used:**
```bash
git checkout -b function-2
```

**Error:**
```text
fatal: a branch named 'function-2' already exists
```

**Why did this happen?**

The `-b` option creates a new branch. But I had already created `function-2`.

**How did I resolve it?**

Instead of creating another branch, I switched to the existing branch:

```bash
git switch function-2
```

**Difference:**

```bash
git checkout -b function-2
```
Creates a new branch.

```bash
git switch function-2
```
Switches to an existing branch.

---

## 4. Error: Local changes would be overwritten by merge

**Command used:**
```bash
git pull origin main
```

**Error:**
```text
error: Your local changes to the following files
would be overwritten by merge
```

**Why did this happen?**

I had made changes to files locally, but GitHub also had changes in the same files.

Git stopped the pull to protect my local work.

**How did I resolve it?**

I used Git stash to temporarily save my changes:

```bash
git stash list
```

I checked the available stashes:

```text
stash@{0}: On function-2: Day 2 local backup
stash@{1}: On main: Day 2 local changes
```

Stash means temporarily keeping your unfinished changes safely.

Useful commands:

```bash
git stash
git stash list
git stash pop
git stash apply
```

**Difference:**

- `git stash pop`: Applies changes and removes the stash entry.
- `git stash apply`: Applies changes but keeps the stash entry.

---

## 5. Error: Non-fast-forward push rejected

**Command used:**
```bash
git push origin main
```

**Error:**
```text
! [rejected] main -> main (non-fast-forward)
```

**Why did this happen?**

My local `main` branch was behind the GitHub `main` branch.

GitHub contained two newer commits that were missing locally.

Git rejected my push to prevent remote changes from being overwritten.

**How did I investigate it?**

```bash
git status
git branch -vv
git fetch origin
```

I found:

```text
function-2 7d149b3 docs: add Day 2 Git troubleshooting guide
main       ad66f8e [origin/main: behind 2] 2nd day push
```

This showed that:
- I was working on `function-2`.
- My local `main` was behind the remote by two commits.
- My documentation was committed on `function-2`.

**How did I resolve it?**

I decided to push my feature branch instead:

```bash
git push -u origin function-2
```

Then I created a Pull Request on GitHub to merge `function-2` into `main`.

**Lesson learned:** Never force push just to bypass a non-fast-forward error. First understand why the branches are different.

---

## 6. Error: Git cannot find the file

**Command used:**
```bash
git add GIT_TROUBLESHOOTING_DAY2.md
```

**Error:**
```text
fatal: pathspec 'GIT_TROUBLESHOOTING_DAY2.md'
did not match any files
```

**Why did this happen?**

Git could not find the specified file in my current directory.

Possible reasons:
- The file was not created.
- The filename was incorrect.
- The file was saved in another folder.

**How did I investigate it?**

```powershell
pwd
dir
```

To search for the file:

```powershell
Get-ChildItem -Recurse -Filter "GIT_TROUBLESHOOTING_DAY2.md"
```

**How did I resolve it?**

If the file did not exist, I created it:

```powershell
New-Item GIT_TROUBLESHOOTING_DAY2.md -ItemType File
```

Then opened it:

```powershell
notepad GIT_TROUBLESHOOTING_DAY2.md
```

After adding and saving the content:

```bash
git add GIT_TROUBLESHOOTING_DAY2.md
```

**Lesson learned:** `git add` stages an existing file. It does not create a file.

---

## 7. Understanding Git reflog

**Command used:**
```bash
git reflog
```

**Why did I use it?**

I wanted to understand my previous branch switches and recover information about earlier Git operations.

**What does it do?**

`git reflog` shows the history of where HEAD was pointing, including previous branch switches and commits.

Example:

```text
HEAD@{0}: checkout: moving from main to function-2
HEAD@{1}: checkout: moving from function1 to main
HEAD@{2}: commit: Day 2 implementation
```

**Useful command:**

```bash
git reflog
```

It is especially helpful when you accidentally switch branches or lose track of a previous commit.

---

## 8. Important Git commands learned

| Command | Purpose |
|---|---|
| `git status` | Check current Git status |
| `git branch` | List local branches |
| `git branch -vv` | Check branch tracking information |
| `git switch main` | Switch to main |
| `git switch -c feature` | Create and switch to a new branch |
| `git stash` | Temporarily save changes |
| `git stash list` | View saved stashes |
| `git stash pop` | Restore and remove a stash |
| `git fetch origin` | Download remote information |
| `git pull origin main` | Download and integrate remote changes |
| `git add filename` | Stage a file |
| `git commit -m "message"` | Save changes in Git history |
| `git push origin branch` | Push commits to GitHub |
| `git reflog` | View recent HEAD history |
| `git log --oneline` | View commit history |

---

## 9. What I learned from Day 2

1. A branch allows us to work on separate features without directly modifying main.
2. Git stash helps protect unfinished local changes.
3. Git fetch and Git pull are different operations.
4. Git prevents accidental overwriting of remote changes.
5. A Pull Request allows us to review code before merging.
6. Always check the current branch before pushing.
7. Always check Git status before performing important operations.

## 10. Professional Git workflow

My recommended workflow for future DevOps projects:

```text
main
  |
  |-- Create feature branch
  |
  |-- Write code
  |
  |-- Test the code
  |
  |-- git add
  |
  |-- git commit
  |
  |-- git push
  |
  |-- Create Pull Request
  |
  |-- Review changes
  |
  |-- Merge into main
```

## Conclusion

During Day 2, I learned how to troubleshoot common Git problems involving branches, stashes, local changes, remote repositories, and Pull Requests.

These practical errors helped me understand how Git works in real-world DevOps development workflows.