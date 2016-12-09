from lab_generator_tests import LabGenerator_tests
import sys


def main_function(argv):
    output_file = open("unit_tests_result",'w')
    tests = LabGenerator_tests()
    output_file.write(tests.get_all_tests())
    output_file.close

if __name__ == "__main__":
    sys.exit(main_function(sys.argv))
