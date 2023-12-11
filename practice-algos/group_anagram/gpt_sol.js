function groupAnagrams(strs) {
    const groups = {};
    for (let s of strs) {
        const key = s.split('').sort().join('');
        if (!groups[key]) {
            groups[key] = [];
        }
        groups[key].push(s);
    }
    return Object.values(groups);
}
