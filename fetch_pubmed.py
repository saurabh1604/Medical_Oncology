import requests
import xml.etree.ElementTree as ET
import json
import argparse

def search_pubmed(query, max_results=5):
    """
    Search PubMed for a given query and return a list of document IDs (PMIDs).
    Uses the Entrez E-utilities API.
    """
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }

    print(f"Searching PubMed for: '{query}'...")
    response = requests.get(base_url, params=params)
    response.raise_for_status()

    data = response.json()
    id_list = data.get("esearchresult", {}).get("idlist", [])

    return id_list

def fetch_pubmed_abstracts(id_list):
    """
    Fetch abstracts and metadata for a list of PubMed IDs (PMIDs).
    """
    if not id_list:
        print("No IDs provided to fetch.")
        return []

    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(id_list),
        "retmode": "xml"
    }

    print(f"Fetching details for {len(id_list)} articles...")
    response = requests.get(base_url, params=params)
    response.raise_for_status()

    root = ET.fromstring(response.content)
    articles_data = []

    for article in root.findall(".//PubmedArticle"):
        pmid = article.find(".//PMID").text if article.find(".//PMID") is not None else "Unknown"
        title = article.find(".//ArticleTitle").text if article.find(".//ArticleTitle") is not None else "No Title"

        abstract_elem = article.find(".//Abstract")
        abstract_text = ""
        if abstract_elem is not None:
            abstract_parts = []
            for abstract_text_node in abstract_elem.findall(".//AbstractText"):
                label = abstract_text_node.get("Label", "")
                text = "".join(abstract_text_node.itertext())
                if label:
                    abstract_parts.append(f"{label}: {text}")
                else:
                    abstract_parts.append(text)
            abstract_text = "\n".join(abstract_parts)
        else:
            abstract_text = "No abstract available."

        articles_data.append({
            "PMID": pmid,
            "Title": title,
            "Abstract": abstract_text
        })

    return articles_data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch oncology literature from PubMed API.")
    parser.add_argument("--query", type=str, default="daratumumab adverse events multiple myeloma", help="Search query")
    parser.add_argument("--max_results", type=int, default=5, help="Maximum number of articles to fetch")
    parser.add_argument("--output", type=str, default="pubmed_data.json", help="Output JSON file path")

    args = parser.parse_args()

    pmids = search_pubmed(args.query, args.max_results)

    if pmids:
        print(f"Found {len(pmids)} articles. Fetching details...")
        articles = fetch_pubmed_abstracts(pmids)

        print("\n--- Extracted Articles ---")
        for idx, article in enumerate(articles, 1):
            print(f"\n[{idx}] {article['Title']}")
            print(f"Abstract preview: {article['Abstract'][:150]}...")

        with open(args.output, "w") as f:
            json.dump(articles, f, indent=4)
        print(f"\nSaved extracted articles to {args.output}")
    else:
        print("No articles found.")
