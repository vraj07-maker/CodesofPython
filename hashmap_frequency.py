def Solution(count):
    counter = {}
    for char in count:
        counter[char] = counter.get(char, 0) + 1
    return counter


if __name__ == "__main__":
    test_str = "goldmansachs"
    result = Solution(test_str)

    print(f"Character counts for '{test_str}':")
    for char, counter in result.items():
        print(f"  '{char}': {counter}")