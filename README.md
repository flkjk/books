
# Literango Book Repo

Public domain books created or sourced for [literango.com](https://literango.com).

## The structure of this repo

Each language has its own folder. For instance, `latin`. 

Inside these folders, each book has a folder. For instance, `aeneid`.

Inside this folder, there are always two folders: `foreign`, and `english`. These are the two epubs stored for this book. Note that these epubs are unzipped (epubs are really zip files).

At the root of the repo is a single .json file named `book_information.json`. This is where metadata for each book is stored. Every book entry in the folder structure should be mirrored in this file, and vice versa.

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
            "verified": false,
            "description": "Virgil’s epic poem begins with Aeneas fleeing the ruins of Troy with his father Anchises and his young son Ascanius, with a plan to make a home in Italy. Because of a prophecy foretelling that the descendants of Aeneas will one day destroy Carthage, Juno’s favorite city, Juno orders the god of the winds to unleash a terrible storm. The ships are thrown off course and arrive at an African port. As Aeneas makes his way towards his new home he encounters Dido, Carthage’s queen, and falls deeply in love. — Standard Ebooks"
          },
          ... (more books) ...
        ]
      },
      ... (more languages) ...
    ]

Adding to this file should be self explanatory; for descriptions we recommend using https://onlinestringtools.com/escape-string to store them in a .json string.

## Book verification

In order for a book to be marked as "verified" in the metadata file, it must meet the following criteria:

1. Clicking through the book using the shared left/right buttons must always land you on the same page in both books. This means that if you press the right arrow on your keyboard three times and hit chapter 1 in the English version, you should hit chapter 1 in the foreign version as well.
2. The table of contents must be very close to identical; any structure or indents in one should be replicated in the other.

Although you're welcome to play around with CSS to make everything in a chapter line up perfectly, it is not necessary.

Additionally, if you modify an Epub, make sure to add "Literango, " to the source metadata.
