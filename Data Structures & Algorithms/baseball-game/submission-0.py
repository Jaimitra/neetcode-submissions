class Solution:
    def calPoints(self, operations: List[str]) -> int:
        data = list()
        for i in range(len(operations)):
            val = operations[i]
            if val not in ["+","D","C"]:
                data.append(int(val))
            elif val == "+":
                data.append(data[-1]+data[-2])
            elif val == "D":
                data.append(data[-1]*2)
            else:
                data.pop()

        return sum(data) 
        