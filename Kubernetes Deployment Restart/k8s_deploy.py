from kubernetes import client, config
from datetime import datetime

# Load kubeconfig
config.load_kube_config()  # Or use load_incluster_config() if running inside cluster
api = client.AppsV1Api()

DEPLOYMENT_NAME = "myapp"
NAMESPACE = "default"

try:
    # Patch deployment to trigger restart
    patch_body = {
        "spec": {
            "template": {
                "metadata": {
                    "annotations": {
                        "kubectl.kubernetes.io/restartedAt": datetime.utcnow().isoformat() + "Z"
                    }
                }
            }
        }
    }

    api.patch_namespaced_deployment(
        name=DEPLOYMENT_NAME,
        namespace=NAMESPACE,
        body=patch_body
    )
    print(f"Deployment '{DEPLOYMENT_NAME}' in namespace '{NAMESPACE}' restarted successfully!")

except client.exceptions.ApiException as e:
    print(f"Failed to restart deployment: {e}")
