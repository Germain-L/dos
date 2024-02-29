import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

# L'URL de votre application de test
URL = "http://localhost:5000/calcul?n=10"

# Nombre de requêtes à exécuter
def send_request(url):
    """Fonction pour envoyer une requête HTTP GET à l'URL spécifiée."""
    try:
        response = requests.get(url)
        return response.status_code
    except Exception as e:
        return str(e)

def main(url, total_requests):
    """Fonction principale pour exécuter les requêtes en parallèle."""
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(send_request, url) for _ in range(total_requests)]
        for future in as_completed(futures):
            try:
                response_status = future.result()
                print(f"Réponse reçue avec le statut : {response_status}")
            except Exception as exc:
                print(f"Une exception a été rencontrée : {exc}")

if __name__ == "__main__":
    while True:
        main(URL, 1000)