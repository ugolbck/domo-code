# domo-code
Workspace setup automation to make your day easier.

-------------

### Goals
- A simple command with arguments should load everything necessary to work on a specific project.
- Reliance on a config file and options in order to make it customizable
- I try to make it in Python, but feel free to make it in bash
- Expected support:
    - VSCode
    - Basically any shell command
    - more if I need it


### Usage

Main way of using it should be:

`domo start -f serious-project-conf.json --no-vscode api --no-run logs_redis`

with _serious-project-config.json_ looking like:

```json
{
    "root": "/home/ugo/code/serious-project",
    "start": {
        "vscode": {
            "api": "api",
            "other-repo" : "other-repo"   
        },
        "run": {
            "compose": {
                "cmd": ["./start-services.local.sh"],
                "extra-path": ["api/bin"]
                },
            "logs_redis": {
                "cmd": ["docker", "logs", "-f", "--tail", "50", "redis-cont"],
                "depends": ["compose"],
                "wait": 5
            },
            "logs_api": {
                "cmd": ["docker", "logs", "-f", "--tail", "50", "api-cont"],
                "depends": ["compose"],
                "wait": 5,
                "retries": 2
            }
        }
    }
}
```

Ideally, the command should:
- not open VSCode in the /home/ugo/code/serious-project/api folder (because of no-vscode option)
- open VSCode in the /home/ugo/code/serious-project/other-repo folder
- run `.start-services.local.sh` in the /home/ugo/code/serious-project/api/bin folder
- ignore the `logs_redis` command because of the `--no-run` option
- run the `logs_api` command afterthe `compose` pipeline has been run because of the `depends` option, and after 15 seconds because of the `wait` option. If the command fails, it will be retried 2 times because of the `retry` option, with a 15 seconds wait between each retry.

------

I don't know if it's possible to do it in Python, but I'd like to be able to run the command in a subshell, so that I can keep my current shell open and still be able to use it.
