To run Foxy-Farmer as a systemd service, a template `foxy-farmer.service` file is provided in the [root of the repo](https://github.com/foxypool/foxy-farmer/blob/main/foxy-farmer.service){target=_blank}.

1. Copy the template `foxy-farmer.service` into `/etc/systemd/system/foxy-farmer.service`
2. Modify the `User` and `Group` to your user/group.
3. Modify the path to the `foxy-farmer` binary as well as the path to the `foxy-farmer.yaml` to fit your paths.

    !!! note
        When running from source the binary path is in `venv/bin/`, so for example `/home/user/foxy-farmer/venv/bin/foxy-farmer`.

4. Reload the daemon to detect your new service:
   ```bash
   sudo systemctl daemon-reload
   ```
5. Enable the service to start on boot:
   ```bash
   sudo systemctl enable foxy-farmer.service
   ```
6. Start the service: 
   ```bash
   sudo service foxy-farmer start
   ```


### Using

- The status of the service can be seen via:
  ```bash
  sudo service foxy-farmer status
  ```
- You can stop the service via:
  ```bash
  sudo service foxy-farmer stop
  ```
- You can tail the logs of the service via:
  ```bash
  sudo journalctl -u foxy-farmer.service --follow
  ```
