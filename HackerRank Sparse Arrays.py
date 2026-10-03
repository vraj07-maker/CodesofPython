def matchingStrings(stringList, queries):
    """Counts how many times each query string appears in stringList using an O(N + Q) hash map approach."""
    # Step 1: Build a frequency map for all strings in stringList
    frequency_map = {}
    for string in stringList:
        frequency_map[string] = frequency_map.get(string, 0) + 1

    # Step 2: Query the frequency map for each item in queries
    results = []
    for query in queries:
        results.append(frequency_map.get(query, 0))

    return results


# Local test runner
if __name__ == "__main__":
    sample_stringList = ["aba", "baba", "aba", "xzxb"]
    sample_queries = ["aba", "xzxb", "ab"]
    print(matchingStrings(sample_stringList, sample_queries))  # Output: [2, 1, 0]