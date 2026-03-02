import requests
import json
import argparse
import sys

def fetch_drug_data(drug_name):
    """
    Fetches drug label data from OpenFDA API for a given drug name.
    """
    url = f"https://api.fda.gov/drug/label.json?search=openfda.generic_name:{drug_name}+openfda.brand_name:{drug_name}&limit=1"

    print(f"Fetching data for {drug_name} from OpenFDA...")
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if not data.get("results"):
            print(f"No results found for {drug_name}.")
            return None

        result = data["results"][0]

        extracted_data = {
            "Brand Name": result.get("openfda", {}).get("brand_name", ["Unknown"])[0],
            "Generic Name": result.get("openfda", {}).get("generic_name", ["Unknown"])[0],
            "Indications and Usage": result.get("indications_and_usage", ["No data available"])[0],
            "Adverse Reactions": result.get("adverse_reactions", ["No data available"])[0],
            "Warnings and Precautions": result.get("warnings_and_cautions", ["No data available"])[0],
            "Boxed Warning": result.get("boxed_warning", ["No boxed warning"])
        }

        return extracted_data
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print(f"No results found for {drug_name} on OpenFDA.")
        else:
            print(f"HTTP Error: {e}")
        return None
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch oncology drug data from OpenFDA API.")
    parser.add_argument("--drug", type=str, default="daratumumab", help="Drug name to search for (e.g., daratumumab, pembrolizumab)")
    parser.add_argument("--output", type=str, default="drug_data.json", help="Output JSON file path")

    args = parser.parse_args()

    drug_data = fetch_drug_data(args.drug)

    if drug_data:
        print("\n--- Extracted Information ---")
        for key, value in drug_data.items():
            print(f"{key}: {value[:200]}...")

        with open(args.output, "w") as f:
            json.dump(drug_data, f, indent=4)
        print(f"\nSaved full extracted data to {args.output}")
    else:
        sys.exit(1)
