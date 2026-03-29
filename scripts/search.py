import asyncio
from myapp.repositories.qdrant import QdrantRepository


async def main():
    query = "I have headache"
    filter_payload = {
        "symptoms": {"match": "headache"},
    }

    with QdrantRepository() as repo:
        results = repo.search(
            query=query,
            k=5,
            filter_payload=filter_payload,
        )

        for doc in results:
            print(doc)


asyncio.run(main())