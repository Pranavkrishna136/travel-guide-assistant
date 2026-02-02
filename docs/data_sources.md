# Data sources

The project uses curated travel content. Typical sources:

- WikiVoyage — public domain travel guides
- Sample travel reviews scraped for sentiment and highlights
- Optional: Open Data from tourism boards, Wikipedia

Attribution and licensing
- When using external content, confirm licensing. WikiVoyage content is usually CC BY-SA; include attribution and comply with license terms.

Preparing new sources
1. Download or scrape pages into `data/raw`.
2. Add a metadata file describing the license and source URL.
3. Run the indexing script to add content to FAISS.
