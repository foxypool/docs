=== "Using the binary"

      Just download the latest version of the binary [from here](https://github.com/foxypool/foxy-farmer/releases/latest){target=_blank} like you did on install and replace the existing binary, that's it.

=== "Running from source"

      1. Open a terminal in the `foxy-farmer` directory which you cloned during install.
      2. Run `git pull`
      3. Run `venv/bin/pip install --upgrade .`

=== "Using docker"

      Pull the latest image using `docker pull ghcr.io/foxypool/foxy-farmer:latest` and recreate the container using `docker compose up -d`.
