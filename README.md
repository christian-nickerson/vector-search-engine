# Vector Search Engine

A vector search engine project that uses NLP to query Nike product descriptions in place of a traditional keyword search engine.

The below outlines how docker compose architecture:

```mermaid
flowchart LR;
    A(Streamlit) --> B(GraphQL API);
    B -->|Read & Write| C(Vector DB);
```