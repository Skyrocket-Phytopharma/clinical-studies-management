# Clinical studies

Manages list of clinical studies.

---

## Prerequisites

This project uses **uv** for dependency and Python version management. Ensure you have it installed before proceeding.

## Setup

You no longer need to manually manage virtual environments. The setup is now handled through a unified project synchronisation.

1.  **Sync the environment**
    Run the following command to create a lockfile and install all required dependencies (such as Pillow) into a managed environment:

    ```shell
    uv sync
    ```

    This should be carried out after a remote `dependabot` update.

2.  **Updating dependencies**
    If you need to add new packages, use the `add` command instead of editing requirements files manually:
    ```shell
    uv add requests
    ```

## Running

- `uv run process.py`
