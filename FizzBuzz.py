"""
Q1. Why is the report method untestable ? [2 pts]

The report method is using the open command which is an external collaborator, the external collaborator should
be passed as an argument to the report method


Q2. How will you change the api of the report method to make it more testable ? [2 pts]

The defintion of report will accept three arguments report_file(self, numbers,fileWrapper)
the calls to open , write and close will be substituted by the fileWrapper.
This wrapper can be mocked and code logic can be tested accordingly.


"""
class FizzBuzz(object):
    def report(self, numbers):

        report_file = open('c:/temp/fizzbuzz_report.txt', 'w')

        for number in numbers:
            msg = str(number) + " "
            fizzbuzz_found = False
            if number % 3 == 0:
                msg += "fizz "
                fizzbuzz_found = True
            if number % 5 == 0:
                msg += "buzz "
                fizzbuzz_found = True

            if fizzbuzz_found:
                report_file.write(msg + "\n")

        report_file.close()

if "__main__" == __name__:
    fb = FizzBuzz()
    fb.report(range(100))

            
