import os
from sys import argv, path
import subprocess
path.append(os.path.dirname(os.path.abspath(__file__)))

def check_output(output):
    out = output.decode()
    out = out.split("\n")
    idx = 0
    for i in range(len(out)):
      if("./" in out[i]):
        idx = i
        break
    out = out[idx+1:-1]
    out = "\n".join(out)
    return out

def test(num):
  cmd = f"cd questions/0{num}; make clean; make test"
  out = subprocess.check_output(cmd, shell=True)
  output = check_output(out)
  return output

def test1():
  out = test(1)
  print("Manual check required")

def test2():
  out = test(2)
  print("Manual check required")

def test3():
  out = test(3)
  line = out.split("\n")
  if(len(line) < 3 and "".join(line) != "#\n##\n###"):
    print("Test failed, at least 3 rows expected")
    print("Expected output:")
    print(f"#\n##\n###")
    print()
    print("Actual output:")
    print(out)
    if(len(line) < 3):
      return [0, "not attempted"]
    return [0, "attempted"]
  print("Test passed")
  return [1, "passed"]


def test4():
  out = test(4)
  line = out.split("\n")
  line = [line for line in line if line != ""]
  line = "\n".join(line)
  if(len(line.split("\n")) < 5 and line != "1\n12\n123\n12\n1"):
    print("Test failed, at least 5 rows expected")
    print("Expected output:")
    print(f"1\n12\n123\n12\n1")
    print()
    print("Actual output:")
    print(out)
    if(len(line.split("\n")) < 5):
      return [0, "not attempted"]
    return [0, "attempted"]
  print("Test passed")
  return [1, "passed"]

def test5():
  out = test(5)
  line = out.split("\n")
  line = [line for line in line if line != ""]
  line = "\n".join(line)
  if(len(line.split("\n")) < 3 and line != "Word: Hello World\nText: HloWrd"):
    print("Test failed, at least 2 rows expected")
    print("Expected output:")
    print(f"Word: Hello World\nText: HloWrd")
    print()
    print("Actual output:")
    print(out)
    if len(line.split("\n")) < 3:
      return [0, "not attempted"]
    return [0, "attempted"]
  print("Test passed")
  return [1, "passed"]

def test6():
  out = test(6)
  line = out.split("\n")
  line = [line for line in line if line != ""]
  line = "\n".join(line)
  length1 = line.split("\n")[1].split(" ")[-1]
  length2 = line.split("\n")[-1].split(" ")[-1]
  if(length1 != "11" and length2 != "16"):
    print("Test failed, incorrect values!")
    print("Expected output:")
    print(f"string: Hello World\nlength: 11")
    print(f"string: You're beautiful\nlength: 16")
    print()
    print("Actual output:")
    print(out)
    if(length1 == "0" and length2 == "0"):
      return [0, "not attempted"]
    return [0, "attempted"]
  print("Test passed")
  return [1, "passed"]

def test7():
  out = test(7)
  line = out.split("\n")
  line = [line for line in line if line != ""]
  line = "\n".join(line)
  print(len(line.split("\n")))
  if(line != "1\n1\n0\n0"):
    print("Test failed, incorrect values!")
    print("Expected output:")
    print(f"1\n1\n0\n0")
    print()
    print("Actual output:")
    print(out)
    if(line == "0\n0\n0\n0"):
      return [0, "not attempted"]
    return [0, "attempted"]
  print("Test passed")
  return [1, "passed"]

def test8():
  out = test(8)
  line = out.split("\n")
  line = [line for line in line if line != ""]
  line = "\n".join(line)
  if(line == "login failed!"):
    print("Test failed, incorrect values!")
    print("Expected output:")
    print(f"login success!")
    print()
    print("Actual output:")
    print(out)
    return [0, "manual check required"]
  print("Test passed")
  return [1, "passed"]

def test9():
  out = test(9)
  line = out.split("\n")
  line = [line for line in line if line != ""]
  line = "\n".join(line)
  expectedLines = [
    "First name: john",
    "Last name: doe",
    "Email: jdoe@gmail.com",
    "First name: jane",
    "Last name: doe",
    "Email: jdoe2@gmail.com"
  ]
  expectedLines = "\n".join(expectedLines)
  if(line != expectedLines):
    print("Test failed, incorrect values!")
    print("Expected output:")
    print(expectedLines)
    print()
    print("Actual output:")
    print(out)
    return [0, "manual check required"]
  print("Test passed")
  return [1, "passed"]

if __name__ == "__main__":
  if(len(argv) == 1):
    print("Invalid arguments")
    exit(1)
  test_num = argv[1]
  try:
    test_num = int(test_num)
    print(f"Testing question {test_num}")
    if(test_num == 1):
      test1()
    elif(test_num == 2):
      test2()
    elif(test_num == 3):
      test3()
    elif(test_num == 4):
      test4()
    elif(test_num == 5):
      test5()
    elif(test_num == 6):
      test6()
    elif(test_num == 7):
      test7()
    elif(test_num == 8):
      test8()
    elif(test_num == 9):
      test9()
    else:
      print("Invalid question number")
      exit(1)
  except ValueError:
    total = 0
    if(test_num == "all"):
      test1()
      test2()
      t3 = test3()
      total += t3[0]
      t4 = test4()
      total += t4[0]
      t5 = test5()
      total += t5[0]
      t6 = test6()
      total += t6[0]
      t7 = test7()
      total += t7[0]
      t8 = test8()
      total += t8[0]
      t9 = test9()
      total += t9[0]
      print(f"Total score: {total}/7")
      if(total == 7):
        print("Congratulations! You have passed the test")
      else:
        if(t3[0] == 0):
          if(t3[1] == "attempted"):
            print("Question 3 attempted")
          else:
            print("Question 3 not attempted")
        if(t4[0] == 0):
          if(t4[1] == "attempted"):
            print("Question 4 attempted")
          else:
            print("Question 4 not attempted")
        if(t5[0] == 0):
          if(t5[1] == "attempted"):
            print("Question 5 attempted")
          else:
            print("Question 5 not attempted")
        if(t6[0] == 0):
          if(t6[1] == "attempted"):
            print("Question 6 attempted")
          else:
            print("Question 6 not attempted")
        if(t7[0] == 0):
          if(t7[1] == "attempted"):
            print("Question 7 attempted")
          else:
            print("Question 7 not attempted")
        if(t8[0] == 0):
          print(t8[1])
        if(t9[0] == 0):
          print(t9[1])
    elif test_num == "clean":
      print("Cleaning up...")
      os.system("rm -rf *.pyc")
      os.system("rm -rf __pycache__")
      os.system("make clean")
      exit(0)
    else:
      print("Invalid question number")
      exit(1)

        