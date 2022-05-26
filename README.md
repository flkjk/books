# Literango Book Repo

Public domain books created or sourced for [literango.com](https://literango.com).

## The structure of this repo

Each language has its own folder. For instance, `latin`. 

Inside these folders, each book has a folder. For instance, `aeneid`.

Inside this folder, there are always two folders: `foreign`, and `english`. These are the two epubs stored for this book. Note that these epubs are unzipped (epubs are really zip files).

At the root of a repo is a single .json file named `book-information.json`. This is where metadata for each book is stored. Every book entry in the folder structure should be mirrored in this file, and vice versa.

Here's an excerpt from this file:

    [
      {
        "language": "latin",
        "books": [
          {
            "filename": "aeneid",
            "title": "The Aeneid",
            "author": "Virgil",
            "translator": "John Dryden",
            "english_source": "Standard Ebooks",
            "foreign_source": "Gutenberg",
            "description": "Virgil’s epic poem begins with Aeneas fleeing the ruins of Troy with his father Anchises and his young son Ascanius, with a plan to make a home in Italy. Because of a prophecy foretelling that the descendants of Aeneas will one day destroy Carthage, Juno’s favorite city, Juno orders the god of the winds to unleash a terrible storm. The ships are thrown off course and arrive at an African port. As Aeneas makes his way towards his new home he encounters Dido, Carthage’s queen, and falls deeply in love. — Standard Ebooks"
          },
          ... (more books) ...
        ]
      },
      ... (more languages) ...
    ]

Adding to this file should be self explanatory; for descriptions we recommend using https://onlinejsontools.com/escape-json to store them in a .json string.
