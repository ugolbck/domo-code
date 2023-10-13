"""This module handles the parsing of the JSON config file for any domo command."""

import os
import subprocess
from pathlib import Path
from typing import Any, Dict



def handle_vscode_repos(root: Path, repos: Dict[str, Any]) -> None:
    """Build full path for every repo and open it in vscode."""
    for repo, path in repos.items():
        repo_path = os.path.join(root, path)
        print(f'Opening {repo} in vscode from path {repo_path}')
        subprocess.run(['code', str(repo_path)])



def parse_start(data: Dict[str, Any]) -> None:
    """
    Parse the JSON config file for domo start command.

    The idea is to parse the config file into a list of sync/async actions to perform.
    Each step has a priority, and some steps are required.
    For instance, the absence of the 'root' step will cause the command to fail.

    In the future, it should be possible to give options to the command and assess them here.
    """
    
    # Get root project path and verify that it exists
    root = data.get('root')
    if not root:
        raise ValueError('No root project path given. Please add a "root" key to your config file.')
    if not Path(root).exists():
        raise ValueError('Root project path does not exist.')
    
    # Get data for "start" action, or raise error if not present
    start_data = data.get('start')
    if not start_data:
        raise ValueError('No start action given. Please add a "start" key to your config file.')

    # Parse and execute every action
    vscode_actions = start_data.get('vscode')
    print(vscode_actions)
    if vscode_actions:
        handle_vscode_repos(root, vscode_actions)

    run_actions = start_data.get('run')
    if run_actions:
        pass