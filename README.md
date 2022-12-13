work in progress

# Output rengu objects with jinja templates

Uses python-box to stuff values into the templates.

index all my previous searches
previous search spans as tokens

tokens = edges
entities = nodes


_id
_ts (timestamp)
_c0  (creator)
_h0  (sha256 content hash)


TOKENS

     Term + TermAliases > slugged > stemmed 
     Subjects > slugged | (MINUS DROPLIST)

     Title + AlternateTitles > slugged > fix_title
     Name + AlternateNames > slugged > fix_name

     ISBN > with-dash
     IAID
     OLID
     ScanCode
     ASIN     
     LCCN (fix)

     Date > ISODate

     (IChing Hexagrams + Title + Hex + Wen= + FuXi= + Trigram + Titles )  > slugged
 
    (all previous search spans) > stemmed > slugged

    
Content fields

    Description
    Body
    Commentary
    Notes

special indexers for descending to find source media=prime @ locus
special indexer to find variants and "zip them up" (change references and eliminate duplicates)
find dangling references and raise errors
scan content for ProperNames and add as creator entities and tag as tokens


relationships direct

  
   _id      source=         _id
             
   _id      contains=       _id        

   _id      references=    _id

   _id      variant=      _id

   _id      see_also=         _id

   _id      by=,editor=,illustrator=,contributor=,creator=



            indirect

   _id      TOKEN             _id

   _id      (TOKEN set in    _id
                TOKEN set)

   _id      creator=same    _id

   _id      source=same    _id

   _id      source=same    _id
            locus=same,next,last

   _id      source=same    _id
            page=same,next,last

   _id      date=same,next,last _id




