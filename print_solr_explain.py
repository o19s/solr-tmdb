def main():
    """
    Just a simple print to format a Solr explain plan.
    :return: None.
    """
    print(
        '"7555": "\n24.63695 = sum of:\n  12.318475 = max of:\n    10.573916 = weight(overview:rambo in 3199) [SchemaSimilarity], result of:\n      10.573916 = score(doc=3199,freq=2.0 = termFreq=2.0\n), product of:\n        8.204964 = idf, computed as log(1 + (docCount - docFreq + 0.5) / (docFreq + 0.5)) from:\n          7.0 = docFreq\n          27442.0 = docCount\n        1.2887219 = tfNorm, computed as (freq * (k1 + 1)) / (freq + k1 * (1 - b + b * fieldLength / avgFieldLength)) from:\n          2.0 = termFreq=2.0\n          1.2 = parameter k1\n          0.75 = parameter b\n          54.925552 = avgFieldLength\n          68.0 = fieldLength\n    12.318475 = weight(title:rambo in 3199) [SchemaSimilarity], result of:\n      12.318475 = score(doc=3199,freq=1.0 = termFreq=1.0\n), product of:\n        8.978624 = idf, computed as log(1 + (docCount - docFreq + 0.5) / (docFreq + 0.5)) from:\n          3.0 = docFreq\n          27760.0 = docCount\n        1.3719779 = tfNorm, computed as (freq * (k1 + 1)) / (freq + k1 * (1 - b + b * fieldLength / avgFieldLength)) from:\n          1.0 = termFreq=1.0\n          1.2 = parameter k1\n          0.75 = parameter b\n          2.9651656 = avgFieldLength\n          1.0 = fieldLength\n  12.318475 = weight(title:rambo in 3199) [SchemaSimilarity], result of:\n    12.318475 = score(doc=3199,freq=1.0 = termFreq=1.0\n), product of:\n      8.978624 = idf, computed as log(1 + (docCount - docFreq + 0.5) / (docFreq + 0.5)) from:\n        3.0 = docFreq\n        27760.0 = docCount\n      1.3719779 = tfNorm, computed as (freq * (k1 + 1)) / (freq + k1 * (1 - b + b * fieldLength / avgFieldLength)) from:\n        1.0 = termFreq=1.0\n        1.2 = parameter k1\n        0.75 = parameter b\n        2.9651656 = avgFieldLength\n        1.0 = fieldLength\n"'
    )

if __name__ == "__main__":
    main()
