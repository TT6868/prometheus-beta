def find_palindrome_pair_indices(words):
    """
    Find pairs of indices where words at those indices are palindromes when reversed.
    
    Args:
        words (list): A list of words to check for palindrome pairs.
    
    Returns:
        list: A list of index pairs where words' reversed characters form palindromes.
    
    Examples:
        >>> find_palindrome_pair_indices(["bat", "tab", "cat"])
        [[0, 1]]
        >>> find_palindrome_pair_indices(["hello", "olleh", "world"])
        [[0, 1]]
        >>> find_palindrome_pair_indices(["a", "b", "c"])
        []
    """
    result = []
    n = len(words)
    
    for i in range(n):
        for j in range(n):
            if i != j:
                # Check if reversing both words creates a palindrome
                if words[i][::-1] == words[j] or words[j][::-1] == words[i]:
                    result.append([i, j])
    
    return result