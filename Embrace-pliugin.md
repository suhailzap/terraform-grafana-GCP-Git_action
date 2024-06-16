
![icon]( https://embrace.io/docs/images/grafana_embrace_logo.png )


# Installing the Embrace.io Metric Plugin for Grafana

Follow these steps to download and install the Embrace.io Metric Plugin for Grafana in your Docker container:

### Step 1: Download the Plugin

First, download the plugin to a temporary directory where you have write permissions. Use the `docker exec` command to run these commands inside your Grafana container.

```bash
docker exec -it grafana_container_name bash -c "curl -L -o /tmp/embraceio-metric-app-1.2.0.zip https://github.com/embrace-io/grafana-metric-plugin/releases/download/1.2.0/embraceio-metric-app-1.2.0.zip"
```

### Step 2: Move the Plugin to the Grafana Plugins Directory

Move the downloaded plugin file to the Grafana plugins directory:

```bash
docker exec -it grafana_container_name bash -c "mv /tmp/embraceio-metric-app-1.2.0.zip /var/lib/grafana/plugins/"
```

### Step 3: Navigate to the Plugins Directory

Change to the Grafana plugins directory:

```bash
docker exec -it grafana_container_name bash -c "cd /var/lib/grafana/plugins/"
```

### Step 4: Unzip the Plugin

Unzip the plugin file:

```bash
docker exec -it grafana_container_name bash -c "unzip /var/lib/grafana/plugins/embraceio-metric-app-1.2.0.zip"
```

### Step 5: Restart Grafana

Finally, restart the Grafana container to load the new plugin:

```bash
# Restart the Grafana container (run this on the host machine)
sudo docker restart grafana_container_name
```

---

By following these steps, you will successfully install the Embrace.io Metric Plugin for Grafana and have it ready for use in your dashboard.

### Additional Information

- Ensure you have the necessary permissions to move files to the Grafana plugins directory.
- You may need to adjust paths based on your specific Docker container setup.
- Restarting Grafana ensures that the plugin is correctly loaded and ready for use.

For more information, refer to the [Grafana documentation](https://grafana.com/docs/grafana/latest/plugins/installation/) and the [Embrace.io Metric Plugin GitHub page](https://github.com/embrace-io/grafana-metric-plugin).

---

