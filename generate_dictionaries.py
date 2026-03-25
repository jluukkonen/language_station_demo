import os
from rdflib import Graph, Namespace, RDF

# CONFIGURATION
# Folder containing the .ttl files
TERMINOLOGY_DIR = "terminology"
# Final output filename
OUTPUT_FILE = "verified_academic_dictionaries.py"

# NAMESPACES
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")

# FILE-TO-DICTIONARY MAPPING (In priority order)
# Rule: If a term appears in multiple files, prioritize mesh > tero > koko > yso.
FILE_MAPPINGS = [
    ("mesh", "MESH_DICTIONARY"),
    ("tero", "TERO_DICTIONARY"),
    ("koko", "KOKO_DICTIONARY"),
    ("yso", "YSO_DICTIONARY")
]

def find_file(pattern):
    """Finds a file in the terminology directory that starts with the pattern."""
    if not os.path.exists(TERMINOLOGY_DIR):
        return None
    for f in os.listdir(TERMINOLOGY_DIR):
        if f.lower().startswith(pattern.lower()) and (f.endswith(".ttl") or f.endswith(".rdf")):
            return f
    return None

def generate_dictionaries():
    """
    Parses SKOS files and extracts English-to-Finnish terminology.
    Applies priority rules and generates a final Python module.
    """
    # Master set for deduplication (priority order)
    seen_terms_en = set()
    
    # Storage for valid dictionaries
    collected_dictionaries = []

    print("--- Terminology Extraction Started ---")

    for pattern, dict_name in FILE_MAPPINGS:
        filename = find_file(pattern)
        
        if not filename:
            print(f"Warning: No file matching '{pattern}' found in {TERMINOLOGY_DIR}. Skipping.")
            continue

        file_path = os.path.join(TERMINOLOGY_DIR, filename)
        print(f"Processing {filename}...")
        
        # Determine format (Turtle for .ttl, XML for .rdf)
        fmt = "turtle" if filename.endswith(".ttl") else "xml"
        
        g = Graph()
        try:
            g.parse(file_path, format=fmt)
        except Exception as e:
            print(f"Error parsing {filename}: {e}")
            continue

        current_dict = {}
        # 1. Locate all skos:Concept subjects
        for concept in g.subjects(RDF.type, SKOS.Concept):
            # 2. Get prefLabels
            en_labels = [str(l).lower() for l in g.objects(concept, SKOS.prefLabel) if l.language == 'en']
            fi_labels = [str(l) for l in g.objects(concept, SKOS.prefLabel) if l.language == 'fi']
            
            # 3. Strictness: Only include if both exist
            if en_labels and fi_labels:
                en_term = en_labels[0].strip()
                fi_term = fi_labels[0].strip()
                
                # 4. Sanitization: Guarantee no empty strings or whitespace keys
                if not en_term or not fi_term:
                    continue
                
                # 4. Deduplication: First come, first served (priority order)
                if en_term not in seen_terms_en:
                    current_dict[en_term] = fi_term
                    seen_terms_en.add(en_term)

        # Store for output
        collected_dictionaries.append((dict_name, current_dict))
        print(f" - {len(current_dict)} terms extracted from {filename}")

    # 5. Write final output file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write("# Generated Academic Terminology Dictionaries\n")
        f.write("# Priority: mesh > tero > koko > yso\n\n")

        for dict_name, data in collected_dictionaries:
            f.write(f"{dict_name} = {{\n")
            for en_key in sorted(data.keys()):
                f.write(f"    {repr(en_key)}: {repr(data[en_key])},\n")
            f.write("}\n\n")

    print(f"\nSUCCESS: Results saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_dictionaries()
