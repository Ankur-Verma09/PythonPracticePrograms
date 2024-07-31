class ArmstrongNumber:
    @staticmethod
    def armstrong_number():
        start_from = int(input('Enter the starting number: '))
        ends_at = int(input('Enter the last number: '))
        for num in range(start_from, ends_at):
            temp_num = num
            sum = 0
            order = len(str(num))
            while temp_num > 0:
                digit = temp_num % 10
                sum += digit ** order
                temp_num //=10

            if num == sum:
                print(num)

    armstrong_number()
