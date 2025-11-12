#!/usr/bin/env python3
"""
Test suite for Evidence Register System

Tests validation, processing, and output compliance for the evidence register.
"""

import unittest
import tempfile
import shutil
import csv
from pathlib import Path
from evidence_register import EvidenceRegister


class TestEvidenceRegister(unittest.TestCase):
    """Test cases for Evidence Register System."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_dir = tempfile.mkdtemp()
        self.test_path = Path(self.test_dir)
        
    def tearDown(self):
        """Clean up test fixtures."""
        shutil.rmtree(self.test_dir, ignore_errors=True)
    
    def create_test_file(self, filename: str, content: bytes = b"Test content") -> Path:
        """Create a test file with given content."""
        filepath = self.test_path / filename
        filepath.write_bytes(content)
        return filepath
    
    def test_extract_date_from_filename(self):
        """Test date extraction from filename."""
        register = EvidenceRegister()
        
        # Test valid date
        date = register.extract_date_from_filename("241016-test-document.pdf")
        self.assertEqual(date, "2024-10-16")
        
        # Test another valid date
        date = register.extract_date_from_filename("250225-receipt.pdf")
        self.assertEqual(date, "2025-02-25")
        
        # Test no date
        date = register.extract_date_from_filename("nodatehere.pdf")
        self.assertEqual(date, "")
    
    def test_extract_message_id(self):
        """Test Message ID extraction from filename."""
        register = EvidenceRegister()
        
        # Test with message ID
        msg_id = register.extract_message_id(
            "250207 - Welcome - test@example.com.pdf"
        )
        self.assertEqual(msg_id, "test@example.com")
        
        # Test complex message ID
        msg_id = register.extract_message_id(
            "250207 - Subject - bNDbx@geopod-ismtpd-9.pdf"
        )
        self.assertEqual(msg_id, "bNDbx@geopod-ismtpd-9")
        
        # Test no message ID
        msg_id = register.extract_message_id("241016-document.pdf")
        self.assertEqual(msg_id, "")
    
    def test_extract_domain_and_email(self):
        """Test domain and email extraction from Message ID."""
        register = EvidenceRegister()
        
        # Test valid message ID
        domain, email = register.extract_domain_and_email("test@example.com")
        self.assertEqual(domain, "example.com")
        self.assertEqual(email, "test@example.com")
        
        # Test complex domain
        domain, email = register.extract_domain_and_email("msg@mail.example.co.uk")
        self.assertEqual(domain, "mail.example.co.uk")
        self.assertEqual(email, "msg@mail.example.co.uk")
        
        # Test no message ID
        domain, email = register.extract_domain_and_email("")
        self.assertEqual(domain, "")
        self.assertEqual(email, "")
    
    def test_extract_subject(self):
        """Test subject extraction from filename."""
        register = EvidenceRegister()
        
        # Test with date prefix
        subject = register.extract_subject("241016 - Contract Agreement.pdf")
        self.assertEqual(subject, "Contract Agreement")
        
        # Test with message ID suffix
        subject = register.extract_subject("250225 - Receipt - test@example.com.pdf")
        self.assertEqual(subject, "Receipt")
        
        # Test simple filename
        subject = register.extract_subject("simple-document.pdf")
        self.assertEqual(subject, "simple-document")
    
    def test_categorize_document(self):
        """Test document categorization."""
        register = EvidenceRegister()
        
        # Test receipt
        category = register.categorize_document("Receipt # 85835.pdf", "Receipt")
        self.assertEqual(category, "Receipt")
        
        # Test agreement
        category = register.categorize_document("rental-agreement.pdf", "Agreement")
        self.assertEqual(category, "Legal")
        
        # Test VCAT
        category = register.categorize_document("VCAT-order.pdf", "VCAT order")
        self.assertEqual(category, "VCAT Document")
        
        # Test maintenance
        category = register.categorize_document("doc.pdf", "Maintenance Request")
        self.assertEqual(category, "Maintenance")
        
        # Test default
        category = register.categorize_document("unknown.pdf", "Unknown")
        self.assertEqual(category, "Document")
    
    def test_compute_hashes(self):
        """Test SHA256/SHA512 hash computation."""
        register = EvidenceRegister(base_path=self.test_dir)
        
        # Create test file with known content
        content = b"Test content for hashing"
        filepath = self.create_test_file("test.pdf", content)
        
        sha256, sha512 = register.compute_hashes(filepath)
        
        # Verify hashes are not empty
        self.assertTrue(len(sha256) > 0)
        self.assertTrue(len(sha512) > 0)
        
        # Verify hash lengths (hex strings)
        self.assertEqual(len(sha256), 64)  # 256 bits = 64 hex chars
        self.assertEqual(len(sha512), 128)  # 512 bits = 128 hex chars
        
        # Verify hashes are consistent
        sha256_2, sha512_2 = register.compute_hashes(filepath)
        self.assertEqual(sha256, sha256_2)
        self.assertEqual(sha512, sha512_2)
    
    def test_validate_evidence_row_success(self):
        """Test successful evidence row validation."""
        register = EvidenceRegister()
        
        evidence_data = {
            "EVID ID": 100001,
            "Filename": "test.pdf",
            "Date Formatted": "2024-10-16",
            "Subject": "Test",
            "Message ID": "",
            "Domain": "",
            "Email Address": "",
            "File Size (KB)": 100,
            "SHA256": "abc123",
            "SHA512": "def456",
            "file_category": "Document",
            "Raw URL": "",
            "storage_path": "Root",
            "ID": 200001,
            "file_number": 5001,
            "Modified (A)": "2024-10-16T10:00:00",
            "Modified (B)": "2024-10-16T10:00:00",
            "Fully detail clean OCR": "Test summary"
        }
        
        is_valid, error_msg = register.validate_evidence_row(evidence_data)
        self.assertTrue(is_valid)
        self.assertEqual(error_msg, "")
    
    def test_validate_evidence_row_missing_evid_id(self):
        """Test validation fails with missing EVID ID."""
        register = EvidenceRegister()
        
        evidence_data = {
            "EVID ID": None,
            "Filename": "test.pdf",
            "Date Formatted": "2024-10-16",
            "Subject": "Test",
            "Message ID": "",
            "Domain": "",
            "Email Address": "",
            "File Size (KB)": 100,
            "SHA256": "abc123",
            "SHA512": "def456",
            "file_category": "Document",
            "Raw URL": "",
            "storage_path": "Root",
            "ID": 200001,
            "file_number": 5001,
            "Modified (A)": "2024-10-16T10:00:00",
            "Modified (B)": "2024-10-16T10:00:00",
            "Fully detail clean OCR": "Test summary"
        }
        
        is_valid, error_msg = register.validate_evidence_row(evidence_data)
        self.assertFalse(is_valid)
        self.assertIn("Missing EVID ID", error_msg)
    
    def test_validate_evidence_row_duplicate_evid_id(self):
        """Test validation fails with duplicate EVID ID."""
        register = EvidenceRegister()
        register.seen_evid_ids.add(100001)
        
        evidence_data = {
            "EVID ID": 100001,
            "Filename": "test.pdf",
            "Date Formatted": "2024-10-16",
            "Subject": "Test",
            "Message ID": "",
            "Domain": "",
            "Email Address": "",
            "File Size (KB)": 100,
            "SHA256": "abc123",
            "SHA512": "def456",
            "file_category": "Document",
            "Raw URL": "",
            "storage_path": "Root",
            "ID": 200001,
            "file_number": 5001,
            "Modified (A)": "2024-10-16T10:00:00",
            "Modified (B)": "2024-10-16T10:00:00",
            "Fully detail clean OCR": "Test summary"
        }
        
        is_valid, error_msg = register.validate_evidence_row(evidence_data)
        self.assertFalse(is_valid)
        self.assertIn("Duplicate EVID ID", error_msg)
    
    def test_validate_evidence_row_duplicate_filename(self):
        """Test validation fails with duplicate filename."""
        register = EvidenceRegister()
        register.seen_filenames.add("test.pdf")
        
        evidence_data = {
            "EVID ID": 100001,
            "Filename": "test.pdf",
            "Date Formatted": "2024-10-16",
            "Subject": "Test",
            "Message ID": "",
            "Domain": "",
            "Email Address": "",
            "File Size (KB)": 100,
            "SHA256": "abc123",
            "SHA512": "def456",
            "file_category": "Document",
            "Raw URL": "",
            "storage_path": "Root",
            "ID": 200001,
            "file_number": 5001,
            "Modified (A)": "2024-10-16T10:00:00",
            "Modified (B)": "2024-10-16T10:00:00",
            "Fully detail clean OCR": "Test summary"
        }
        
        is_valid, error_msg = register.validate_evidence_row(evidence_data)
        self.assertFalse(is_valid)
        self.assertIn("Duplicate Filename", error_msg)
    
    def test_generate_ocr_summary(self):
        """Test OCR summary generation."""
        register = EvidenceRegister()
        
        evidence_data = {
            "EVID ID": 100001,
            "Filename": "test-document.pdf",
            "Date Formatted": "2024-10-16",
            "Subject": "Test Document",
            "Message ID": "test@example.com",
            "Domain": "example.com",
            "Email Address": "test@example.com",
            "File Size (KB)": 100,
            "SHA256": "abc123def456",
            "SHA512": "ghi789jkl012",
            "file_category": "Legal",
            "Raw URL": "",
            "storage_path": "Root",
            "ID": 200001,
            "file_number": 5001,
            "Modified (A)": "2024-10-16T10:00:00",
            "Modified (B)": "2024-10-16T10:00:00",
            "Fully detail clean OCR": ""
        }
        
        summary = register.generate_ocr_summary(evidence_data)
        
        # Verify summary contains key information
        self.assertIn("test-document.pdf", summary)
        self.assertIn("100 KB", summary)
        self.assertIn("2024-10-16", summary)
        self.assertIn("Test Document", summary)
        self.assertIn("Legal", summary)
        self.assertIn("test@example.com", summary)
        self.assertIn("abc123def456", summary)
        self.assertIn("ghi789jkl012", summary)
        self.assertIn("Root", summary)
        self.assertIn("authenticated", summary)
        self.assertIn("legal proceedings", summary)
    
    def test_process_document_integration(self):
        """Integration test for document processing."""
        register = EvidenceRegister(base_path=self.test_dir)
        
        # Create a test PDF file
        content = b"PDF test content for integration test"
        filepath = self.create_test_file("241016-test-document.pdf", content)
        
        # Process the document
        evidence_data = register.process_document(filepath, 100001, 200001, 5001)
        
        # Verify the result
        self.assertIsNotNone(evidence_data)
        self.assertEqual(evidence_data["EVID ID"], 100001)
        self.assertEqual(evidence_data["Filename"], "241016-test-document.pdf")
        self.assertEqual(evidence_data["Date Formatted"], "2024-10-16")
        self.assertEqual(evidence_data["Subject"], "241016-test-document")
        self.assertEqual(evidence_data["ID"], 200001)
        self.assertEqual(evidence_data["file_number"], 5001)
        self.assertTrue(len(evidence_data["SHA256"]) > 0)
        self.assertTrue(len(evidence_data["SHA512"]) > 0)
        self.assertTrue(len(evidence_data["Fully detail clean OCR"]) > 0)
    
    def test_csv_output_format(self):
        """Test CSV output format compliance."""
        register = EvidenceRegister(base_path=self.test_dir)
        
        # Create test files
        self.create_test_file("241016-document1.pdf", b"Content 1")
        self.create_test_file("250225-document2.pdf", b"Content 2")
        
        # Process documents
        register.process_all_documents()
        
        # Write CSV
        output_path = self.test_path / "output.csv"
        register.write_csv(str(output_path))
        
        # Verify CSV file exists
        self.assertTrue(output_path.exists())
        
        # Parse CSV and verify structure
        with open(output_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            
            # Check we have rows
            self.assertEqual(len(rows), 2)
            
            # Check all columns present
            for row in rows:
                self.assertEqual(len(row), 18)
                for col in register.CSV_COLUMNS:
                    self.assertIn(col, row)
            
            # Verify sorting by EVID ID
            evid_ids = [int(row["EVID ID"]) for row in rows]
            self.assertEqual(evid_ids, sorted(evid_ids))
    
    def test_column_order(self):
        """Test that CSV columns are in the correct order."""
        register = EvidenceRegister(base_path=self.test_dir)
        
        # Create a test file
        self.create_test_file("241016-test.pdf", b"Test")
        
        # Process and write
        register.process_all_documents()
        output_path = self.test_path / "output.csv"
        register.write_csv(str(output_path))
        
        # Read and check column order
        with open(output_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            
            # Verify exact column order
            self.assertEqual(header, register.CSV_COLUMNS)


class TestValidationRules(unittest.TestCase):
    """Test validation rules and error handling."""
    
    def test_invalid_evid_id_type(self):
        """Test validation fails with non-integer EVID ID."""
        register = EvidenceRegister()
        
        evidence_data = {
            "EVID ID": "not-a-number",
            "Filename": "test.pdf",
            "Date Formatted": "",
            "Subject": "",
            "Message ID": "",
            "Domain": "",
            "Email Address": "",
            "File Size (KB)": 0,
            "SHA256": "",
            "SHA512": "",
            "file_category": "Document",
            "Raw URL": "",
            "storage_path": "Root",
            "ID": 200001,
            "file_number": 5001,
            "Modified (A)": "",
            "Modified (B)": "",
            "Fully detail clean OCR": ""
        }
        
        is_valid, error_msg = register.validate_evidence_row(evidence_data)
        self.assertFalse(is_valid)
        self.assertIn("Invalid EVID ID", error_msg)


if __name__ == "__main__":
    unittest.main()
