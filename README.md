# Clinical studies

Manages list of clinical studies.

- Create a virtual environment and activate it:

  ```shell
  uv venv .venv
  source .venv/bin/activate  # (MacOS)
  .venv\Scripts\Activate  # (Windows)
  ```

- Install the required packages:

  ```shell
  pip install -r requirements.txt
  ```

- Copy the `env.sample` file to `.env` and then populate with required environment variables.

## Package update

- `./update.sh`

## Running

- `python process.py`
