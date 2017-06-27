import sys
sys.path.append('.')
import mylib

if len(sys.argv) != 3:
    exit("Usage: " + sys.argv[0] + " abc  def")

print(mylib.is_anagram(sys.argv[1], sys.argv[2]))

