import os
import difflib
from pathlib import Path

def extract_code(filepath):
    # Simple C++ code extractor (adjust as needed)
    with open(filepath, 'r') as f:
        content = f.read()
    # Add more sophisticated code extraction logic here
    return content

def check_similarity(file1, file2):
    code1 = extract_code(file1)
    code2 = extract_code(file2)
    
    matcher = difflib.SequenceMatcher(None, code1, code2)
    return matcher.ratio() * 100  # Returns percentage

def check_all_assignments(new_assignment_path):
    assignments_dir = Path('assignments')
    results = []
    
    for existing_file in assignments_dir.glob('*.cpp'):
        if existing_file.name != Path(new_assignment_path).name:
            similarity = check_similarity(new_assignment_path, existing_file)
            results.append((existing_file.name, similarity))
    
    return sorted(results, key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python check_plagiarism.py <new_assignment.cpp>")
        sys.exit(1)
    
    results = check_all_assignments(sys.argv[1])
    for filename, similarity in results:
        print(f"{filename}: {similarity:.2f}% similar")
    
    if results and results[0][1] > 40:
        print("\nERROR: Plagiarism detected (>40% similarity)")
        sys.exit(1)
    else:
        print("\nOK: No significant plagiarism detected")
