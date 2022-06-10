import sys
import json
from datetime import datetime, timezone

def isoformat_js(dt: datetime):
  return (
    dt.astimezone(timezone.utc)
      .isoformat(timespec="milliseconds")
      .replace("+00:00", "Z")
  )

# python update_json.py [changes file] [sha hash of commit] [commit time as unix timestamp] [book_information.json]

with open(sys.argv[4], "r") as jsonFile:
    info = json.load(jsonFile)

with open(sys.argv[1]) as changes_file:
  for line in changes_file:
    split = line.strip().split("/")
    print(split)

    if len(split) != 3:
      continue
    if split[2] != "english.epub" and split[2] != "foreign.epub":
      continue

    language = split[0]
    book = split[1]
    
    language_object = next((x for x in info if x["language"] == language), None)
    if language_object:
      book_object = next((x for x in language_object["books"] if x["filename"] == book), None)
      if book_object:
        book_object["last_commit"] = sys.argv[2]
        book_object["last_commit_time"] = isoformat_js(datetime.fromtimestamp(int(sys.argv[3])))
        if "first_commit" not in book_object:
          book_object["first_commit"] = sys.argv[2]
          book_object["first_commit_time"] = isoformat_js(datetime.fromtimestamp(int(sys.argv[3])))

with open(sys.argv[4], "w") as jsonFile:
    json.dump(info, jsonFile, indent=2)
