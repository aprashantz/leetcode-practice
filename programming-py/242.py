def isAnagram(self, s: str, t: str) -> bool:
    s_count, t_count = {}, {}
    for each in s:
        s_count[each] = s.count(each)
    for each in t:
        t_count[each] = t.count(each)
    return s_count == t_count
