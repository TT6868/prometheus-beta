def find_palindrome_index_pairs(words):
    """
    Find pairs of indices where the words at those indices are palindromes when reversed.
    
    Args:
        words (list): A list of words to check for palindrome index pairs.
    
    Returns:
        list: A list of index pairs where the reversed words form palindromes.
    """
    palindrome_pairs = []
    
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j:
                # Check if reversed word at j matches word at i
                if (words[i] + words[j]) == (words[i] + words[j])[::-1]:
                    palindrome_pairs.append([i, j])
    
    return palindrome_pairs