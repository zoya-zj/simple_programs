class UnsignedBinary:
    def __init__(self, num):
        self.num = num
        self.bin = self.get_bin(num) # bin is in reverse order.
    
    def get_bin(self, num):
        if num < 0:
            return []
        elif(num == 0):
            return [0]

        r = []
        while num > 0:
            r.append(num % 2)
            num = int(num/2)
        
        return r
    
    def get_top_bit(self):
        return self.bin[-1]
    
    def get_num(self):
        return self.num
    
    def __str__(self):
        i =  len(self.bin)-1
        s = str(self.num) + ' -> '
        while i >= 0:
            s += str((self.bin[i]))
            i -= 1
        
        return s

class SignedBinary:
    def __init__(self, num):
        self.num = num
        self.bin = self.get_bin(self.num)

    def get_bin(self, num):
        r = [] # Return array.
        if num < 0:
            # Make number positive.
            num = num*-1

            # Get unsigned binary
            while num > 0:
                r.append(num % 2)
                num = int(num/2)

            # Flip digits
            j = 0
            while j < len(r):
                if r[j] == 1:
                    r[j] = 0
                else:
                    r[j] = 1
                j += 1 
            
            # Add 1
            carry = 1
            i = 0
            r.append(1)
            while i < len(r):
                if r[i] == 0 and carry == 0:
                    r[i] = 0
                    carry = 0

                if r[i] == 0 and carry == 1:
                    r[i] = 1
                    carry = 0

                if r[i] == 1 and carry == 0:
                    r[i] = 1
                    carry = 0

                if r[i] == 1 and carry == 1:
                    r[i] = 0
                    carry  = 1

                i += 1
            
            if carry == 1:
                r.append(1)

        elif num == 0:
            return [0]

        else:
            while num > 0:
                r.append(num % 2)
                num = int(num/2)
            r.append(0)

        return r
    
    def __str__(self):
        i =  len(self.bin)-1
        s = str(self.num) + ' -> '
        while i >= 0:
            s += str((self.bin[i]))
            i -= 1
        
        return s

if __name__ == "__main__":
    print(SignedBinary(0))
    print(SignedBinary(-12))
    print(SignedBinary(-10))
    print(SignedBinary(10))

    
