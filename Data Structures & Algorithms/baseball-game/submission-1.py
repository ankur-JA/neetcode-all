class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []

        for i in range(len(operations)):
            if operations[i] == "C":
                records.pop()
            elif operations[i] == "D":
                n = records[-1]
                records.append(2*n)
            elif operations[i] == "+":
                sum = records[-1] + records[-2]
                records.append(sum)
            else:
                records.append(int(operations[i]))
    
        sum = 0
        for num in records: # 5, -2, -4, 9, 8, 16
            sum += num
    
        return sum