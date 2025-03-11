import pandas as pd
import re

# File paths
INPUT_FILE = "H:\\SoftZonik\\mail_auto_sent_utility\\data\\Business_Pune_Sorted.xlsx"
OUTPUT_FILE = "H:\\SoftZonik\\mail_auto_sent_utility\\data\\Merged_Business_Pune.xlsx"

EMAIL_COLUMNS = ["Email", "Email1", "CompanyEmail"]

def split_first_last_name(full_name):
    """Extract first and last name from 'ptc_name'."""
    if pd.isna(full_name):
        return ("", "")
    parts = str(full_name).strip().split(maxsplit=1)
    return (parts[0], parts[1] if len(parts) > 1 else "")

def split_and_clean_emails(email_str):
    """Splits emails by comma/semicolon, removes duplicates and empty values."""
    if pd.isna(email_str):
        return []
    
    # Convert non-string values (like numbers) to strings
    email_str = str(email_str)

    # Split emails and clean
    possible_emails = re.split(r"[,;]\s*", email_str.strip())
    unique_emails = []
    for em in possible_emails:
        em = em.strip()
        if em and em not in unique_emails:
            unique_emails.append(em)
    return unique_emails

def merge_emails(row):
    """Merge emails from multiple columns, remove duplicates, and format properly."""
    all_emails = []
    for col in EMAIL_COLUMNS:
        if col in row:
            all_emails.extend(split_and_clean_emails(row[col]))
    
    unique_emails = list(dict.fromkeys(all_emails))  # Remove duplicates while preserving order
    return ", ".join(unique_emails)

def main():
    # Read Excel file
    df = pd.read_excel(INPUT_FILE, dtype=str)  # Force all columns to be read as strings

    # Extract FirstName & LastName
    df["FirstName"], df["LastName"] = zip(*df["ptc_name"].apply(split_first_last_name))

    # Merge email columns
    df["MergedEmails"] = df.apply(merge_emails, axis=1)

    # Save updated data
    df.to_excel(OUTPUT_FILE, index=False)
    print(f"✅ Merged data saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
