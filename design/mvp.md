# AI Babysitter Desk: MVP

Pain: Parents searching for a babysitter face a decentralized, exhausting process, mostly through WhatsApp groups. They struggle to evaluate candidates' patience and reliability based on CVs alone, and waste time checking basic availability.

Product: An AI agent for parents. Instead of dry CVs, the AI agent conducts a free-dialogue interview with the candidate using simulation scenarios (e.g., crying baby) to produce a structured personality profile. It analyzes past reviews, checks calendar availability automatically, calculates travel distances, and finalizes the booking.

| Feature | Technique |
|---|---|
| Conducting interview dialogue and assessing personality | Multi-turn conversation, Agent loop |
| Extracting insights from past reviews and recommendations | RAG (Retrieval-Augmented Generation) |
| Producing personality profile from interview transcript | LLM call & Prompting |
| Checking availability and calculating distance | Tool calling (Calendar API, Maps API) |
| Initial chat to collect basic candidate details | Ordinary code (not AI) |