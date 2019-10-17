# Git Releases

Get the release history of different GitHub Repositery


### Prerequisites

  Project run on python 3.6.
  
  Need the following library installed: bs4,urllib,json
  

### Part 1
  To get the release from each repo I used the Beautiful Soup package for parsing HTML.
  Tag object allows us to navigate through HTML.
  By looking at the source page of the git release page I identify two main tags to get:
  The tags to get the releases number and the tags to get the next page of the release numbers.
 
  
### Part 2
  To standardized the release version across the 3 repositeries, I decided to apply some rules:
*  The beginning of each release should start with a number (in order to transform  v1.2 in 1.2 for example)

* No separation between the release number and the stage of development (for example 2.2.0rc2)

*  Abbrevation for the different stage of development : ('alpha'->'a','beta'->'b','incubating'->'i','candidate'->'c','release    candidate'->'rc')

*  Exception for two specific releases : in tensorflow 'tflite-v0.1.7'->'tflitev0.1.7' and in kafka 'show'
## Authors

Germain Geoffroy
