data "google_compute_network" "vpc_network" {
  name = "grafana-network"
}

# You can access the existing network using data.google_compute_network.vpc_network
