# OPTIMIZED
import sys, re                                                                                                                                                                             
m=["--.. . .-. ---","--- -. .","- .-- ---","- .... .-. . .","..-. --- ..- .-.","..-. .. ...- .","... .. -..-","... . ...- . -.",". .. --. .... -","-. .. -. .","-- .. -. ..- ...",".--. .-.. ..- ..."]
n="0123456789-+"   
#n=["0","1","2","3","4","5","6","7","8","9","-","+"]                                                                                                                                       
print (" / ").join([m[n.index(c)] for c in str(eval(("").join([n[m.index(p.strip())] for p in sys.argv[1].split("/")])))])                                                                     



# UNDERSTANDING THE CODE - solution for all numbers

# Read stdin and split on dash w. list comprehension
# For each morse part, find it's related numeric value in num using index position
# Calculate result using eval on arithmetic operation
# For each char in resulting number, print associated morse value


# 5 + 5 + 3 - 20
# "..-. .. ...- ./.--. .-.. ..- .../..-. .. ...- ./.--. .-.. ..- .../ - .... .-. . ./ -- .. -. ..- ... / - .-- --- / --.. . .-. ---"
# ans -- .. -. ..- ... ... . ...- . -. (-7)

# 4 + 4 - 7
# "..-. --- ..- .-. / .--. .-.. ..- ... / ..-. --- ..- .-. / -- .. -. ..- ...  /  ... . ...- . -."
# ans --- -. . (1)

# 11 + 2 + 6 - 8 
# "--- -. . / --- -. . /.--. .-.. ..- .../ - .-- ---/.--. .-.. ..- .../... .. -..- / -- .. -. ..- .../ . .. --. .... -"
# ans (11)