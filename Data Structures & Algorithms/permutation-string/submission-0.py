class Solution:
 def checkInclusion(self, s1: str, s2: str) -> bool:
    n1, n2 = len(s1), len(s2)
    if n1 > n2:
        return False

    s1_count = {}
    window_count = {}

    # Initialize the frequency map for s1 and the first window of s2
    for i in range(n1):
        s1_count[s1[i]] = s1_count.get(s1[i], 0) + 1
        window_count[s2[i]] = window_count.get(s2[i], 0) + 1

    # Check the first window immediately
    if s1_count == window_count:
        return True

    # Slide the window across s2
    for i in range(n1, n2):
        new_char = s2[i]
        old_char = s2[i - n1]

        # Add the new character to the window
        window_count[new_char] = window_count.get(new_char, 0) + 1

        # Remove the character that is sliding out
        if window_count[old_char] == 1:
            del window_count[old_char]
        else:
            window_count[old_char] -= 1

        # Compare the maps (Python allows direct dict comparison)
        if s1_count == window_count:
            return True

    return False