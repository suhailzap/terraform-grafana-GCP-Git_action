resource "google_compute_instance" "grafana" {
  name         = "grafana-instance"
  machine_type = "e2-medium"

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2004-lts"  # Update this to your desired Ubuntu version
      size  = 35
    }
  }

  network_interface {
    network       = data.google_compute_network.vpc_network.name
    access_config {
      // Ephemeral public IP
    }
  }


  tags = ["grafana"]

  labels = {
    name        = "grafana_compute_engine"
    description = "grafana_terraform_deployment"
  }
}
