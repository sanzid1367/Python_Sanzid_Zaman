class Program:
    # --- Original Methods ---
    def subtract(self, first_number, second_number, third_number):
        answer = first_number - second_number - third_number
        return answer

    def add_up(self, first_number, second_number, third_number):
        answer = first_number + second_number + third_number
        return answer

    # --- NEW Methods Added ---
    def multiply(self, first_number, second_number, third_number):
        answer = first_number * second_number * third_number
        return answer

## Keeping division simple with just 2 numbers for clarity        
    def divide(self, first_number, second_number):
        # Simple division
        answer = first_number / second_number
        return answer

number1 = 100
number2 = 49
number3 = 51


cal = Program()

sub_answer = cal.subtract(number1, number2, number3)
add_answer = cal.add_up(number1, number2,number3)

mul_answer = cal.multiply(number1, number2, number3)
div_answer = cal.divide(number1, number2)

print("Subtraction answer is", sub_answer)
print("Addition answer is", add_answer)
print("Multiplication answer is", mul_answer)
print("Division answer is", div_answer)