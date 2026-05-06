class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split('/') # splits each string in the string by the / slash
        for part in parts:
            if part in {"", "."}:
                continue
            if part != "..":
                stack.append(part)
            else:
                if stack:
                    stack.pop()
        return "/" + "/".join(stack)
