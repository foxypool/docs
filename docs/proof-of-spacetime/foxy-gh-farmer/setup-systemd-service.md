To run Foxy-GH-Farmer as a systemd service, a template `foxy-gh-farmer.service` file is provided in the [root of the repo](https://github.com/foxypool/foxy-gh-farmer/blob/main/foxy-gh-farmer.service){target=_blank}.

1. Copy the template `foxy-gh-farmer.service` into `/etc/systemd/system/foxy-gh-farmer.service`
2. Modify the `User` and `Group` to your user/group.
3. Modify the path to the `foxy-gh-farmer` binary as well as the path to the `foxy-gh-farmer.yaml` to fit your paths.

    !!! note
        When running from source the binary path is in `venv/bin/`, so for example `/home/user/foxy-gh-farmer/venv/bin/foxy-gh-farmer`.

4. Reload the daemon to detect your new service:
   ```bash
   sudo systemctl daemon-reload
   ```
5. Enable the service to start on boot:
   ```bash
   sudo systemctl enable foxy-gh-farmer.service
   ```
6. Start the service: 
   ```bash
   sudo service foxy-gh-farmer start
   ```


### Using

- The status of the service can be seen via:
  ```bash
  sudo service foxy-gh-farmer status
  ```
- You can stop the service via:
  ```bash
  sudo service foxy-gh-farmer stop
  ```
- You can tail the logs of the service via:
  ```bash
  sudo journalctl -u foxy-gh-farmer.service --follow
  ```
