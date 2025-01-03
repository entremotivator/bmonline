import requests

DEFAULT_API_URL = "https://theaisource-u29564.vm.elestio.app:57987"
DEFAULT_USERNAME = "root"
DEFAULT_PASSWORD = "eZfLK3X4-SX0i-UmgUBe6E"

def fetch_models():
    """Fetch available models from the API."""
    try:
        response = requests.get(
            f"{DEFAULT_API_URL}/api/tags",
            auth=(DEFAULT_USERNAME, DEFAULT_PASSWORD),
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()
        models = response.json()
        return [
            model["name"]
            for model in models.get("models", [])
            if "failed" not in model["name"].lower()
        ]
    except Exception as e:
        raise RuntimeError(f"Error fetching models: {e}")

def generate_response(model_name, prompt):
    """Send a prompt to the API and fetch the generated response."""
    try:
        url = f"{DEFAULT_API_URL}/api/generate"
        payload = {"model": model_name, "prompt": prompt}
        response = requests.post(
            url,
            json=payload,
            auth=(DEFAULT_USERNAME, DEFAULT_PASSWORD),
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise RuntimeError(f"Error generating response: {e}")
