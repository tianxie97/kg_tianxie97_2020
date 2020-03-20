import sys
import one_to_one_mapping

if __name__ == '__main__':
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    s = one_to_one_mapping.Solution()
    print(s.mapping(s1, s2))
