class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        res = 0

        # for op in operations:
        #     if op == "D":
        #         records.append(2 * records[-1])
        #     elif op == "C":
        #         records.pop()
        #     elif op == "+":
        #         records.append(records[-1] + records[-2])
        #     else:
        #         records.append(int(op))
            
        # return sum(records)

        for op in operations:
            if op == "D":
                res += (2 * records[-1])
                records.append(2 * records[-1])
            elif op == "C":
                res -= records[-1]
                records.pop()
            elif op == "+":
                res += (records[-1] + records[-2])
                records.append(records[-1] + records[-2])
            else:
                res += int(op)
                records.append(int(op))

        return res