func isPalindrome(num: Int)->Bool{
    return String(num) == String(String(num).reversed());
}

// test below
print(isPalindrome(num: 123));
print(isPalindrome(num: 121));