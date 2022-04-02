# Plot inteference intensity of 2 - 7 source
# (CC 2011) Sparisoma Viridi
# dudung@fi.itb.ac.id
# 2011.04.04.40132

# postscript output is selected
set term post eps enhanced 26 lw 1.5

# size of the output
set size 1.2, 0.9

# some constants
PI = 3.14159
E0 = 1
wt = PI/2

# electric field E1 - E6
E1(dq) = E0 * sin(wt + 0 * dq)
E2(dq) = E0 * sin(wt + 1 * dq)
E3(dq) = E0 * sin(wt + 2 * dq)
E4(dq) = E0 * sin(wt + 3 * dq)
E5(dq) = E0 * sin(wt + 4 * dq)
E6(dq) = E0 * sin(wt + 5 * dq)
E7(dq) = E0 * sin(wt + 6 * dq)

# resultants and intensities
Et2(dq) = E1(dq) + E2(dq)
I2(dq) = Et2(dq) * Et2(dq)
Et3(dq) = E1(dq) + E2(dq) + E3(dq)
I3(dq) = Et3(dq) * Et3(dq)
Et4(dq) = E1(dq) + E2(dq) + E3(dq) + E4(dq)
I4(dq) = Et4(dq) * Et4(dq)
Et5(dq) = E1(dq) + E2(dq) + E3(dq) + E4(dq) + E5(dq)
I5(dq) = Et5(dq) * Et5(dq)
Et6(dq) = E1(dq) + E2(dq) + E3(dq) + E4(dq) + E5(dq) + E6(dq)
I6(dq) = Et6(dq) * Et6(dq)
Et7(dq) = E1(dq) + E2(dq) + E3(dq) + E4(dq) + E5(dq) + E6(dq) \
+ E7(dq)
I7(dq) = Et7(dq) * Et7(dq)

# axis settings
set xlabel "{/Symbol Df/p}"
set ylabel "{/Italics I}_0"
set xrange [-4:4]
set xtics 1
set grid lw 2

# samples resolution
set samples 5000

# two sources interference
set output "pattern-2.eps"
set yrange [0:4]
set ytics 1
plot I2(x * PI) t "" lw 3

# three sources interference
set output "pattern-3.eps"
set yrange [0:9]
set ytics 3
plot I3(x * PI) t "" lw 3

# four sources interference
set output "pattern-4.eps"
set yrange [0:16]
set ytics 4
plot I4(x * PI) t "" lw 3

# five sources interference
set output "pattern-5.eps"
set yrange [0:25]
set ytics 5
plot I5(x * PI) t "" lw 3

# six sources interference
set output "pattern-6.eps"
set yrange [0:36]
set ytics 6
plot I6(x * PI) t "" lw 3

# seven sources interference
set output "pattern-7.eps"
set yrange [0:49]
set ytics 7
plot I7(x * PI) t "" lw 3
