# InterestingTaskWPaths
Decision of a employee task

Given text file, every line means path to file or dir.
If the line describes the file, then there is the file size in bytes is separated by a space.

input file:

 
TEST1\TEST\b 77
TEST1\TEST\C
TEST1\TEST\Z\test 111
TEST1\ABC\EFG\ZZZ\QWERTY\ASD\F\a.txt 16
TEST1\ABC\EFG\ZZZ\QWERTY\ASD\F\c.txt 32
TEST1\ABC\EFG\ZZZ\QWERTY\ASD\F\b.txt 32
TEST1\ABC\EFG\ZZZ\QWERTY\ASD\F\F
TEST2\TEST\Z\B
TEST2\TEST\Z\AAA\test 111
TEST2\TEST\Z\ZZZ\test 111
TEST2\TEST\Z\A
TEST2\TEST\Z\E
TEST3\TEST\B\XXX
TEST3\TEST\a 111
TEST4\ABC\EFG\ZZZ\QWERTY\ASD\F
TEST4\ABC\EFG\ZZZ\QWERTY\ASD\F2
TEST4\ABC\EFG\ZZZ\QWERTY\ASD\F3
TEST4\ABC\EFG\ZZ1
TEST4\ABC\EFG\ZZZ
TEST4\ABC\ZZZ
TEST4\ABC\EFG

 

Output file format:

TEST1
 ABC
  EFG
   ZZZ
    QWERTY
     ASD
      F
       F
       b.txt
       c.txt
       a.txt
 TEST
  C
  Z
   test
  b
TEST2
 TEST
  Z
   A
   AAA
    test
   B
   E
   ZZZ
    test
TEST3
 TEST
  B
   XXX
  a
TEST4
 ABC
  EFG
   ZZ1
   ZZZ
    QWERTY
     ASD
      F
      F2
      F3
  ZZZ
 

Inside the folder, first of all, subfolders should be displayed in alphabetical order, then files in descending order of size.
Files of the same size need to be sorted alphabetically.
All folders are written in capital letters, and files are written in lowercase.
Files can be without extension.
