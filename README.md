# INTSEC-HT2024 Challenges

Welcome to the **INTSEC-HT2024** repository! This repository contains solutions to all the challenges presented in the course "Introduction to Security" (HT2024) of Stockholm University. Below, you will find a detailed breakdown of the challenges and their corresponding solutions, organized by lecture.

---

## Repository Structure

The repository is organized as follows:
- Each lecture has its own directory (e.g., `Lecture0`, `Lecture1`, etc.).
- Inside each directory, you will find subdirectories or files corresponding to the challenges (e.g., `Challenge0.1`, `Challenge1.2`, etc.).
- Supplementary files (e.g., scripts, PDFs, or test cases) are included where necessary.

---

## Challenges Overview

### Lecture 0
#### Challenge 0.1 (Simple)
- **Task:** Find the login/password combination used in Lab 0's scavenger hunt.
- **Solution:** A file/script is provided to retrieve the login/password combination.

#### Challenge 0.2 (Normal)
- **Task:** Write a script or one-liner to find all clues in Lab 0's scavenger hunt.
- **Solution:** A Python script is included that automates clue discovery.

---

### Lecture 1
#### Challenge 1.1 (Simple)
- **Task:** Decode a given string.
- **Solution:** The decoding process and logic are documented in the solution file.

#### Challenge 1.2 (Normal)
- **Task:** Decrypt a file encrypted with a 120-bit key using provided hints.
- **Solution:** A decryption script and detailed explanation are included.

---

### Lecture 2
#### Challenge 2.1 (Hard)
- **Task:** Perform a Length Extension Attack on an HMAC-SHA1 implementation.
- **Solution:** The extended message and valid HMAC are generated using a custom Python script.

#### Challenge 2.2 (Simple)
- **Task:** Verify HMACs for given messages and identify tampered ones.
- **Solution:** A verification script highlights tampered messages.

#### Challenge 2.3 (Normal)
- **Task:** Send an encrypted email using PGP.
- **Solution:** Instructions for generating keys, encrypting emails, and uploading public keys are provided.

---

### Lecture 3
#### Challenge 3.1 (Normal)
- **Task:** Break weak passwords without salt.
- **Solution:** A password-cracking script using hash algorithms is included.

#### Challenge 3.2 (Normal)
- **Task:** Break weak passwords with salt.
- **Solution:** The script demonstrates how to crack salted hashes using hints.

#### Challenge 3.3 (Normal)
- **Task:** Benchmark hash computations for MD5, SHA1, SHA256, and Argon2id.
- **Solution:** Benchmark results are documented, including GPU-based performance metrics.

---

### Lecture 4
#### Challenge 4.1 (Simple)
- **Task:** Set permissions for a game and high score file following least privilege principles.
- **Solution:** A shell script configures appropriate permissions securely.

#### Challenge 4.2 (Simple)
- **Task:** Analyze Samy’s MySpace exploit.
- **Solution:** Explanations for bypassing HTML tag restrictions and JavaScript keyword limitations are provided in a text file.

---

### Lecture 5
#### Challenge 5.1 (Hard)
- **Task:** Write a quine in a programming language of your choice.
- **Solution:** A self-replicating program is included with thorough testing results.

#### Challenge 5.2 (Normal)
- **Task:** Compare files in two directories using checksums.
- **Solution:** A Python script performs file comparisons and checksum validation.

#### Challenge 5.3 (Normal)
- **Task:** Write unit tests for the XOR encryption function from Challenge 1.2.
- **Solution:** Unit tests are implemented using a testing framework, with comments explaining each section.

---

### Lecture 6
#### Challenge 6.1 (Hard)
- **Task:** Analyze privacy concerns of indoor security cameras from human-centered and feminist perspectives.
- **Solution:** A PDF (`Lecture6_Challenge6.1.pdf`) outlines potential concerns and proposes technical solutions.

---

### Lecture 7
#### Challenge 7.1 (Normal)
- **Task:** Extract a secret value using SQL injection techniques.
- **Solution:** The SQL injection steps used to retrieve the secret value are documented in detail.

#### Challenge 7.2 (Hard)
- **Task:** Identify the backdoor in Passoire's original image.
- **Solution:** An analysis of the backdoor mechanism is provided, along with detailed explanations of findings.

---

## How to Use This Repository

1. Clone this repository:
git clone https://github.com/amanjuman/intsec-ht2024.git

2. Navigate to the lecture/challenge directory of interest:
cd LectureX/ChallengeY

3. Follow instructions in the solution files or scripts provided for each challenge.

---

## Notes

- Some challenges require external tools or dependencies; ensure you have them installed as specified in individual solution files.
- For Challenge 6.1, refer to the PDF document for an in-depth analysis of privacy concerns and proposed solutions.

---

## Contact

If you have any questions or feedback about this repository, feel free to open an issue or contact me directly through GitHub!

Happy hacking! 😊
