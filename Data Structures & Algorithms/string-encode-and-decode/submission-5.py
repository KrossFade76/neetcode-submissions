class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "[]"
        return_str = "separator".join(strs)
        return return_str

    def decode(self, s: str) -> List[str]:
        if s == "[]":
            return []
        return_list = s.split("separator")
        return return_list