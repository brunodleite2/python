class Solution:
    def reverse(self, x: int) -> int:      
        is_negative = False
        
        if x < 0: 
          is_negative = True
          x *= -1
          
        x_str = str(x)
        x_list = list(x_str)
        x_list_reversed = x_list[::-1]
        
        print(x_list_reversed)
        x_string = ''.join([char for char in x_list_reversed ])
        
        if is_negative:
          x_reversed =  int(x_string) * -1
        else:
          x_reversed =  int(x_string)
               

        if x_reversed > (2**31 -1) or x_reversed < 2**31 * -1:
          return 0
        
        return x_reversed
        