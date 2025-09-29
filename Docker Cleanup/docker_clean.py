import docker

client = docker.from_env()

try:
    # Remove stopped containers
    containers_result = client.containers.prune()
    print(f"Containers removed: {containers_result.get('ContainersDeleted', [])}")

    # Remove unused images
    images_result = client.images.prune()
    print(f"Images removed: {images_result.get('ImagesDeleted', [])}")

    # Remove unused volumes
    volumes_result = client.volumes.prune()
    print(f"Volumes removed: {volumes_result.get('VolumesDeleted', [])}")

    # Optional: prune networks
    networks_result = client.networks.prune()
    print(f"Networks removed: {networks_result.get('NetworksDeleted', [])}")

    print("Docker cleanup completed successfully!")

except docker.errors.APIError as e:
    print(f"Docker cleanup failed: {e}")
