from collections import defaultdict

def group_anagrams(strings):
    """
    Groups the anagrams together in an array of strings.

    Parameters:
        strings (List[str]): The list of strings to be grouped.

    Returns:
        List[List[str]]: A list of lists containing grouped anagrams.

   
    """

    anagram_groups = defaultdict(list)

    for string in strings:
        sorted_string = ''.join(sorted(string))
        
        anagram_groups[sorted_string].append(string)
        
    grouped_anagrams = list(anagram_groups.values())
   
    return grouped_anagrams


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))