import regex as re

pattern = r'^\s*(.*?)\bOBTW\b'
line = "hhuhu OBTW ememem"
match = re.match(pattern, line)
if match:
    words_before_obtw = match.group(1).split()
    
    # Check if there are words before "OBTW"
    if words_before_obtw:
        print("Words exist before OBTW:", words_before_obtw)
    else:
        print("valid")
    
# Given line
# line = " PRODUKT OF oTLDR AN aTLDR     "
# # TLDR regex can only have a space before it
# pattern = r'\s+TLDR\b'
# # Split the line by "TLDR" to get segments after each occurrence
# segments = line.split("TLDR")[1:]

# # Check if any segment has words after "TLDR"
# words_after_tldr = []
# for segment in segments:
#     # Remove leading/trailing spaces and split by spaces to get individual words
#     words = segment.strip().split()
#     # Check if there are words after "TLDR" in this segment
#     if words:
#         words_after_tldr.extend(words)

# # Check if there are words after "TLDR" in any segment
# if words_after_tldr:
#     print("Words exist after TLDR:", words_after_tldr)
# else:
#     print("No words after TLDR")
    

line = "0TLDR   "

# Define the regex pattern to match one or more spaces before "TLDR"
pattern = r'TLDR'

# Search for the pattern in the line
matches = re.findall(pattern, line)

if matches:
    # Split the line by "TLDR" to get segments after each occurrence
    segments = line.split("TLDR")[1:]

    # Check if any segment has words after "TLDR"
    words_after_tldr = []
    
    # Remove leading/trailing spaces and split by spaces to get individual words
    words = segments[-1].strip().split()
    # Check if there are words after "TLDR" in this segment
    if words:
        words_after_tldr.extend(words)

    # Check if there are words after "TLDR" in any segment
    if words_after_tldr:
        print("Words exist after TLDR:", words_after_tldr)
    else:
        print("[TLDR FOUND] No words after TLDR")
else:
    print("Pattern not found")

import re

# Your initial text
text = "Some text o a TLDRa   "

# Regular expression pattern
pattern = r'(\bTLDR\b)\s*$'

# Find a match using the pattern
match = re.search(pattern, text)

if match:
    print("No words after TLDR")
else:
    # Check if TLDR is not found
    if re.search(r'\bTLDR\b', text):
        print("There are words after TLDR")
    else:
        print("TLDR not found")




"""
SCRATCH
"""

    # # Search for the pattern in the line
    # matches = re.findall(pattern, line)

    # if matches:
    #     # Split the line by "TLDR" to get segments after each occurrence
    #     segments = line.split("TLDR")[1:]

    #     # Check if any segment has words after "TLDR"
    #     words_after_tldr = []
        
    #     # Remove leading/trailing spaces and split by spaces to get individual words
    #     words = segments[-1].strip().split()
    #     # Check if there are words after "TLDR" in this segment
    #     if words:
    #         words_after_tldr.extend(words)

    #     # Check if there are words after "TLDR" in any segment
    #     if words_after_tldr:
    #         print("CommentError: Words exist after TLDR:", words_after_tldr)
    #         print(f"\n\tLine {i+1}: {line}")
    #         sys.exit()
    #     else:
    #         print("TLDR is found!!! \n\n\n\n")
    #         return True

    # else: return False