resource "google_compute_firewall" "firewall" {
  name    = "allow-http-https"
  network = data.google_compute_network.vpc_network.name

 allow {
    protocol = "tcp"
    ports    = ["22", "80", "443", "3000", "5672", "15672"]
  }

  source_ranges = ["0.0.0.0/0"]
}
