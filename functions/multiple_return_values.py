def become_warrior(first_name, last_name, power):
    title = f"{first_name} {last_name} the warrior"
    new_power = power + 1
    return title, new_power



    

def main():
    test("Frodo", "Baggins", 5)
    test("Bilbo", "Baggins", 10)
    test("Gandalf", "The Grey", 9000)



def test(input1, input2, input3):
    result1, result2 = become_warrior(input1, input2, input3)
    print(result1, "has a power level of:", result2)


main()

