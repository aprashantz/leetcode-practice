/// take list of numbers and return length of non duplicate numbers
// The judge will test your solution with the following code:

// int[] nums = [...]; // Input array
// int[] expectedNums = [...]; // The expected answer with correct length

// int k = removeDuplicates(nums); // Calls your implementation

// assert k == expectedNums.length;
// for (int i = 0; i < k; i++) {
//     assert nums[i] == expectedNums[i];
// }

func removeDuplicated(nums: inout [Int])-> Int{
        var uniqueUptoIndex: Int = 0;
        for index: Int in 1..<nums.count{
            if(nums[uniqueUptoIndex] != nums[index]){
                uniqueUptoIndex += 1;
                nums[uniqueUptoIndex] = nums[index];
            }
        }
        return uniqueUptoIndex+1
}


// to test
var sample1 = [0,0,1,2,3]
var sample2: [Int] = [1,2,3];
print(removeDuplicated(nums: &sample1)) // should be 4
print(removeDuplicated(nums: &sample2)) // should be 3