function productExceptSelf(nums) {
    let n = nums.length;
    let left = new Array(n), right = new Array(n), answer = new Array(n);

    left[0] = 1;
    for (let i = 1; i < n; i++) {
        left[i] = left[i - 1] * nums[i - 1];
    }

    right[n - 1] = 1;
    for (let i = n - 2; i >= 0; i--) {
        right[i] = right[i + 1] * nums[i + 1];
    }

    for (let i = 0; i < n; i++) {
        answer[i] = left[i] * right[i];
    }

    return answer;
}
