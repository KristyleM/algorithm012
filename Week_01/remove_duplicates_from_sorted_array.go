func removeDuplicates(nums []int) int {
    p := 0
    for _, v := range(nums) {
        if v != nums[p]{
            nums[p+1] = v
            p++
        }
    }
    return p + 1
}

