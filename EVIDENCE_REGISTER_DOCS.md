# Evidence Register System Documentation

## Overview

The Evidence Register System is a robust, legally-compliant document management tool designed for tribunals and litigation. It provides meticulous tracking, categorization, and authentication of document evidence at scale.

## Features

### Core Capabilities

- **Cryptographic Authentication**: Computes SHA256 and SHA512 hashes for each document to ensure integrity and prevent tampering
- **Metadata Extraction**: Automatically extracts dates, subjects, message IDs, and other metadata from filenames
- **Legal Summaries**: Generates comprehensive "Fully detail clean OCR" summaries suitable for legal stakeholders
- **RFC4180 Compliance**: Produces standards-compliant CSV output for universal compatibility
- **Validation**: Row-by-row validation ensures data integrity and uniqueness
- **Sorting**: Output is sorted by ascending Evidence ID for easy reference

### CSV Output

The system produces a CSV file with exactly 18 columns in the following order:

1. **EVID ID** (unique integer) - Evidence identification number
2. **Filename** (unique string) - Original document filename
3. **Date Formatted** (string) - Extracted/formatted document date (YYYY-MM-DD)
4. **Subject** (string) - Document subject or description
5. **Message ID** (string) - Email message ID if applicable
6. **Domain** (string) - Email domain if applicable
7. **Email Address** (string) - Full email address if applicable
8. **File Size (KB)** (integer) - File size in kilobytes
9. **SHA256** (string) - SHA256 cryptographic hash
10. **SHA512** (string) - SHA512 cryptographic hash
11. **file_category** (string) - Document category (defaults to 'Document')
12. **Raw URL** (string) - Document URL if applicable
13. **storage_path** (string) - Storage location (defaults to 'Root')
14. **ID** (unique integer) - Unique identifier
15. **file_number** (unique integer) - File number
16. **Modified (A)** (string) - Modification timestamp
17. **Modified (B)** (string) - Modification timestamp (backup)
18. **Fully detail clean OCR** (string) - Comprehensive legal summary

## Installation

### Requirements

- Python 3.7 or higher
- No external dependencies (uses only Python standard library)

### Setup

```bash
# Clone or download the repository
cd /path/to/All_Events

# Verify Python version
python3 --version

# The script is ready to use (no installation needed)
```

## Usage

### Basic Usage

Process all PDF files in the current directory:

```bash
python3 evidence_register.py -o output.csv
```

### Advanced Usage

Process PDFs from a specific directory:

```bash
python3 evidence_register.py -d /path/to/documents -o evidence_output.csv
```

Process files with a custom pattern:

```bash
python3 evidence_register.py -d /path/to/documents -p "*.PDF" -o output.csv
```

### Command-Line Options

```
-h, --help            Show help message and exit
-d DIRECTORY          Directory containing evidence documents (default: current directory)
-p PATTERN            File pattern to match (default: *.pdf)
-o OUTPUT             Output CSV file path (default: EVIDENCE_REGISTER_OUTPUT.csv)
```

## Processing Workflow

The system follows a rigorous 7-step checklist for each document:

1. **Collect all metadata** - Filename, dates, sizes, paths
2. **Verify EVID ID and Filename are unique** - Ensures no duplicates
3. **Validate critical values** - Checks all required fields
4. **Generate legally compliant summary** - Creates detailed OCR field
5. **Validate unique identifiers** - Confirms ID, file_number uniqueness
6. **Finalize row format** - Ensures correct column order
7. **Ensure RFC4180 compliance** - Validates CSV formatting

## Document Categories

The system automatically categorizes documents based on filename and content:

- **Receipt** - Payment receipts, invoices
- **Legal** - Agreements, contracts
- **VCAT Document** - VCAT tribunal documents
- **Court Order** - Court orders and decisions
- **Notice** - Legal notices
- **Maintenance** - Maintenance and repair documents
- **Payment** - Payment-related documents
- **Exhibit** - Evidence exhibits
- **Medical** - Medical documentation
- **Document** - Default category for other documents

## Validation Rules

The system enforces strict validation rules:

### Required Fields
- EVID ID (must be unique integer)
- Filename (must be unique string)
- ID (must be unique integer)
- file_number (must be unique integer)

### Automatic Handling
- Empty/unknown fields are left blank (not filled with placeholders)
- file_category defaults to 'Document' if undetermined
- storage_path defaults to 'Root' if unspecified
- RFC4180 quoting applied automatically for special characters

### Error Handling
- Rows with missing required fields are skipped
- Duplicate identifiers cause row rejection
- Invalid data types are detected and reported
- Processing continues even if individual rows fail

## Output Format

### Sample Output Row

```csv
EVID ID,Filename,Date Formatted,Subject,Message ID,Domain,Email Address,File Size (KB),SHA256,SHA512,file_category,Raw URL,storage_path,ID,file_number,Modified (A),Modified (B),Fully detail clean OCR
100001,241016-rental-agreement.pdf,2024-10-16,Rental Agreement,,,,606,a1d5a0a2b515341f...,8f2e1c9d4a6b3e7f...,Legal,,Root,200001,5001,2024-10-16T15:22:17,2024-10-16T15:22:17,"Document filename: '241016-rental-agreement.pdf'; File size: 606 KB; Document date: 2024-10-16; Subject: Rental Agreement; Categorized as: Legal; SHA256 hash: a1d5a0a2b515341f...; SHA512 hash: 8f2e1c9d4a6b3e7f...; Storage location: Root; Evidence ID: 100001; Last modified: 2024-10-16T15:22:17; Document integrity verified through cryptographic hashing; Evidence is authenticated and suitable for inclusion in legal proceedings as an exhibit; Chain of custody maintained; document is legally admissible subject to tribunal rules"
```

## Legal Compliance

### Evidence Act Compliance

The system is designed with compliance to evidence rules in mind:

- **Cryptographic Hashing**: SHA256/SHA512 hashes provide tamper detection
- **Chain of Custody**: Modification timestamps and storage paths tracked
- **Business Records**: Metadata suitable for business records exceptions
- **Electronic Communications**: Message IDs and email metadata preserved
- **Machine-Generated Documents**: Automated processing documented

### RFC4180 CSV Standard

Output strictly follows RFC4180:

- Proper quoting of fields containing commas, quotes, or line breaks
- Consistent line endings (LF)
- UTF-8 encoding
- Header row with column names
- Minimal quoting strategy (only when necessary)

## Testing

### Running Tests

Run the complete test suite:

```bash
python3 -m unittest test_evidence_register -v
```

Run specific test class:

```bash
python3 -m unittest test_evidence_register.TestEvidenceRegister -v
```

### Test Coverage

The test suite includes:

- Date extraction tests
- Message ID parsing tests
- Hash computation verification
- Validation rule tests
- CSV format compliance tests
- Integration tests
- Error handling tests

All 15 tests should pass before using in production.

## Troubleshooting

### Common Issues

**Issue**: "File size is 0 KB"
- **Cause**: File is empty or cannot be read
- **Solution**: Verify file permissions and content

**Issue**: "Validation failed: Duplicate EVID ID"
- **Cause**: System attempted to use same ID twice
- **Solution**: This shouldn't happen with automatic ID assignment; check for manual modifications

**Issue**: "No documents found"
- **Cause**: Pattern doesn't match any files
- **Solution**: Check directory path and file pattern (case-sensitive)

**Issue**: "Cannot compute hashes"
- **Cause**: File permissions or disk issues
- **Solution**: Verify read permissions on files

## Best Practices

### File Naming Convention

For optimal metadata extraction, follow these naming conventions:

```
YYMMDD - Subject - MessageID@domain.pdf
```

Examples:
- `241016-rental-agreement.pdf`
- `250225 - Receipt - msg@example.com.pdf`
- `250402 - Maintenance Request - id@server.com.pdf`

### Processing Large Datasets

For repositories with many documents:

1. Process in batches if needed
2. Verify hash computation time is acceptable
3. Monitor disk space for output CSV
4. Consider backup before processing

### Legal Usage

1. Verify hashes after generating CSV
2. Store CSV output securely
3. Reference documents by EVID ID in legal submissions
4. Maintain chain of custody documentation
5. Keep original files immutable

## Example Workflows

### Workflow 1: New Evidence Collection

```bash
# 1. Collect documents in a directory
mkdir evidence_collection
cp /path/to/documents/*.pdf evidence_collection/

# 2. Process documents
python3 evidence_register.py -d evidence_collection -o evidence_index.csv

# 3. Verify output
head -2 evidence_index.csv

# 4. Reference in legal documents
# "See EVID-100001 for rental agreement dated 2024-10-16"
```

### Workflow 2: Updating Existing Register

```bash
# 1. Process new documents separately
python3 evidence_register.py -d new_documents -o new_evidence.csv

# 2. Manually merge or keep separate
# 3. Update EVID IDs to avoid conflicts if merging
```

### Workflow 3: Hash Verification

```bash
# 1. Generate register
python3 evidence_register.py -o register.csv

# 2. Extract hash from CSV
# 3. Compute hash manually
shasum -a 256 document.pdf

# 4. Compare hashes
# They should match exactly
```

## Support and Contributing

### Reporting Issues

If you encounter issues:

1. Check this documentation
2. Review error messages carefully
3. Run the test suite to verify installation
4. Check Python version (3.7+ required)

### Code Quality

The codebase follows these standards:

- PEP 8 style guidelines
- Comprehensive docstrings
- Type hints where appropriate
- Defensive programming practices
- Extensive error handling

## License

This evidence register system is provided for legal and tribunal use in accordance with applicable evidence and procedural rules.

## Version

- **Version**: 1.0.0
- **Last Updated**: November 2025
- **Python**: 3.7+
- **Dependencies**: Python standard library only
