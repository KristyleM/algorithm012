func twoSum(nums []int, target int) []int {
    dic := make(map[int]int)
	result := make([]int, 0)
	for index, num := range nums {
		_, ok := dic[target - num]
		if ok {
			result = append(result, index)
			result = append(result, dic[target - num])
			break
		}
		dic[num] = index
	}
	return result
}

