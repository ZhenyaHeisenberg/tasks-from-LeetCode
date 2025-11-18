class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]

        for j in range(2, numRows+1):
            string = output[j-2]
            x = []
            x.append(string[0])
            for i in range(len(string)-1):
                x.append(string[i]+string[i+1])
            x.append(string[-1])
            output.append(x)

        return output