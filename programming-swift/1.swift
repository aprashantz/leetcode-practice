func twoSum(nums: [Int], target: Int)-> [Int]{
    for i: Int in 0..<nums.count{
        for j: Int in i+1..<nums.count{
            if ( nums[i] + nums[j] == target){
                return [i,j];
            }
        }
    }
    return [];
}

// test below
print(twoSum(nums: [2, 7, 15, 11], target: 9))