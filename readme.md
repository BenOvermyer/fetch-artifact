# Fetch Artifact

Fetches a build artifact from CircleCI.

Dependency: Requests

```
pip install requests
```

## Arguments:

* `-b`, `--branch` The project branch (defaults to master)
* `-p`, `--project` The project to pull from
* `-u`, `--user` The CircleCI username to check under
* `-t`, `--token` Your CircleCI API token
* `-v`, `--vcs` The VCS to use (either github, which is the default, or bitbucket)
