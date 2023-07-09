from src.client.api import APIClient

SEARCH_TEXT = "a soccer jacket"

if __name__ == "__main__":
    client = APIClient()
    client.build_db()
    results = client.search_query(SEARCH_TEXT)
    print(results)

    # for item, distance in results:
    #     print(f"TITLE: {item.name}")
    #     print(f"SUBTITLE: {item.sub_title}")
    #     print(f"DESCRIPTION: {item.description}")
    #     print(f"DISTANCE: {distance}")
    #     print("--------------------------------")
