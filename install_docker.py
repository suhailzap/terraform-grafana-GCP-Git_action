import subprocess
import sys

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True, stdout=sys.stdout, stderr=sys.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running command: {command}")
        print(f"Error message: {e}")
        sys.exit(1)

def main():
    # Update package index
    run_command("sudo apt-get update")
    
    # Install packages to allow apt to use a repository over HTTPS and wget
    packages = [
        "apt-transport-https",
        "ca-certificates",
        "curl",
        "gnupg",
        "lsb-release",
        "wget"  # Add wget to the list of packages to install
    ]
    install_command = f"sudo apt-get install -y {' '.join(packages)}"
    run_command(install_command)
    
    # Add Docker’s official GPG key
    run_command("curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg")
    
    # Set up stable repository
    ubuntu_codename = subprocess.run(["lsb_release", "-cs"], capture_output=True, text=True).stdout.strip()
    docker_repo_command = f"echo 'deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu {ubuntu_codename} stable' | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null"
    run_command(docker_repo_command)
    
    # Install Docker Engine
    run_command("sudo apt-get update")
    docker_install_command = "sudo apt-get install -y docker-ce docker-ce-cli containerd.io"
    run_command(docker_install_command)
    
    # Install Docker Compose
    install_compose_command = "sudo wget -O /usr/local/bin/docker-compose https://github.com/docker/compose/releases/download/v2.27.1/docker-compose-Linux-x86_64"
    run_command(install_compose_command)
    run_command("sudo chmod +x /usr/local/bin/docker-compose")
    
    # Verify Docker and Docker Compose installation
    run_command("docker --version")
    run_command("docker-compose --version")

if __name__ == "__main__":
    main()
