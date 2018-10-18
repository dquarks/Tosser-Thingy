# NOTE: Strive toward using this same setup to
# create a similar UI/UX in Javascript/HTML using sliders
# that dependently recalibrate

from math import floor

# Some variables
var_a_one = 1;
var_b_one = 0.7; # vs 0.5
toss_first = 28.3495;
toss_second = 20;
toss_third = 10;
dashed_bar = "-----------------------------------------------------------------"

def split_rem(rate, amount):
    return [floor(amount), (float(amount) % rate) * 100];

input_amount = input("Enter the variable amount: ")

total_toss_first = float(input_amount) * toss_first;
toss_per_packet = total_toss_first
stoss_per_packet = total_toss_first / var_b_one
h_toss_per_packet = toss_per_packet / 2;
h_stoss_per_packet = h_toss_per_packet / var_b_one;

# [[0,0 | 0,1], [1,0 | 1,1], [2,0 | 2,1], [3,0 | 3,1]]
# [[toss packets, toss percents], [s-toss packets, s-toss percents],
# [half toss packets, toss percents], [half s-toss packets, s-toss percents]]

text_dump = [split_rem(var_a_one, toss_per_packet),split_rem(var_b_one, stoss_per_packet),
             split_rem(var_a_one, h_toss_per_packet),split_rem(var_b_one, h_stoss_per_packet)]
row_1 = ["Types", "Packets", "% leftover", "$$$"]
row_2 = ["Toss(F)", "S-Toss(F)", "[Toss_z", "[S-Toss_z"]
row_3 = [text_dump[0][0], text_dump[1][0], text_dump[2][0], text_dump[3][0]] # Packets
row_4 = [text_dump[0][1], text_dump[1][1], text_dump[2][1], text_dump[3][1]] # Percentages
row_5 = [float(row_3[0]) * toss_second, float(row_3[1]) * toss_third, float(row_3[2]) * toss_second, float(row_3[3]) * toss_third]

print dashed_bar
print "%s           %s          %s              %s" % tuple(row_1)
print dashed_bar
for i in range(0, len(row_1)):
    print "{}           {}            {}                {}".format(row_2[i], row_3[i], floor(row_4[i]), row_5[i])
print dashed_bar
