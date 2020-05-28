# Read lines as a list
fh = open("output.txt", "r", encoding="utf8")
lines = fh.readlines()
fh.close()
# Weed out blank lines with filter
lines = filter(lambda x: not x.isspace(), lines)
# Write
fh = open("output2.txt", "w", encoding="utf8")
fh.write("".join(lines))
# should also work instead of joining the list:
# fh.writelines(lines)
fh.close()
