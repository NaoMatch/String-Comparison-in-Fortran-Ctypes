# String-Comparison-in-Fortran-Ctypes

## Algorithms
### Longest Common Substring
      - Distance (normalized)
      - Sequence (normalized)
      - Character
         
### Longest Common Subsequence
      - Distance (normalized)
      - Sequence (normalized)
      - Character
      
### Hamming 
      - Distance (normalized)
      - Sequence (normalized)
   
### Levenshtein
      - Distance (normalized)
      - Sequence (normalized)
   
### Gestalt Pattern Matching
      - Score
      
### Jaro
      - Distance (normalized)
      - Sequence (normalized)
   
## Usage
    make 
    
    python callF90lib.py

## Functions
### Longest Common Substring
      - LCSubStr_length(sequence1, sequence2)
      - LCSubStr_length_norm(sequence1, sequence2)
      - LCSubStr_distance(sequence1, sequence2)
      - LCSubStr_distance_norm(sequence1, sequence2)
      - LCSubStr_position(sequence1, sequence2)
      - LCSubStr_character(sequence1, sequence2)
      
### Longest Common Subsequence
      - LCSubSeq_length(sequence1, sequence2)
      - LCSubSeq_position(sequence1, sequence2)
      - LCSubSeq_character(sequence1, sequence2)
      
### Hamming
      - hammingdistance(sequence1, sequence2)
      - hammingdistance_norm(sequence1, sequence2)
      - hammingsimilarity(sequence1, sequence2)
      - hammingsimilarity_norm(sequence1, sequence2)
      
### Levenshtein
      - levenshteindistance(sequence1, sequence2)
      - levenshteindistance_norm(sequence1, sequence2)
      - levenshteinsimilarity(sequence1, sequence2)
      - levenshteinsimilarity_norm(sequence1, sequence2)
      
### Gestalt Pattern Matching
      - gpmscore(sequence1, sequence2)

### Jaro 
      - jarodistance(sequence1, sequence2)
      - jarodistance_norm(sequence1, sequence2)
      - jarosimilarity(sequence1, sequence2)
      - jarosimilarity_norm(sequence1, sequence2)
      (There is no difference jarodistance(similarity) and jarodistance_norm(similarity_norm). For consistency function name.)

