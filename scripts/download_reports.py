import os
import sys
import urllib.parse
import urllib.request

# Check if input file parameter was provided
if len(sys.argv) < 2:
    print("Error: Missing input file parameter.")
    print("\nUsage:")
    print("  python download_reports.py <input_file.txt>")
    print("\nExample:")
    print("  python download_reports.py report_dashboard_urls.txt")
    sys.exit(1)

input_file = sys.argv[1]

# Check if input file exists
if not os.path.isfile(input_file):
    print(f"Error: File '{input_file}' not found.")
    sys.exit(1)

# Create output directory
output_dir = os.path.join("reports", "published")
os.makedirs(output_dir, exist_ok=True)

# Read URLs from the given input file
with open(input_file, "r", encoding="utf-8") as f:
    urls = [line.strip() for line in f if line.strip()]

print(f"Loaded {len(urls)} URLs from '{input_file}'. Starting download...\n")

headers = {"User-Agent": "Mozilla/5.0"}
success, failed = 0, 0

for idx, url in enumerate(urls, start=1):
    filename = urllib.parse.unquote(url.split("/")[-1])
    filepath = os.path.join(output_dir, filename)

    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as response, open(
            filepath, "wb"
        ) as out_file:
            out_file.write(response.read())
        print(f"[{idx}/{len(urls)}] Downloaded: {filename}")
        success += 1
    except Exception as e:
        print(f"[{idx}/{len(urls)}] Failed: {filename} ({e})")
        failed += 1

print(
    f"\nDone! Downloaded {success} files to '{output_dir}' folder ({failed} failed)."
)