# Pipeline de Ingestão

```mermaid
flowchart LR

    API["API Pública"]

    LANDING["Landing
    JSON RAW"]

    BRONZE["Bronze
    Delta Lake"]

    SILVER["Silver
    Curated"]

    GOLD["Gold
    Analytics"]

    API --> LANDING
    LANDING --> BRONZE
    BRONZE --> SILVER
    SILVER --> GOLD
```