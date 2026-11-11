# Day 2 Git Troubleshooting --- Stash, Pull, and Merge Conflict

## What happened? (Simple explanation)

I was working on the `function-2` branch. I had local changes that I did
not want to lose, so I saved them temporarily using Git stash.

After getting updates from GitHub, I tried to bring my saved changes
back. Git found that the same Python file had changed in more than one
place. It could not automatically combine the changes, so it reported a
merge conflict.

The file involved was:

`day 2/Disk Usage Monitoring Automation.py`

The good news: the committed version of the Python file was still
available in Git history, and Git kept the stash entries because
`git stash pop` did not finish successfully.

------------------------------------------------------------------------

## Errors faced and what they mean

### 1. `git pull` refused to overwrite local changes

**Error seen**

``` text
error: Your local changes to the following files would be overwritten by merge
```

**Layman's explanation**

Git was trying to download and apply the latest changes from GitHub. But
I also had my own uncommitted edits in the same file. Git stopped
because pulling could overwrite my work.

**Command used to investigate**

``` powershell
git stash list
```

**What it does**

Shows the changes that were saved temporarily with Git stash.

**Lesson**

Before pulling, either commit your work or stash it if you need to keep
it temporarily. Do not discard local changes unless you are sure you no
longer need them.

------------------------------------------------------------------------

### 2. Branch name typo

**Error seen earlier**

``` text
fatal: invalid reference: funtion-2
```

**Layman's explanation**

I typed `funtion-2`, but the actual branch name was `function-2`. Git
could not find a branch with the misspelled name.

**Commands used**

``` powershell
git branch
git switch function-2
```

**What they do**

-   `git branch` lists local branches and marks the current branch with
    `*`.
-   `git switch function-2` moves to the existing `function-2` branch.

**Lesson**

Check the exact branch name before switching. A typo can make Git report
that the branch does not exist.

------------------------------------------------------------------------

### 3. Git would not delete a branch because a worktree was using it

**Error seen earlier**

``` text
error: cannot delete branch 'function1' used by worktree
```

**Layman's explanation**

A worktree is another working folder connected to the same Git
repository. Git would not delete `function1` while that worktree was
still using it.

**Useful commands**

``` powershell
git worktree list
git branch
```

**What they do**

-   `git worktree list` shows the working folders attached to the
    repository.
-   `git branch` shows local branches.

**Lesson**

Switch away from a branch in the worktree that is using it, or safely
remove that worktree if it is no longer needed. Do not force-delete a
branch without checking where it is being used.

------------------------------------------------------------------------

### 4. `git stash pop` caused a merge conflict

**Command used**

``` powershell
git stash pop
```

**Error seen**

``` text
Auto-merging day 2/Disk Usage Monitoring Automation.py
CONFLICT (content): Merge conflict in day 2/Disk Usage Monitoring Automation.py
```

**Layman's explanation**

`git stash pop` tried to put my saved edits back into the project. The
same file had also changed in the current branch. Git could not decide
which lines to keep, so it asked me to resolve the conflict.

**Important message**

``` text
The stash entry is kept in case you need it again.
```

This means the stash was not removed. Git keeps it so the saved changes
can still be inspected or recovered.

**Commands used to inspect the situation**

``` powershell
git status
git stash list
```

**What they do**

-   `git status` tells which branch I am on and whether files are
    modified, staged, or conflicted.
-   `git stash list` shows saved stashes.

**Lesson**

When `git stash pop` reports a conflict, do not run `git stash pop`
again. Inspect the file, resolve the conflict, and verify the result
first.

------------------------------------------------------------------------

### 5. VS Code command opened, but did not show terminal output

**Command used**

``` powershell
code "day 2/Disk Usage Monitoring Automation.py"
```

**Layman's explanation**

This command asks Visual Studio Code to open the file. It is normal for
the terminal not to print the file contents. The file should open in the
editor.

**Lesson**

Use the editor to inspect conflict markers such as:

``` text
<<<<<<<
=======
>>>>>>>
```

Remove the markers only after deciding which code should remain.

------------------------------------------------------------------------

### 6. `git add` failed because I used the wrong relative path

**Command that failed**

``` powershell
git add "day 2/Disk Usage Monitoring Automation.py"
```

**Error seen**

``` text
warning: could not open directory 'Day 2/day 2/': No such file or directory
fatal: pathspec 'day 2/Disk Usage Monitoring Automation.py' did not match any files
```

**Layman's explanation**

My terminal was already inside the `Day 2` folder. I typed a path that
included `day 2` again, so Git looked for a folder inside the current
folder that did not exist.

The file was shown by Git as:

``` text
../day 2/Disk Usage Monitoring Automation.py
```

**Correct path from inside the `Day 2` folder**

``` powershell
git add "..\day 2\Disk Usage Monitoring Automation.py"
```

**Alternative**

Move to the repository root first:

``` powershell
cd ..
git add "day 2/Disk Usage Monitoring Automation.py"
```

**Lesson**

A relative path starts from the folder where the terminal is currently
located. Check your location with:

``` powershell
pwd
```

------------------------------------------------------------------------

### 7. The staged changes showed that code was being deleted

**Commands used**

``` powershell
git diff --cached --check
git diff --cached --stat
git diff --cached
```

**Output summary**

``` text
1 file changed, 1 insertion(+), 20 deletions(-)
```

**Layman's explanation**

Git was showing that the version prepared for the next commit had
removed 20 lines and added only 1. That was a warning sign because I did
not intend to delete the Python implementation.

**What the commands do**

-   `git diff --cached --check` checks staged changes for whitespace
    problems.
-   `git diff --cached --stat` gives a short summary of staged changes.
-   `git diff --cached` shows the exact staged changes.

**Lesson**

Always inspect staged changes before committing. If you see unexpected
deletions, stop and investigate. Do not commit blindly.

------------------------------------------------------------------------

### 8. Inspecting the stash showed the saved change

**Command used**

``` powershell
git stash show -p "stash@{0}"
```

**Output included**

``` diff
-import shutil
```

**Layman's explanation**

This showed the difference stored in the most recent stash. The minus
sign means that line was removed in the stashed version compared with
the version Git used for the comparison.

**Useful commands**

``` powershell
git stash list
git stash show -p "stash@{0}"
git stash show -p "stash@{1}"
```

**Lesson**

A stash is a saved set of changes, not necessarily a complete backup of
the entire project. Inspect it before applying or deleting it.

------------------------------------------------------------------------

### 9. Checking the current file and committed version

**Commands used**

``` powershell
Get-Content "..\day 2\Disk Usage Monitoring Automation.py"
git --no-pager show "HEAD:day 2/Disk Usage Monitoring Automation.py"
```

**Layman's explanation**

-   `Get-Content` displays the file currently on disk.
-   `git show HEAD:path` displays the version of that file in the latest
    commit.

The current file displayed only the initial setup and `import shutil`.
The committed version in `HEAD` contained the `check_disk_usage()`
function and its function call.

**Important discovery**

The committed version was safe in Git history. This meant I could use it
as the recovery source instead of guessing or rewriting the code.

------------------------------------------------------------------------

## Safe recovery and completion steps

At the last check, the committed `HEAD` version contained the Day 2
implementation. The following recovery command was recommended, but it
must be run and verified before considering the recovery complete.

### Step 1 --- Confirm you are in the repository root

``` powershell
cd "C:\Users\vijay\30 Day python"
pwd
```

### Step 2 --- Restore the committed file

Only do this after confirming that the committed `HEAD` version is the
version you want to keep:

``` powershell
git restore --source=HEAD --staged --worktree -- "day 2/Disk Usage Monitoring Automation.py"
```

This restores the file in both the staging area and working folder from
the current commit. It does not delete the stash entries.

### Step 3 --- Verify the file and Git status

``` powershell
Get-Content "day 2/Disk Usage Monitoring Automation.py"
git status
git diff --check
git stash list
```

Confirm that the Python function is present and that there are no
unresolved conflicts.

### Step 4 --- Stage and commit only after verification

If the restored file is correct and there are changes to commit:

``` powershell
git add "day 2/Disk Usage Monitoring Automation.py"
git diff --cached --check
git diff --cached
git commit -m "Resolve Day 2 disk monitoring conflict"
```

If Git says there is nothing to commit, do not create an unnecessary
commit.

### Step 5 --- Push the branch to GitHub

First confirm the branch:

``` powershell
git branch --show-current
```

If it prints `function-2`, push it with:

``` powershell
git push -u origin function-2
```

The `-u` option links the local branch to the remote branch, making
future pushes easier.

### Step 6 --- Keep the stash until everything is verified

``` powershell
git stash list
```

After confirming that the committed and pushed code contains everything
needed, a stash can be removed with:

``` powershell
git stash drop "stash@{0}"
```

**Caution:** Do not run the drop command until you have verified the
code on GitHub and confirmed that the stash contains nothing else you
need. The stash index can change after dropping an entry, so inspect
`git stash list` again before removing another stash.

------------------------------------------------------------------------

## Git commands learned

  -----------------------------------------------------------------------
  Command                             Simple meaning
  ----------------------------------- -----------------------------------
  `git branch`                        List branches

  `git switch branch-name`            Move to another branch

  `git status`                        Check what is happening in the
                                      repository

  `git stash`                         Temporarily save local changes

  `git stash list`                    List saved stashes

  `git stash pop`                     Apply a stash and remove it if
                                      successful

  `git stash apply`                   Apply a stash but keep it saved

  `git stash show -p`                 Inspect the changes inside a stash

  `git pull origin main`              Download and integrate updates from
                                      remote `main`

  `git diff --cached`                 Inspect staged changes

  `git diff --cached --stat`          Summarize staged changes

  `git diff --check`                  Check for whitespace errors

  `git add`                           Stage changes for a commit

  `git commit`                        Save a snapshot in local Git
                                      history

  `git show HEAD:path`                Display a file from the latest
                                      commit

  `git restore`                       Restore a file from a chosen
                                      version

  `git push -u origin branch-name`    Push a branch and set its upstream

  `git stash drop`                    Delete a saved stash
  -----------------------------------------------------------------------

## What I learned

1.  Save or commit local work before pulling updates.
2.  Check the current branch and folder before running Git commands.
3.  A merge conflict means Git needs help choosing how two sets of
    changes should be combined.
4.  Never commit without reviewing `git diff --cached`.
5.  A failed `git stash pop` can leave the stash available.
6.  Git history can help recover a previously committed file.
7.  Verify the code and GitHub push before deleting any backup stash.

## Final status checklist

-   [ ] The Python file contains the intended Day 2 implementation.
-   [ ] `git status` shows no unresolved conflicts.
-   [ ] The staged diff contains only intended changes.
-   [ ] The changes are committed, if a commit is needed.
-   [ ] The `function-2` branch is pushed to GitHub.
-   [ ] The stash entries are checked before any deletion.
