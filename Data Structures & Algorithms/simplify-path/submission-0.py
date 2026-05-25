class Solution:
    def simplifyPath(self, path: str) -> str:
        new_path = path.split("/")
        s = []
        res = "/"
        for i in range(len(new_path)):
            if s and new_path[i] == "..":
                s.pop()
            elif new_path[i] == "" or new_path[i] == ".":
                continue
            else:
                if new_path[i] != "..":
                    s.append(new_path[i])
        return "/" + "/".join(s)

            