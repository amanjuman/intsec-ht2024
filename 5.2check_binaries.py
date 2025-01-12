import os
import hashlib
import sys

def compute_checksum(file_path):
    """Compute SHA256 checksum of a file."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def compare_directories(dir1, dir2):
    """Compare files in two directories based on name and checksum."""
    dir1_files = set(os.listdir(dir1))
    dir2_files = set(os.listdir(dir2))

    # Files missing in second directory
    missing_in_dir2 = dir1_files - dir2_files
    if missing_in_dir2:
        print(f"Files missing in {dir2}: {missing_in_dir2}")

    # Files missing in first directory
    missing_in_dir1 = dir2_files - dir1_files
    if missing_in_dir1:
        print(f"Files missing in {dir1}: {missing_in_dir1}")

    # Compare checksums for files present in both directories
    common_files = dir1_files & dir2_files
    for file_name in common_files:
        file1_path = os.path.join(dir1, file_name)
        file2_path = os.path.join(dir2, file_name)

        checksum1 = compute_checksum(file1_path)
        checksum2 = compute_checksum(file2_path)

        if checksum1 != checksum2:
            print(f"Checksum mismatch for {file_name}:")
            print(f"  {dir1}: {checksum1}")
            print(f"  {dir2}: {checksum2}")
        else:
            print(f"Checksum match for {file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <directory1> <directory2>")
        sys.exit(1)

    dir1, dir2 = sys.argv[1], sys.argv[2]
    if not (os.path.isdir(dir1) and os.path.isdir(dir2)):
        print("Both inputs must be valid directories.")
        sys.exit(1)

    compare_directories(dir1, dir2)
