# DOI verification for Scheme B
import requests, csv, time, sys
def verify_doi(doi):
    if not doi or doi.strip() in ('NA','', 'To be filled'):
        return None, None, None
    url = f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}?fields=title,year,authors,citationCount"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            return True, data.get('title'), data.get('year')
        else:
            return False, None, None
    except Exception as e:
        return False, str(e), None

csv_path = '/home/user/academic-research-skills/subhealth-review/literature_matrix_schemeB_template.csv'
try:
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            doi = row.get('DOI','').strip()
            if doi.startswith('10.'):
                valid, title, year = verify_doi(doi)
                status = "✓ VALID" if valid else "✗ INVALID - check"
                print(f"{row['No']} {row['First_Author_Year']} DOI:{doi} {status} Title:{title} Year:{year}")
                time.sleep(1)
            else:
                print(f"{row['No']} {row['First_Author_Year']} DOI:{doi} SKIP")
except FileNotFoundError:
    print(f"CSV not found: {csv_path}")
